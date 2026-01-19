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

# Evita cache desnecessário para reduzir o tamanho da imagem
RUN pip install --no-cache-dir -r requirements.txt

# Ajustamos para garantir que o Gradio escute em todos os interfaces (0.0.0.0), essencial para Docker.
ENV GRADIO_SERVER_NAME="0.0.0.0"
EXPOSE 7860
CMD ["python", "ui/gradio_app.py"]
