"""
Pacote AgroData - Pipeline de Ciência de Dados para Produtividade Agrícola e Zonificação Agroecológica.
"""
from .config import (
    ROOT_DIR,
    RAW_DATA_PATH,
    PROCESSED_DATA_PATH,
    RANDOM_STATE,
    FEATURES_CLUSTERING,
    TARGET_REGRESSION,
    TARGET_CLASSIFICATION
)

__all__ = [
    "ROOT_DIR",
    "RAW_DATA_PATH",
    "PROCESSED_DATA_PATH",
    "RANDOM_STATE",
    "FEATURES_CLUSTERING",
    "TARGET_REGRESSION",
    "TARGET_CLASSIFICATION"
]
