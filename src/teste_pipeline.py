import sys
from pathlib import Path

# Adiciona o diretório Projeto ao sys.path
sys.path.insert(0, r"C:\Users\kinha\predicao_agricola\Projeto")

from src.data_wrangling import carregar_dados_brutos, executar_data_wrangling
from src.regression_models import preparar_dados_regressao, treinar_e_avaliar_regressoes
from src.unsupervised_clustering import (
    padronizar_features_clustering,
    avaliar_k_otimo_kmeans,
    executar_kmeans,
    executar_hierarquico_ward,
    executar_dbscan,
    executar_pca_2d,
    gerar_tabela_personas
)

print("--- ETAPA 1: DATA WRANGLING ---")
df_raw = carregar_dados_brutos()
df_proc = executar_data_wrangling(df_raw, salvar_csv=True)
print(f"[OK] {len(df_raw)} linhas brutas -> {len(df_proc)} linhas válidas tratadas.")

print("\n--- ETAPA 2: REGRESSAO LINEAR ---")
X_train, X_test, y_train, y_test, med = preparar_dados_regressao(df_proc)
res_reg = treinar_e_avaliar_regressoes(X_train, X_test, y_train, y_test)
print(f"R2 Simples: {res_reg['metricas_simples']['R2']:.3f} | MAE: {res_reg['metricas_simples']['MAE']:.2f}")
print(f"R2 Multiplo: {res_reg['metricas_multiplo']['R2']:.3f} | MAE: {res_reg['metricas_multiplo']['MAE']:.2f}")

print("\n--- ETAPA 3: CLUSTERING AVANÇADO (AULAS 11 E 12) ---")
Z, scaler, df_feat = padronizar_features_clustering(df_proc)
km, km_labels = executar_kmeans(Z, n_clusters=3)
matriz_w, hc, hc_labels = executar_hierarquico_ward(Z, n_clusters=3)
db, db_labels = executar_dbscan(Z, eps=1.60, min_samples=5)
pca, coords_2d, loadings = executar_pca_2d(Z)

df_proc["Cluster_KMeans"] = km_labels
df_proc["Cluster_Hierarquico"] = hc_labels
df_proc["Cluster_DBSCAN"] = db_labels
df_proc["PC1"] = coords_2d[:, 0]
df_proc["PC2"] = coords_2d[:, 1]

tabela = gerar_tabela_personas(df_proc)
print("\nTabela de Personas Agroecológicas:")
print(tabela[["Qtd_Talhoes", "Chuva_Media_mm", "Temp_Media_C", "Produtividade_Media_Sacas_ha", "Persona_Agroecologica"]])

n_ruido = int((db_labels == -1).sum())
print(f"\nDBSCAN: {n_ruido} talhoes anomalos isolados como ruido (-1).")
var_tot = float(pca.explained_variance_ratio_.sum() * 100)
print(f"PCA 2D: Variancia total retida = {var_tot:.1f}%")
print("\n[SUCESSO] Pipeline modular testado com 100% de exito!")
