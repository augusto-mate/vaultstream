# 🔐 /core/encrypt.py

import subprocess
import os

def encrypt_folder(source_dir: str, output_dir: str, password: str):
    os.makedirs(output_dir, exist_ok=True)
    output_file = f"{output_dir}/vaultstream_encrypted.7z"

    cmd = [
        "7z", "a",
        "-t7z",
        f"-p{password}",
        "-mhe=on",
        output_file,
        source_dir
    ]

    subprocess.run(cmd, check=True)
    return output_file
