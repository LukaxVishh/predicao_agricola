"""
Módulo de Aprendizado Não Supervisionado Avançado (Aulas 11 e 12)
Implementa:
1. Padronização Z-Score com StandardScaler
2. K-Means (Método do Cotovelo e Coeficiente de Silhueta)
3. Clusterização Hierárquica Aglomerativa (Método de Ward)
4. Agrupamento Espacial Baseado em Densidade com Detecção de Anomalias (DBSCAN)
5. Redução de Dimensionalidade e Mapeamento 2D com PCA
"""
import numpy as np
import pandas as pd
from typing import Dict, Any, List, Tuple
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
from scipy.cluster.hierarchy import linkage
from .config import RANDOM_STATE, FEATURES_CLUSTERING

def padronizar_features_clustering(df: pd.DataFrame, features: List[str] = FEATURES_CLUSTERING) -> Tuple[np.ndarray, StandardScaler, pd.DataFrame]:
    """
    Trata eventuais valores ausentes residuais com a mediana e padroniza os dados com StandardScaler (Z-Score):
    z = (x - mu) / sigma
    """
    df_feat = df[features].copy()
    for col in features:
        df_feat[col] = df_feat[col].fillna(df_feat[col].median())
        
    scaler = StandardScaler()
    Z = scaler.fit_transform(df_feat)
    return Z, scaler, df_feat

def avaliar_k_otimo_kmeans(Z: np.ndarray, k_min: int = 2, k_max: int = 7) -> pd.DataFrame:
    """
    Calcula WCSS (Inércia / Cotovelo) e Coeficiente de Silhueta para K de k_min até k_max.
    """
    resultados = []
    for k in range(k_min, k_max + 1):
        km = KMeans(n_clusters=k, random_state=RANDOM_STATE, n_init=10)
        labels = km.fit_predict(Z)
        wcss = km.inertia_
        sil = silhouette_score(Z, labels)
        resultados.append({"K": k, "WCSS": wcss, "Silhueta": sil})
    return pd.DataFrame(resultados)

def executar_kmeans(Z: np.ndarray, n_clusters: int = 3) -> Tuple[KMeans, np.ndarray]:
    """Treina o modelo K-Means com o número ótimo de clusters."""
    km = KMeans(n_clusters=n_clusters, random_state=RANDOM_STATE, n_init=10)
    labels = km.fit_predict(Z)
    return km, labels

def executar_hierarquico_ward(Z: np.ndarray, n_clusters: int = 3) -> Tuple[np.ndarray, AgglomerativeClustering, np.ndarray]:
    """
    Executa a clusterização hierárquica aglomerativa pelo Método de Ward:
    Retorna a matriz de ligação (linkage) e o modelo ajustado.
    """
    matriz_ward = linkage(Z, method="ward")
    hc = AgglomerativeClustering(n_clusters=n_clusters, linkage="ward")
    labels = hc.fit_predict(Z)
    return matriz_ward, hc, labels

def executar_dbscan(Z: np.ndarray, eps: float = 1.60, min_samples: int = 5) -> Tuple[DBSCAN, np.ndarray]:
    """
    Executa o algoritmo DBSCAN nos dados padronizados:
    Pontos com densidade insuficiente no raio eps são rotulados como Ruído/Anomalias (-1).
    """
    db = DBSCAN(eps=eps, min_samples=min_samples)
    labels = db.fit_predict(Z)
    return db, labels

def executar_pca_2d(Z: np.ndarray, features: List[str] = FEATURES_CLUSTERING) -> Tuple[PCA, np.ndarray, pd.DataFrame]:
    """
    Comprime o espaço multidimensional em 2 Componentes Principais (PC1 e PC2):
    Calcula a variância explicada (autovalores) e cargas fatoriais (autovetores).
    """
    pca = PCA(n_components=2, random_state=RANDOM_STATE)
    coords_pca = pca.fit_transform(Z)
    
    df_loadings = pd.DataFrame(
        pca.components_.T,
        index=features,
        columns=["Peso_PC1 (v1)", "Peso_PC2 (v2)"]
    ).round(3)
    
    return pca, coords_pca, df_loadings

def gerar_tabela_personas(df: pd.DataFrame, cluster_col: str = "Cluster_KMeans") -> pd.DataFrame:
    """
    Gera a tabela executiva consolidando médias das variáveis e batizando as Personas Agronômicas.
    """
    tabela = df.groupby(cluster_col).agg(
        Qtd_Talhoes=("ID_Talhao", "count") if "ID_Talhao" in df.columns else (cluster_col, "count"),
        Chuva_Media_mm=("Precipitacao_Acumulada_mm", "mean"),
        Temp_Media_C=("Temperatura_Media_C", "mean"),
        Umidade_Media_Pct=("Umidade_Relativa_Pct", "mean"),
        Fertilizante_Medio_kg_ha=("Fertilizante_kg_ha", "mean"),
        Produtividade_Media_kg_ha=("Produtividade_kg_ha", "mean"),
        Produtividade_Media_Sacas_ha=("Produtividade_Sacas_ha", "mean") if "Produtividade_Sacas_ha" in df.columns else ("Produtividade_kg_ha", lambda x: (x/60).mean())
    ).round(2)
    
    # Mapeamento semântico das Personas
    nome_personas = {
        0: "[REGULAR] Rendimento Médio e Manejo Estável",
        1: "[ALERTA] Déficit Hídrico, Estresse Térmico e Risco de Quebra",
        2: "[OURO] Alta Produtividade e Pluviometria Ideal"
    }
    tabela["Persona_Agroecologica"] = tabela.index.map(lambda c: nome_personas.get(c, f"Cluster {c}"))
    return tabela
