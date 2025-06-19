import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QFileDialog, QListWidgetItem,
    QMessageBox, QCheckBox, QVBoxLayout, QWidget, QLabel, QTableWidget,
    QTableWidgetItem, QPushButton
)
from PyQt6.QtCore import Qt
from PyQt6.uic import loadUi


class DataAnalyzerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("main_window.ui", self)

        self.addFilePushButton.clicked.connect(self.load_files)
        self.generatePushButton.clicked.connect(self.generate_chart)
        self.FilesListWidget.itemDoubleClicked.connect(self.show_item_info)
        self.previewButton.clicked.connect(self.preview_data)

        self.selected_files = {}
        self.dataframes = {}
        self.columns = set()

        self.chartTypeComboBox.addItems(["Bar Chart", "Pie Chart", "Comparison Chart"])

        self.filterLayout = QVBoxLayout()
        self.filterWidget = QWidget()
        self.filterWidget.setLayout(self.filterLayout)
        self.scrollArea.setWidget(self.filterWidget)
        self.scrollArea.setWidgetResizable(True)
        self.filterCheckboxes = {}

        self.scrollAreaLabel = QLabel("No columns found", self)
        self.scrollAreaLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.scrollAreaLabel.setStyleSheet("font: 12pt 'Arial'; color: grey;")
        self.scrollAreaLabel.setGeometry(616, 180, 141, 61)
        self.scrollAreaLabel.show()

    def read_file(self, file):
        try:
            if file.endswith((".xls", ".xlsx")):
                return pd.read_excel(file)
            elif file.endswith(".csv"):
                return pd.read_csv(file)
            elif file.endswith(".ods"):
                return pd.read_excel(file, engine='odf')
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error reading file {file}: {e}")
        return None
    def randum_colors(self, n):
        import random
        """Generate a list of n random hex color codes."""
        if n <= 0:
            return []
        if n > 16777215:  # 0xFFFFFF + 1
            raise ValueError("n must be less than or equal to 16777215 (0xFFFFFF + 1)")
        return [f'#{random.randint(0, 0xFFFFFF):06x}' for _ in range(n)]
    
    def load_files(self):
        files, _ = QFileDialog.getOpenFileNames(
            self, "Select Files", "", "Excel Files (*.xlsx *.xls *.ods);;CSV Files (*.csv)"
        )

        if files:
            for file in files:
                file_name = os.path.basename(file)

                if file_name not in self.selected_files:
                    df = self.read_file(file)
                    if df is not None:
                        self.selected_files[file_name] = file
                        self.dataframes[file_name] = df
                        self.FilesListWidget.addItem(QListWidgetItem(file_name))
                        self.columns.update(df.columns)

            self.update_filter_options()

    def update_filter_options(self):
        for i in reversed(range(self.filterLayout.count())):
            self.filterLayout.itemAt(i).widget().setParent(None)

        self.filterCheckboxes.clear()
        for column in sorted(self.columns):
            checkbox = QCheckBox(column)
            self.filterCheckboxes[column] = checkbox
            self.filterLayout.addWidget(checkbox)

        if self.columns:
            self.scrollAreaLabel.hide()
        else:
            self.scrollAreaLabel.show()

    def show_item_info(self, item):
        file_name = item.text()
        full_path = self.selected_files.get(file_name, "Unknown Path")
        response = QMessageBox.question(
            self, "Full Path", f"Full path of {file_name}:\n{full_path}\n\nDo you want to remove this file?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if response == QMessageBox.StandardButton.Yes:
            self.remove_file(item)
        

    def remove_file(self, item):
        file_name = item.text()
        if file_name in self.selected_files:
            del self.selected_files[file_name]
            del self.dataframes[file_name]
            self.FilesListWidget.takeItem(self.FilesListWidget.row(item))

            self.columns.clear()
            for df in self.dataframes.values():
                self.columns.update(df.columns)

            self.update_filter_options()
            QMessageBox.information(self, "Removed", f"Removed file: {file_name}")

    def preview_data(self):
        item = self.FilesListWidget.currentItem()
        if item:
            file_name = item.text()
            df = self.dataframes.get(file_name)
            if df is not None:
                preview_window = QMainWindow(self)
                preview_window.setWindowTitle(f"Preview - {file_name}")
                table = QTableWidget(preview_window)
                table.setRowCount(min(20, len(df)))
                table.setColumnCount(len(df.columns))
                table.setHorizontalHeaderLabels(df.columns.astype(str).tolist())
                for i in range(min(20, len(df))):
                    for j, col in enumerate(df.columns):
                        item = QTableWidgetItem(str(df.iloc[i, j]))
                        table.setItem(i, j, item)
                preview_window.setCentralWidget(table)
                preview_window.resize(800, 400)
                preview_window.show()
        else:
            QMessageBox.warning(self, "No File Selected", "Please select a file to preview.")

    def generate_chart(self):
        selected_columns = [col for col, cb in self.filterCheckboxes.items() if cb.isChecked()]
        chart_type = self.chartTypeComboBox.currentText()

        if not selected_columns:
            QMessageBox.warning(self, "Warning", "Please select at least one column for visualization!")
            return

        if chart_type in ["Bar Chart", "Pie Chart"] and len(selected_columns) > 1:
            QMessageBox.warning(self, "Warning", "Please select only one column for this chart type!")
            return

        plt.figure(figsize=(8, 5))

        if chart_type == "Comparison Chart":
            for df in self.dataframes.values():
                for column in selected_columns:
                    if column in df.columns:
                        df[column].value_counts().plot(kind="bar", alpha=0.6, label=column)
            plt.legend()
            plt.ylabel("Frequency")
            plt.title("Comparison of Selected Columns")

        else:
            col = selected_columns[0]
            all_data = pd.concat([
                df[col] for df in self.dataframes.values() if col in df.columns
            ])
            value_counts = all_data.value_counts()

            if chart_type == "Bar Chart":
                value_counts.plot(kind="bar", color="lightgreen")
                plt.ylabel("Frequency")
                plt.title(f"Bar Chart of {col}")

            elif chart_type == "Pie Chart":
                value_counts.plot(
                    kind="pie", autopct="%1.1f%%",
                    colors= self.randum_colors(len(value_counts))
                )
                plt.ylabel("")
                plt.title(f"Pie Chart of {col}")

        plt.xticks(rotation=45)
        plt.tight_layout()

        plt.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DataAnalyzerApp()
    window.show()
    sys.exit(app.exec())
