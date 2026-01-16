# 🐳 /docker/Dockerfile

FROM python:3.10-slim

# Sistema
RUN apt update && \
    apt install -y aria2 rclone p7zip-full ca-certificates && \
    rm -rf /var/lib/apt/lists/*

# Diretório de trabalho
WORKDIR /app

# Python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Código
COPY . .

# Streamlit
EXPOSE 8501

ENV PYTHONUNBUFFERED=1

CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]

