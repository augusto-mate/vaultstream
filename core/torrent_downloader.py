# 📦 /core/torrent_downloader.py

import subprocess
import os
import re

def download_torrent(magnet_link: str, download_dir: str):
    os.makedirs(download_dir, exist_ok=True)

    cmd = [
        "aria2c",
        "--enable-dht=true",
        "--follow-torrent=mem",
        "--seed-time=0",
        "--summary-interval=1", # Atualização a cada 1 segundo
        "--console-log-level=notice",
        "-d", download_dir,
        magnet_link
    ]

    # Usamos Popen para ler a saída em tempo real
    process = subprocess.Popen(
        cmd, 
        stdout=subprocess.PIPE, 
        stderr=subprocess.STDOUT, 
        text=True, 
        bufsize=1
    )

    print(f"📡 Conectando aos peers para: {magnet_link[:50]}...")

    for line in process.stdout:
        line = line.strip()
        # Captura a linha de status do Aria2 (Ex: [#ada432 1.1MiB/4.3MiB(25%) CN:15 SD:2 DL:1.2MiB])
        if "[" in line and "]" in line and "(" in line:
            yield f"📥 {line}"
        elif "Download Complete" in line:
            yield "✅ Download finalizado com sucesso."

    process.wait()
    if process.returncode != 0:
        yield f"❌ Erro no Aria2 (Código {process.returncode})"
