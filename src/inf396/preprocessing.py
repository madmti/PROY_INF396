"""Limpieza y transformaciones de las razones financieras."""

import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


class Winsorizer(BaseEstimator, TransformerMixin):
    """Recorta cada variable entre los percentiles p y 100-p del entrenamiento."""

    def __init__(self, p: float = 1):
        self.p = p

    def fit(self, X, y=None):
        self.low_ = np.percentile(X, self.p, axis=0)
        self.high_ = np.percentile(X, 100 - self.p, axis=0)
        return self

    def transform(self, X):
        return np.clip(X, self.low_, self.high_)


def drop_constant_columns(X: pd.DataFrame) -> pd.DataFrame:
    """Elimina las columnas con un unico valor."""
    return X.loc[:, X.nunique() > 1]


def preprocessing_steps(p: float = 1) -> list:
    """Pasos (winsorizar, estandarizar) para anteponer a un modelo en un Pipeline."""
    return [("winsorize", Winsorizer(p)), ("scale", StandardScaler())]


def make_preprocessor(p: float = 1) -> Pipeline:
    """Pipeline de preprocesamiento: winsorizar y estandarizar."""
    return Pipeline(preprocessing_steps(p))
