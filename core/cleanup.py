# ♻️ core/cleanup.py

import shutil
import os

def cleanup_paths(*paths):
    for path in paths:
        if os.path.exists(path):
            shutil.rmtree(path, ignore_errors=True)
