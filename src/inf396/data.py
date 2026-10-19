"""Carga y descarga del dataset."""

import io
import urllib.request
import zipfile
from pathlib import Path

import pandas as pd

UCI_URL = "https://archive.ics.uci.edu/static/public/572/taiwanese+bankruptcy+prediction.zip"
DATA_DIR = Path(__file__).resolve().parents[2] / "data"
CSV_PATH = DATA_DIR / "taiwanese_bankruptcy.csv"
TARGET = "Bankrupt?"


def download_dataset(path: Path = CSV_PATH, force: bool = False) -> Path:
    """Descarga el dataset desde UCI y lo guarda en `path`."""
    if path.exists() and not force:
        return path
    path.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(UCI_URL, timeout=60) as resp:
        payload = resp.read()
    with zipfile.ZipFile(io.BytesIO(payload)) as zf:
        path.write_bytes(zf.read("data.csv"))
    return path


def load_dataset(path: Path = CSV_PATH) -> pd.DataFrame:
    """Carga el CSV con los nombres de columna sin espacios sobrantes."""
    if not path.exists():
        raise FileNotFoundError(f"{path} no existe; ejecutar `uv run python scripts/download_data.py`")
    df = pd.read_csv(path)
    df.columns = df.columns.str.strip()
    return df
