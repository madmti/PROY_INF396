"""Descarga el Taiwanese Bankruptcy Prediction Dataset (UCI #572) a data/."""

import argparse

from inf396.data import CSV_PATH, download_dataset


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--force", action="store_true", help="volver a descargar si ya existe")
    args = parser.parse_args()
    path = download_dataset(force=args.force)
    print(f"Dataset disponible en {path.relative_to(CSV_PATH.parents[1])}")


if __name__ == "__main__":
    main()
