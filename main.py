# 🚀 main.py

import argparse
from core.pipeline import run_pipeline

def main():
    parser = argparse.ArgumentParser(description="VaultStream CLI")
    parser.add_argument("--magnets", required=True, help="Arquivo .txt com magnet links")
    parser.add_argument("--destino", default="GoogleDrive")
    parser.add_argument("--zipar", action="store_true")

    args = parser.parse_args()

    with open(args.magnets) as f:
        links = [l.strip() for l in f if l.strip()]

    run_pipeline(links, args.destino, args.zipar)

if __name__ == "__main__":
    main()
