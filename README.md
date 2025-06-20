# 📊 DataAnalyzerApp (English)

DataAnalyzerApp is a desktop GUI application built with **Python + PyQt6** that allows:

* Importing  **CSV** , **Excel (.xls, .xlsx)** and **ODS (.ods)**, **LibreOffice** and open **office** files
* Visualizing data using  **bar** ,  **pie** , or **comparison** charts
* Selecting columns via checkboxes
* Previewing file content in a table
* Using randomized color palettes for plots

---

## 📸 Preview


> Main window:
![screenshots/main_window.png](https://github.com/kele6man/DataAnalyzerApp/blob/main/screenshots/main_window.png?raw=true)

> Pie Scheme:
![screenshots/main_window.png](https://github.com/kele6man/DataAnalyzerApp/blob/main/screenshots/pie.png?raw=true)

---

## 🧠 How it works

1. Start the application.
2. Use the `+` button to add files.
3. Select desired columns with checkboxes.
4. Choose a chart type from the dropdown.
5. Click `Generate Chart` to visualize.
6. (Optional) Save the chart as `.png` or `.jpg`.

---

## 🧰 Dependencies

* Python 3.10+
* pandas
* matplotlib
* PyQt6
* odfpy (for ODS support)

---

## ⚙️ Run without Docker

### 🔵 Windows / Linux / macOS

1. Clone the repository:

```shell
git clone https://github.com/kele6man/DataAnalyzerApp.git
cd DataAnalyzerApp
```

2. Install dependencies:

```shell
pip install -r requirements.txt
```

3. Run the app:

```shell
python main.py
```

---

## 🐳 Run with Docker

### 1. Build the container:

```shell
docker build -t data-analyzer-app .
```

### 2. Run (Linux):

```shell
sudo xhost +local:docker
sudo docker run -e DISPLAY=$DISPLAY \
           -v /tmp/.X11-unix:/tmp/.X11-unix \
           --rm data-analyzer-app
```

### 2. Run (macOS with XQuartz):

```shell
xhost + 127.0.0.1
docker run -e DISPLAY=host.docker.internal:0 \
           -v /tmp/.X11-unix:/tmp/.X11-unix \
           --rm data-analyzer-app
```

---
