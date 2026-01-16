# 📤 /core/uploader.py

import subprocess
import os

def upload_with_rclone(file_path: str, remote: str, folder: str):
    cmd = [
        "rclone",
        "copy",
        file_path,
        f"{remote}:{folder}"
    ]

    subprocess.run(cmd, check=True)
