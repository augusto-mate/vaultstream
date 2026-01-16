# 📦 /core/torrent_downloader.py

import subprocess
import os

def download_torrent(magnet_link: str, download_dir: str):
    os.makedirs(download_dir, exist_ok=True)

    cmd = [
        "aria2c",
        "--enable-dht=true",
        "--follow-torrent=mem",
        "--seed-time=0",
        "--summary-interval=10",
        "-d", download_dir,
        magnet_link
    ]

    process = subprocess.run(cmd, capture_output=True, text=True)

    if process.returncode != 0:
        raise RuntimeError(process.stderr)

    return download_dir
