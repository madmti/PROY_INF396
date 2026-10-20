"""Protocolo de validacion y metricas."""

import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import StratifiedKFold, cross_val_predict
from sklearn.pipeline import Pipeline

from inf396.preprocessing import preprocessing_steps


def error_rates(y_true, y_pred) -> dict[str, float]:
    """Accuracy balanceado y errores Tipo I / Tipo II (clase positiva = quiebra).

    Tipo I: quiebras clasificadas como sanas. Tipo II: sanas clasificadas como quiebra.
    """
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
    type1 = fn / (fn + tp)
    type2 = fp / (fp + tn)
    return {"bal_acc": 1 - (type1 + type2) / 2, "type1": type1, "type2": type2}


def balanced_subsample(X: pd.DataFrame, y: pd.Series, rep: int) -> tuple[pd.DataFrame, pd.Series]:
    """Todas las quiebras mas igual numero de sanas elegidas al azar (semilla = rep)."""
    rng = np.random.default_rng(rep)
    bankrupt = y.index[y == 1]
    healthy = rng.choice(y.index[y == 0], size=len(bankrupt), replace=False)
    idx = np.concatenate([bankrupt, healthy])
    return X.loc[idx], y.loc[idx]


def repeated_balanced_cv(
    models: dict[str, BaseEstimator],
    X: pd.DataFrame,
    y: pd.Series,
    n_reps: int = 5,
    n_splits: int = 10,
    steps: list | None = None,
    n_jobs: int = -1,
) -> pd.DataFrame:
    """Submuestreo balanceado + CV estratificada, repetido `n_reps` veces.

    `steps` son los pasos de preprocesamiento previos al modelo (por defecto
    winsorizar + estandarizar); se ajustan solo con el pliegue de entrenamiento.
    Devuelve un DataFrame con una fila por (modelo, repeticion).
    """
    prefix = steps if steps is not None else preprocessing_steps()
    rows = []
    for rep in range(n_reps):
        print(f"  -> Ejecutando repetición {rep + 1}/{n_reps}...", flush=True)
        Xb, yb = balanced_subsample(X, y, rep)
        cv = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=rep)
        for name, model in models.items():
            pipe = Pipeline([*prefix, ("model", model)])
            pred = cross_val_predict(pipe, Xb, yb, cv=cv, n_jobs=n_jobs)
            rows.append({"model": name, "rep": rep, **error_rates(yb, pred)})
    return pd.DataFrame(rows)

