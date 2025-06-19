FROM python:3.11-slim

# Install system dependencies for GUI and Qt
RUN apt-get update && apt-get install -y \
    libgl1 \
    libx11-xcb1 \
    libxrender1 \
    libxcb1 \
    libxcb-cursor0 \
    libxcb-render0 \
    libxcb-shape0 \
    libxcb-shm0 \
    libxcb-xfixes0 \
    libxcb-icccm4 \
    libxcb-image0 \
    libxcb-keysyms1 \
    libxcb-randr0 \
    libxcb-render-util0 \
    libxcb-util1 \
    libxcb-xinerama0 \
    libxkbcommon-x11-0 \
    qt6-base-dev \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Allow X11 GUI access
ENV QT_X11_NO_MITSHM=1

# Entry point
CMD ["python", "main.py"]
