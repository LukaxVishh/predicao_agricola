"""
Módulo de Data Wrangling e Pré-processamento Rastreável (Aula 09 / CRISP-DM)
"""
import numpy as np
import pandas as pd
from pathlib import Path
from .config import RAW_DATA_PATH, PROCESSED_DATA_PATH, LIMIAR_QUEBRA_SAFRA_KG_HA

def carregar_dados_brutos(caminho_csv: Path = RAW_DATA_PATH) -> pd.DataFrame:
    """Carrega o dataset bruto de produção agrícola e clima."""
    if not caminho_csv.exists():
        raise FileNotFoundError(f"Arquivo não encontrado no caminho especificado: {caminho_csv}")
    return pd.read_csv(caminho_csv)

def executar_data_wrangling(df_bruto: pd.DataFrame, salvar_csv: bool = True) -> pd.DataFrame:
    """
    Aplica a higienização rastreável de dados:
    1. Deduplicação de linhas repetidas decorrentes de exportação.
    2. Padronização e sanitização de strings categóricas.
    3. Conversão de valores impossíveis no domínio físico para NaN.
    4. Expurgo de outliers extremos na variável alvo.
    5. Engenharia da variável binária de risco de quebra de safra para classificação futura.
    """
    df = df_bruto.copy()
    
    # 1. Deduplicação
    df = df.drop_duplicates().reset_index(drop=True)
    
    # 2. Padronização textual de colunas de texto
    if "Sistema_Irrigacao" in df.columns:
        df["Sistema_Irrigacao"] = df["Sistema_Irrigacao"].astype(str).str.strip().str.title()
        
    if "Cultura" in df.columns:
        df["Cultura"] = df["Cultura"].astype(str).str.strip().str.title()
        
    if "Regiao" in df.columns:
        df["Regiao"] = df["Regiao"].astype(str).str.strip().str.title()
        
    if "Tipo_Solo" in df.columns:
        df["Tipo_Solo"] = df["Tipo_Solo"].astype(str).str.strip().str.title()

    # 3. Tratamento de limites físicos (Pluviometria negativa é fisicamente impossível)
    if "Precipitacao_Acumulada_mm" in df.columns:
        df.loc[df["Precipitacao_Acumulada_mm"] < 0, "Precipitacao_Acumulada_mm"] = np.nan

    # 4. Expurgo de erro de digitação/outlier extremo de produtividade (> 10.000 kg/ha)
    if "Produtividade_kg_ha" in df.columns:
        df = df[df["Produtividade_kg_ha"] < 10000.0].copy()

    # 5. Engenharia de features para o Checkpoint 2 (Risco_Quebra_Safra)
    df["Risco_Quebra_Safra"] = (df["Produtividade_kg_ha"] < LIMIAR_QUEBRA_SAFRA_KG_HA).astype(int)
    
    # 6. Conversão de rendimento físico para sacas de 60 kg por hectare
    df["Produtividade_Sacas_ha"] = (df["Produtividade_kg_ha"] / 60.0).round(2)
    
    if salvar_csv:
        PROCESSED_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(PROCESSED_DATA_PATH, index=False)
        
    return df

if __name__ == "__main__":
    df_raw = carregar_dados_brutos()
    df_proc = executar_data_wrangling(df_raw)
    print(f"[OK] Data Wrangling concluído: {len(df_raw)} linhas brutas -> {len(df_proc)} linhas válidas tratadas.")
