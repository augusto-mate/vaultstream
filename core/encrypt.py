# 🔐 /core/encrypt.py

import subprocess
import os

def encrypt_folder(source_dir: str, output_dir: str, password: str):
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, "vaultstream_encrypted.7z")

    cmd = [
        "7z", "a", "-t7z", f"-p{password}", "-mhe=on",
        output_file, source_dir
    ]

    process = subprocess.Popen(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1
    )

    for line in process.stdout:
        # Captura apenas a porcentagem de compressão do 7z
        if "%" in line:
            yield f"🔐 Criptografando: {line.strip()}"

    process.wait()
    yield f"✅ Arquivo gerado: {output_file}"
    return output_file
