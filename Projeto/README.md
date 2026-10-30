# 🌾 Projeto AgroData — Inteligência Agrometeorológica Preditiva & Clustering Avançado
**Disciplina:** Ciência de Dados — Aprendizado Supervisionado e Não Supervisionado  
**Professor Responsável:** Dr. Rafael Duarte  
**Equipe:** Grupo 10  
**Status da Entrega:** Checkpoint 1 Consolidado (Aulas 09, 10, 11 e 12 — Valor: 1,25 Pontos)

---

## 📁 Estrutura de Diretórios do Projeto

Todo o projeto foi reorganizado dentro da pasta raiz `Projeto`, estruturado de forma modular e rastreável:

```
Projeto/
│
├── data/                               <- Bases de dados do projeto
│   ├── raw/                            <- Dados brutos originais
│   │   └── dataset_producao_agricola_clima.csv (305 registros brutos)
│   └── processed/                      <- Dados higienizados pós-wrangling
│       └── dataset_agro_tratado.csv    (298 registros válidos com Risco_Quebra_Safra)
│
├── notebooks/                          <- Paradigma 100% guiado via Jupyter Notebook
│   ├── 01_aulas_referencia/            <- Cadernos de aula teórica e laboratórios do professor
│   │   ├── Aula_10_Aprendizado_Preditivo_Regressao.ipynb
│   │   ├── Aula_11_Aprendizado_Nao_Supervisionado_Clustering.ipynb
│   │   └── Aula_12_Aprendizado_Nao_Supervisionado_Avancado.ipynb
│   └── 02_projeto_principal/           <- Cadernos oficiais executáveis da entrega do Grupo 10
│       ├── projeto_agrodata_pipeline_completo.ipynb (Notebook Mestre Integrado com 27 células)
│       └── aula01.ipynb (Espelho sincronizado para compatibilidade)
│
├── docs/                               <- Documentação técnica e executiva
│   ├── especificacao_do_projeto.md     (Especificação técnica, framework CRISP-DM e regras)
│   ├── ficha_gatekeeper_grupo10.md     (Ficha de validação oficial do Gatekeeper)
│   └── especificacao_projeto_agrodata.html (Dashboard executivo interativo em HTML/JS)
│
└── src/                                <- Código modular de suporte e automação de testes
    ├── __init__.py
    ├── config.py                       (Constantes globais, caminhos e hiperparâmetros)
    ├── data_wrangling.py               (Higienização rastreável de dados)
    ├── regression_models.py            (Regressão OLS Simples vs. Múltipla)
    ├── unsupervised_clustering.py      (K-Means, Ward, DBSCAN e PCA)
    ├── gerar_notebook_oficial.py       (Gerador automatizado do caderno Jupyter)
    └── validar_execucao_notebook.py    (Validador de integridade e zero erros de execução)
```

---

## 🎯 Roteiro de Execução do Notebook Principal

O arquivo principal para apresentação e avaliação pelo professor é:  
👉 `Projeto/notebooks/02_projeto_principal/projeto_agrodata_pipeline_completo.ipynb`

### Módulos Contidos no Notebook:
1. **Ficha Oficial do Gatekeeper:** Grupo 10, Integrantes, RGM, Problema de Negócio e Metadados.
2. **Setup do Ambiente:** Importações de NumPy, Pandas, Scikit-Learn e Scipy com suppressão de avisos.
3. **Carga e Dicionário de Variáveis:** Carregamento com busca dinâmica de caminhos relativos.
4. **Data Wrangling (Aula 09):** Deduplicação (5 duplicatas removidas), sanitização de strings, conversão de chuva negativa para `NaN` e expurgo de outliers de digitação ($>10.000\text{ kg/ha}$).
5. **Demonstração do Sequestro da Reta:** Comparativo visual do impacto devastador de outliers em modelos OLS.
6. **Preparação Preditiva (Aula 10):** `get_dummies(drop_first=True)` contra a armadilha das dummies e `train_test_split` antes da imputação pela mediana de treino (Zero Data Leakage).
7. **Regressão Simples vs. Múltipla:** Redução de $34,0\%$ no MAE ($319,91\text{ kg/ha}$ ou $5,33\text{ sc/ha}$) e salto de $R^2$ de $34,8\%$ para $67,8\%$.
8. **Clustering K-Means (Aula 11):** `StandardScaler` (Z-Score), Método do Cotovelo e Silhueta definindo $K=3$.
9. **Clusterização Hierárquica de Ward (Aula 12):** Dendrograma completo com linha de corte em $18,0$ confirmando a genealogia dos 3 grupos.
10. **DBSCAN e Caça a Anomalias (Aula 12):** Detecção de 24 talhões anômalos ($8,1\%$) marcados como Ruído (`-1`) devido a estresse hídrico extremo ou discrepâncias bioclimáticas.
11. **Redução 2D com PCA (Aula 12):** Compressão em $PC_1$ (Vigor Hídrico / Produtividade - $30,0\%$) e $PC_2$ (Estresse Térmico / Insolação - $17,8\%$), retendo $47,9\%$ da variância original e plotando os mapas comparativos.
12. **Síntese Executiva do Checkpoint 1 (1,25 pts):** Tabela de Personas Agroecológicas (`[REGULAR]`, `[ALERTA]` e `[OURO]`) com planos de manejo agronômico.
13. **Preparação para o Checkpoint 2 (Aula 13/14):** Engenharia de `Risco_Quebra_Safra` pronta para classificação supervisionada.
