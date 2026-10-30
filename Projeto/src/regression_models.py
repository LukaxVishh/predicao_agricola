"""
Módulo de Modelagem Preditiva Supervisionada — Regressão OLS (Aula 10)
Implementação livre de Data Leakage e Colinearidade Perfeita (Dummy Variable Trap).
"""
import numpy as np
import pandas as pd
from typing import Dict, Any, Tuple
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from .config import RANDOM_STATE, TEST_SIZE, TARGET_REGRESSION

def preparar_dados_regressao(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series, pd.Series]:
    """
    Realiza o pré-processamento estrito para modelagem de regressão:
    1. One-Hot Encoding com drop_first=True nas variáveis categóricas explicativas.
    2. Divisão Treino e Teste ANTES da imputação de valores ausentes (elimina Data Leakage).
    3. Imputação pela mediana aprendida unicamente no conjunto de Treino.
    """
    colunas_categoricas = ["Regiao", "Tipo_Solo", "Sistema_Irrigacao"]
    colunas_existentes = [c for c in colunas_categoricas if c in df.columns]
    
    # One-Hot Encoding com drop_first=True para evitar a armadilha das dummies
    df_encoded = pd.get_dummies(df, columns=colunas_existentes, drop_first=True, dtype=int)
    
    # Remoção de identificadores e variáveis alvo derivadas
    cols_ignorar = ["ID_Talhao", "Cultura", TARGET_REGRESSION, "Risco_Quebra_Safra", "Produtividade_Sacas_ha"]
    features_x = [c for c in df_encoded.columns if c not in cols_ignorar]
    
    X = df_encoded[features_x]
    y = df_encoded[TARGET_REGRESSION]
    
    # Separação Treino e Teste com semente reprodutível
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE
    )
    
    # Imputação estrita pela mediana do Treino
    medianas_treino = X_train.median(numeric_only=True)
    X_train_imputed = X_train.fillna(medianas_treino)
    X_test_imputed = X_test.fillna(medianas_treino)
    
    return X_train_imputed, X_test_imputed, y_train, y_test, medianas_treino

def treinar_e_avaliar_regressoes(
    X_train: pd.DataFrame, X_test: pd.DataFrame, y_train: pd.Series, y_test: pd.Series
) -> Dict[str, Any]:
    """
    Treina e avalia:
    - Modelo Baseline: Regressão Linear Simples (apenas Precipitacao_Acumulada_mm).
    - Modelo Integrado: Regressão Linear Múltipla (todas as covariáveis).
    """
    # 1. Regressão Linear Simples
    feature_simples = ["Precipitacao_Acumulada_mm"]
    modelo_simples = LinearRegression()
    modelo_simples.fit(X_train[feature_simples], y_train)
    y_pred_simples = modelo_simples.predict(X_test[feature_simples])
    
    mae_simples = mean_absolute_error(y_test, y_pred_simples)
    rmse_simples = np.sqrt(mean_squared_error(y_test, y_pred_simples))
    r2_simples = r2_score(y_test, y_pred_simples)
    
    # 2. Regressão Linear Múltipla
    modelo_multiplo = LinearRegression()
    modelo_multiplo.fit(X_train, y_train)
    y_pred_multiplo = modelo_multiplo.predict(X_test)
    
    mae_multiplo = mean_absolute_error(y_test, y_pred_multiplo)
    rmse_multiplo = np.sqrt(mean_squared_error(y_test, y_pred_multiplo))
    r2_multiplo = r2_score(y_test, y_pred_multiplo)
    
    # Tabela de coeficientes do modelo múltiplo
    tabela_betas = pd.DataFrame({
        "Feature": ["Intercepto (Beta_0)"] + list(X_train.columns),
        "Coeficiente_Beta": [modelo_multiplo.intercept_] + list(modelo_multiplo.coef_)
    })
    
    return {
        "modelo_simples": modelo_simples,
        "modelo_multiplo": modelo_multiplo,
        "metricas_simples": {"MAE": mae_simples, "RMSE": rmse_simples, "R2": r2_simples},
        "metricas_multiplo": {"MAE": mae_multiplo, "RMSE": rmse_multiplo, "R2": r2_multiplo},
        "tabela_betas": tabela_betas,
        "y_pred_simples": y_pred_simples,
        "y_pred_multiplo": y_pred_multiplo
    }
