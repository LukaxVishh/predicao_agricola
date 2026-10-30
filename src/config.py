"""
Projeto AgroData - Inteligência Agrometeorológica Preditiva
Módulo de Configuração e Constantes Globais
"""
import os
from pathlib import Path

# Raiz do projeto
ROOT_DIR = Path(__file__).resolve().parent.parent

# Diretórios principais
DATA_DIR = ROOT_DIR / "data"
RAW_DATA_PATH = DATA_DIR / "raw" / "dataset_producao_agricola_clima.csv"
PROCESSED_DATA_PATH = DATA_DIR / "processed" / "dataset_agro_tratado.csv"

NOTEBOOKS_DIR = ROOT_DIR / "notebooks"
DOCS_DIR = ROOT_DIR / "docs"

# Sementes e hiperparâmetros
RANDOM_STATE = 42
TEST_SIZE = 0.20

# Features analíticas contínuas para modelos de agrupamento e PCA
FEATURES_CLUSTERING = [
    "Precipitacao_Acumulada_mm",
    "Temperatura_Media_C",
    "Umidade_Relativa_Pct",
    "Insolacao_Horas_Sol",
    "Fertilizante_kg_ha",
    "Produtividade_kg_ha"
]

# Variável contínua alvo para regressão
TARGET_REGRESSION = "Produtividade_kg_ha"

# Variável categórica alvo para classificação futura (Checkpoint 2)
TARGET_CLASSIFICATION = "Risco_Quebra_Safra"
LIMIAR_QUEBRA_SAFRA_KG_HA = 2600.0  # Limite crítico de quebra (< 43.3 sacas/ha)
