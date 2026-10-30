# 📋 FICHA DE VALIDAÇÃO OFICIAL DO GATEKEEPER (ENTREGA 0 — AULA 11)
**Disciplina:** Ciência de Dados — Aprendizado Supervisionado e Não Supervisionado  
**Professor Responsável:** Dr. Rafael Duarte  

---

### 1. Nome ou Número do Grupo
**Grupo 10** — AgroData (Inteligência Agrometeorológica Preditiva)

---

### 2. Integrantes e RGM
1. **Carlos Eduardo Sielski Urbim** — RGM: 33755973
2. **Fernando de Araujo Pereira** — RGM: 34210245
3. **Lucas Antonio Domingues de Souza Oliveira** — RGM: 33476055
4. **Eduardo Bryan Braga Rocha** — RGM: 34731067
5. **Otavio Caetano Ribeiro** — RGM: 32736274

---

### 3. Problema de Negócio
Predição antecipada da produtividade agrícola de grãos ($kg/ha$ e sacas/ha) a partir de variáveis bioclimáticas e edafológicas, e zonificação agroecológica não supervisionada de talhões para apoio à contratação logística de fretes e silos, precificação de seguro rural e mitigação de risco de seca.

---

### 4. Fonte do Dataset
**Base Agrometeorológica Pública Consolidada (INMET / BDMEP e PAM / IBGE)** — Multiplicador $M_{real} = \mathbf{1,0\times}$.

---

### 5. Arquivo Dataset Carregado
`dataset_producao_agricola_clima.csv`

---

### 6. Variável Alvo Contínua para Regressão (Aprendizado Supervisionado)
`Produtividade_kg_ha` (Rendimento físico colhido ao final do ciclo fenológico).

---

### 7. Variáveis Numéricas para Clustering (Aprendizado Não Supervisionado)
* `Precipitacao_Acumulada_mm` (Volume de chuva acumulado no ciclo);
* `Temperatura_Media_C` (Temperatura média diária do ar);
* `Umidade_Relativa_Pct` (Umidade relativa média do ar);
* `Insolacao_Horas_Sol` (Horas totais de luz solar direta);
* `Fertilizante_kg_ha` (Volume de adubação NPK aplicada);
* `Produtividade_kg_ha` (Produtividade colhida).

---

### 8. Variável Alvo Categórica para Classificação Futura (Checkpoint 2)
`Risco_Quebra_Safra` (Classificação binária: $1$ = Risco Severo de Quebra de Safra / Perda Crítica $< 2.600\text{ kg/ha}$; $0$ = Produtividade Normal ou Alta).

---

## 💻 Versão Executável em Python (Para Célula do Notebook)

```python
# ==============================================================================
# FICHA DE VALIDAÇÃO OFICIAL DO GATEKEEPER — GRUPO 10
# ==============================================================================
ficha_gatekeeper = {
    "Grupo_Nome_ou_Numero": "Grupo 10 — AgroData (Inteligência Agrometeorológica Preditiva)",
    "Integrantes_e_RGM": [
        "1. Carlos Eduardo Sielski Urbim - RGM: 33755973",
        "2. Fernando de Araujo Pereira - RGM: 34210245",
        "3. Lucas Antonio Domingues de Souza Oliveira - RGM: 33476055",
        "4. Eduardo Bryan Braga Rocha - RGM: 34731067",
        "5. Otavio Caetano Ribeiro - RGM: 32736274"
    ],
    "Problema_de_Negocio": "Predição antecipada da produtividade de grãos (kg/ha e sacas/ha) a partir de variáveis bioclimáticas e edafológicas, e zonificação agroecológica não supervisionada de talhões para apoio à contratação logística de fretes/silos, precificação de seguro rural e mitigação de risco de seca.",
    "Fonte_Dataset": "Base Agrometeorológica Pública Consolidada (INMET / BDMEP e PAM / IBGE) - Multiplicador 1.0x",
    "Arquivo_Dataset_Carregado": "dataset_producao_agricola_clima.csv",
    "Variavel_Alvo_Continua_p_Regressao": "Produtividade_kg_ha",
    "Variaveis_Numericas_p_Clustering": [
        "Precipitacao_Acumulada_mm", 
        "Temperatura_Media_C", 
        "Umidade_Relativa_Pct", 
        "Insolacao_Horas_Sol", 
        "Fertilizante_kg_ha", 
        "Produtividade_kg_ha"
    ],
    "Variavel_Alvo_Categorica_p_Classificacao_Futura": "Risco_Quebra_Safra (1 = Quebra Severa / Perda Crítica; 0 = Produtividade Normal/Alta)"
}

# Exibição estruturada na tela
print("======================================================================")
print("FICHA DE VALIDAÇÃO DO GATEKEEPER REGISTRADA — GRUPO 10")
print("======================================================================")
for chave, valor in ficha_gatekeeper.items():
    if isinstance(valor, list):
        print(f"\n{chave}:")
        for item in valor:
            print(f"  • {item}")
    else:
        print(f"{chave}: {valor}")
print("======================================================================")
```
