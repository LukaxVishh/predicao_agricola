# Projeto AgroData

## Sistema Preditivo Agrometeorológico e Zonificação Agroecológica

Projeto integrador da disciplina **Ciência de Dados — Aprendizado Supervisionado e Não Supervisionado**, ministrada pelo professor **Dr. Rafael Duarte**. A entrega documentada corresponde ao **Checkpoint 1 consolidado** (Aulas 09 a 12, valor: 1,25 pontos).

### Equipe — Grupo 10

- Carlos Eduardo Sielski Urbim — RGM 33755973
- Fernando de Araujo Pereira — RGM 34210245
- Lucas Antonio Domingues de Souza Oliveira — RGM 33476055
- Eduardo Bryan Braga Rocha — RGM 34731067
- Otavio Caetano Ribeiro — RGM 32736274

## Sobre o projeto

O AgroData estuda como prever a produtividade de grãos, em kg/ha e sacas/ha, a partir de variáveis climáticas e características do solo. Também agrupa talhões por similaridade agroecológica para apoiar decisões de logística de fretes e silos, precificação de seguro rural e mitigação de riscos associados à seca.

A análise usa uma base pública indicada como Kaggle/Gov (INMET/BDMEP e PAM/IBGE). O notebook realiza exploração e tratamento dos dados, compara modelos de regressão simples e múltipla e aplica K-Means, agrupamento hierárquico, DBSCAN e PCA. A variável `Risco_Quebra_Safra` prepara a base para uma etapa futura de classificação: valor 1 para produtividade abaixo de 2.600 kg/ha e 0 caso contrário.

## Arquivos principais

- [Notebook principal](notebooks/Projeto-Agrodata.ipynb)
- [Dados brutos](data/raw/dataset_producao_agricola_clima.csv)
- [Dados tratados](data/processed/dataset_agro_tratado.csv)
- [Documentação](docs/)
- [Código-fonte](src/)
- Dependências: `requirements.txt`
