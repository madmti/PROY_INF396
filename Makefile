.PHONY: help sync data eda lab lint report clean

REPORT_DIR := report
REPORT := main

help:
	@echo "make sync    - instalar dependencias (uv sync)"
	@echo "make data    - descargar el dataset a data/"
	@echo "make eda     - ejecutar notebooks/00_EDA.ipynb in-place"
	@echo "make lab     - abrir JupyterLab"
	@echo "make lint    - ruff check"
	@echo "make report  - compilar report/main.pdf (pdflatex + bibtex)"
	@echo "make clean   - borrar archivos auxiliares de LaTeX"

sync:
	uv sync

data: sync
	uv run python scripts/download_data.py

eda: data
	uv run jupyter nbconvert --to notebook --execute --inplace notebooks/00_EDA.ipynb

lab: sync
	uv run jupyter lab

lint: sync
	uv run ruff check .

report:
	cd $(REPORT_DIR) && pdflatex -interaction=nonstopmode $(REPORT).tex \
		&& bibtex $(REPORT) \
		&& pdflatex -interaction=nonstopmode $(REPORT).tex \
		&& pdflatex -interaction=nonstopmode $(REPORT).tex

clean:
	cd $(REPORT_DIR) && rm -f $(REPORT).aux $(REPORT).log $(REPORT).out $(REPORT).bbl $(REPORT).blg $(REPORT).toc $(REPORT).fls $(REPORT).fdb_latexmk $(REPORT).synctex.gz
