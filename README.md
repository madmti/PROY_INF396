# INF396 - Modelos alternativos con menos informacion para la prediccion de quiebra empresarial

Proyecto del curso INF396 (Introduccion a la Ciencia de Datos).
Integrantes: Tomas Molina R., Matias Penaloza B.

## Estructura

```
data/          Datos (los CSV no se versionan)
notebooks/     EDA y experimentos exploratorios
src/inf396/    Codigo reutilizable (datos, preprocesamiento, modelos, evaluacion)
scripts/       Scripts ejecutables
results/       Tablas y figuras generadas
report/        Informe LaTeX (main.tex, refs.bib)
```

## Entorno

Requiere [uv](https://docs.astral.sh/uv/).

```bash
uv sync                 # crea .venv e instala dependencias
uv run jupyter lab      # abrir notebooks
uv run ruff check .     # lint
```

## Datos

Taiwanese Bankruptcy Prediction Dataset (UCI #572 / Kaggle `fedesoriano/company-bankruptcy-prediction`).
Dejar el CSV en `data/` (ignorado por git). Script de descarga: pendiente.

## Informe

```bash
cd report && latexmk -pdf main.tex
```

## Fechas

- Entrega parcial: 2026-10-23
- Entrega final: 2026-11-20
