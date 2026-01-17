# 🐳 /docker/Dockerfile

FROM python:3.10-slim

# Sistema
RUN apt update && apt install -y \
    aria2 p7zip-full rclone \
    && rm -rf /var/lib/apt/lists/*

# Diretório de trabalho
WORKDIR /app

# Python deps
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

# Gradio
EXPOSE 7860
CMD ["python", "ui/gradio_app.py"]
