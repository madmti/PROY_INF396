"""Definicion de modelos (baseline SVM y candidatos)."""

from sklearn.base import BaseEstimator
from sklearn.linear_model import LogisticRegressionCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

BASELINE = "SVM lineal"


def candidate_models() -> dict[str, BaseEstimator]:
    """Baseline (SVM lineal, como en el paper) y modelos candidatos."""
    return {
        BASELINE: SVC(kernel="linear"),
        "LogReg L2": LogisticRegressionCV(penalty="l2", Cs=5, max_iter=500),
        "LogReg L1": LogisticRegressionCV(penalty="l1", solver="liblinear", Cs=5),
        "KNN (K=7)": KNeighborsClassifier(n_neighbors=7),
    }
