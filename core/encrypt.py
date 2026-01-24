# 🔐 /core/encrypt.py

import subprocess
import os

def encrypt_folder(source_dir: str, output_dir: str, password: str):
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, "vaultstream_encrypted.7z")

    # -mhe=on: Criptografa nomes de arquivos (essencial para o Drive não ver)
    # -mx=1: Compressão "Fastest" (evita travar a CPU por horas)
    # -p: Senha
    cmd = [
        "7z", "a", f"-p{password}", "-mhe=on", "-mx=1",
        output_file, source_dir
    ]

    yield f"🔐 Iniciando criptografia rápida (AES-256)..."

    try:
        # O 7-zip é pesado, capturar cada linha de progresso no Gradio pode causar o deadlock
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    
        # Monitoramento simples para não travar
        while True:
            line = process.stdout.readline()
            if not line and process.poll() is not None:
                break
            # Apenas envia logs de arquivos grandes ou progresso em blocos
            if "Compressing" in line or "Everything is Ok" in line:
                yield f"⚡ {line.strip()}"

        if process.returncode == 0:
            yield f"✅ Arquivo gerado: {output_file}"
        else:
            yield "❌ Erro na criptografia. Verifique espaço em disco."

    except Exception as e:
        yield f"⚠️ Falha crítica no 7z: {str(e)}"
    
