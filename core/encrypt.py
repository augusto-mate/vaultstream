# 🔐 /core/encrypt.py

import subprocess
import os

def encrypt_folder(source_dir: str, output_dir: str, password: str):
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, "vaultstream_encrypted.7z")

    # -mhe=on: Criptografa nomes de arquivos (essencial para o Drive não ver)
    # -mx0: Modo "Copy" (Sem compressão, apenas senha. É instantâneo!)
    # -p: Senha
    cmd = [
        "7z", "a", f"-p{password}", "-mhe=on", "-mx0",
        output_file, f"{source_dir}/*"
    ]

    yield f"🔐 Gerando container criptografado (Modo Ultra-Rápido)..."

    try:
        # O 7-zip é pesado, capturar cada linha de progresso no Gradio pode causar o deadlock
        result = subprocess.run(cmd, capture_output=True, text=True)
    
        # Monitoramento simples para não travar
        #while True:
            #line = process.stdout.readline()
            #if not line and process.poll() is not None:
                #break
            # Apenas envia logs de arquivos grandes ou progresso em blocos
            #if "Compressing" in line or "Everything is Ok" in line:
                #yield f"⚡ {line.strip()}"

        if result.returncode == 0:
            yield f"✅ Arquivo gerado: {output_file}"
        else:
            yield "❌ Erro na criptografia: {result.stderr[:200]}"

    except Exception as e:
        yield f"⚠️ Falha crítica no 7z: {str(e)}"
    
