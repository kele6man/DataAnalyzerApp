# 📊 DataAnalyzerApp

DataAnalyzerApp е настолно GUI приложение, създадено с  **Python + PyQt6** , което позволява:

* Импортиране на файлове във формат  **CSV** , **Excel (.xls, .xlsx)** и **ODS (.ods)**
* Визуализация на данните чрез  **бар** , **пай** или **сравнителни графики**
* Избор на колони чрез чекбоксове
* Преглед на съдържанието на файла в таблица
* Случайни цветови палитри при визуализация

---

## 📸 Преглед



> Main window:
> ![screenshots/main_window.png](https://github.com/kele6man/DataAnalyzerApp/blob/main/screenshots/main_window.png?raw=true)
>
>
> Pie Scheme:
> ![screenshots/main_window.png](https://github.com/kele6man/DataAnalyzerApp/blob/main/screenshots/pie.png?raw=true)
>

---

## 🧠 Как работи

1. Стартирай приложението.
2. Използвай бутона `+` за избор на файлове.
3. Избери желани колони с чекбоксове.
4. Избери вид графика от падащото меню.
5. Натисни `Generate Chart` за визуализация.
6. (По избор) Запази графиката като `.png` или `.jpg`.

---

## 🧰 Зависимости

* Python 3.10+
* pandas
* matplotlib
* PyQt6
* odfpy (за ODS файлове)

---

## ⚙️ Стартиране (без Docker)

### 🔵 Windows / Linux / macOS

1. Клонирай хранилището:

```bash
git clone https://github.com/kele6man/DataAnalyzerApp.git
cd DataAnalyzerApp
```

2. Инсталирай зависимостите:

```bash
pip install -r requirements.txt
```

3. Стартирай приложението:

```bash
python main.py
```

---

## 🐳 Стартиране с Docker

### 1. Изгради Docker контейнера:

```bash
docker build -t data-analyzer-app .
```

### 2. Стартирай (на Linux):

```bash
sudo xhost +local:docker
sudo docker run -e DISPLAY=$DISPLAY \
           -v /tmp/.X11-unix:/tmp/.X11-unix \
           --rm data-analyzer-app
```

### 2. Стартирай (на macOS с XQuartz):

```bash
xhost + 127.0.0.1
docker run -e DISPLAY=host.docker.internal:0 \
           -v /tmp/.X11-unix:/tmp/.X11-unix \
           --rm data-analyzer-app
```

---
