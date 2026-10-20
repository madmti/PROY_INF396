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

Requiere [uv](https://docs.astral.sh/uv/) y `make`. El informe requiere `pdflatex` y `bibtex`.

```bash
make sync     # crea .venv e instala dependencias
make lab      # abrir JupyterLab
make lint     # ruff check
```

## Datos

Taiwanese Bankruptcy Prediction Dataset (UCI #572 / Kaggle `fedesoriano/company-bankruptcy-prediction`).

```bash
make data     # guarda data/taiwanese_bankruptcy.csv (ignorado por git)
make eda      # ejecuta notebooks/00_EDA.ipynb
make baselines # ejecuta notebooks/01_baselines.ipynb
```

## Informe

```bash
make report   # genera report/main.pdf
make clean    # borra archivos auxiliares de LaTeX
```

`make help` lista todos los objetivos.
