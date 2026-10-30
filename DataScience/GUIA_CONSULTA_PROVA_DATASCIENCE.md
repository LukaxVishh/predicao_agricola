# 📘 GUIA DEFINITIVO DE CONSULTA E SOBREVIVÊNCIA: CIÊNCIA DE DADOS
**Curso:** Engenharia de Software  
**Disciplina:** Ciência de Dados | **Docente:** Prof. Rafael Duarte  
**Propósito:** Manual de Consulta Rápida, Interpretação de Cenários e Cola de Código Python para Avaliações  

---

## SUMÁRIO GERAL DE CONSULTA RÁPIDA

1. [MÓDULO 1: Governança de Dados, Segurança e LGPD](#módulo-1-governança-de-dados-segurança-e-lgpd)
2. [MÓDULO 2: Estatística Descritiva 1 - Posição, Dispersão e Caos](#módulo-2-estatística-descritiva-1---posição-dispersão-e-caos)
3. [MÓDULO 3: Estatística Descritiva 2 - Quartis, Cercas Matemáticas e Raio-X Visual](#módulo-3-estatística-descritiva-2---quartis-cercas-matemáticas-e-raio-x-visual)
4. [MÓDULO 4: Inferência Estatística e Testes A/B (SciPy)](#módulo-4-inferência-estatística-e-testes-ab-scipy)
5. [MÓDULO 5: Correlação, Covariância e Causalidade](#módulo-5-correlação-covariância-e-causalidade)
6. [MÓDULO 6: Machine Learning Preditivo - Regressão Linear Simples (Scikit-Learn)](#módulo-6-machine-learning-preditivo---regressão-linear-simples-scikit-learn)
7. [MÓDULO 7: Gabarito Completo do Simulado Integrador (Caso TechMarket)](#módulo-7-gabarito-completo-do-simulado-integrador-caso-techmarket)
8. [MÓDULO 8: Arsenal de Código - Problemático vs. Corrigido & Trap Guide](#módulo-8-arsenal-de-código---problemático-vs-corrigido--trap-guide)

---

# MÓDULO 1: Governança de Dados, Segurança e LGPD

### 1.1. O Paradigma do Dado: Ativo vs. Passivo
- **Ativo de Negócio:** Dados geram inteligência competitiva, otimização de conversão e personalização de serviços.
- **Passivo de Risco:** Armazenar dados atrai custos de custódia, risco de sequestro/vazamento e responsabilidade civil/administrativa severa.
- **Regra de Ouro da Arquitetura:** Se uma coluna não possui justificativa operacional estrita ou finalidade analítica comprovada, ela **não deve ser coletada nem persistida**.

### 1.2. A Tríade CIA (Pilares Fundamentais de Segurança)
1. **Confidencialidade:** O dado só pode ser lido e acessado por identidades autorizadas sob rigoroso controle de acesso (Criptografia em repouso/trânsito e gestão de identidade IAM).
2. **Integridade:** Garantia de que a informação permanece exata, inalterada e protegida contra manipulação indevida ou corrupção acidental (Hashes criptográficos como SHA-256, checksums e logs de auditoria append-only).
3. **Disponibilidade:** Acesso garantido e ininterrupto ao dado no momento em que os processos legítimos de negócio demandarem (SLA, replicação geográfica, backups e tolerância a falhas).

### 1.3. O Panorama Regulatório: LGPD vs. GDPR vs. CCPA
- **LGPD (Brasil - Lei 13.709/2018):** Multas de até 2% do faturamento da empresa no Brasil, limitadas a **R$ 50 milhões por infração**. O titular do dado é o proprietário legítimo de sua identidade.
- **GDPR (União Europeia):** O modelo mais rigoroso globalmente. Penalidades de até **€ 20 milhões ou 4% do faturamento global anual da holding** (o que for maior).
- **CCPA (Califórnia/EUA):** Foco enfático nos direitos de transparência e na proibição explícita de revenda de dados sem consentimento (*"Do Not Sell My Personal Information"*).

### 1.4. Os Três Princípios Mandatórios da LGPD
1. **Finalidade:** O propósito da coleta deve ser explícito, legítimo, informado previamente e jamais genérico (Ex: Coletar CPF sob pretexto de "desconto", mas revender hábitos de consumo a seguradoras é **Desvio de Finalidade**).
2. **Adequação:** O tratamento realizado deve ser estritamente compatível e proporcional com o objetivo informado ao titular.
3. **Minimização (*Need-to-Know*):** Coletar somente o estritamente necessário para atingir o objetivo.
   - *Exemplo Prático:* Para verificar se um cliente pode comprar bebidas alcoólicas, armazene um booleano `maior_de_idade = True`, em vez de coletar e armazenar sua Data de Nascimento completa.

### 1.5. Tipologia de Dados: Pessoal vs. Sensível
| Tipo de Dado | Definição | Exemplos de Atributos | Rigor de Tratamento |
| :--- | :--- | :--- | :--- |
| **Dado Pessoal (PII)** | Qualquer dado que identifique ou possa identificar uma pessoa de forma direta ou indireta. | Nome, CPF, RG, E-mail, Telefone, Endereço IP, Placa de Veículo, Geolocalização precisa. | Exige consentimento explícito ou base legal justificada; sujeito à anonimização. |
| **Dado Sensível** | Informações que carregam inerente potencial de **discriminação social, exclusão ou preconceito financeiro/moral**. | Origem racial/étnica, convicção religiosa, opinião política, filiação sindical, dados genéticos/biométricos, histórico médico/saúde, orientação sexual. | **Rigor Máximo**. Proibido o uso em decisões algorítmicas opacas, precificações abusivas ou compartilhamento não autorizado. |

### 1.6. Anti-Patterns Clássicos de Arquitetura de Software
1. **Data Leakage em Logs:** Aplicações configuradas em modo de depuração gravando o payload completo de requisições HTTP (com senhas e números de cartão) nos arquivos de log `.txt` do servidor.
2. **Bases de Produção em Homologação:** Fazer dump de dados reais de clientes de produção para o ambiente de testes (Staging) ou notebooks locais de desenvolvedores sem anonimização prévia.
3. **A Síndrome do "Exportar para Excel":** Sistemas que expõem um botão irrestrito de "Baixar CSV", desprovido de paginação, limite de registros ou log de auditoria rastreando quem extraiu o arquivo.
4. **Violação do Menor Privilégio (IAM):** Desenvolvedores ou rotinas de serviço com credenciais administrativas completas (`SELECT *` irrestrito) diretamente na base transacional de produção.
5. **O Sistema "Hotel California" (Dark Patterns no Opt-Out):** Facilitar o cadastro em um clique (OAuth com Google/Facebook), mas exigir ligações telefônicas ou procedimentos complexos para cancelamento ou exclusão de conta. A revogação do consentimento deve ser tão fácil quanto sua concessão.

### 1.7. Resolução de Cenários Clássicos de Prova (Casos de Estudo do Professor)

#### Cenário A: A HealthTech e a Seguradora (Parceria B2B)
- **Problema:** Um app de monitoramento por smartwatch quer transferir dados para uma seguradora precificar apólices: `id_usuario`, `nome`, `email`, `data_nasc`, `batimento_cardiaco_medio`, `doenca_pre_existente`, `geo_lat_long_tempo_real`, `renda_mensal`.
- **Diagnóstico Jurídico/Técnico:** Transferência bruta é ilegal por cruzar PII com dados médicos sensíveis, criando risco de exclusão discriminatória.
- **Intervenção Arquitetural Obrigatória:**
  1. **DROP:** Deletar `nome` e `email` (modelos de precificação não precisam de identificação civil).
  2. **HASHING:** Converter `id_usuario` via algoritmo unidirecional com salt (ex: `SHA-256`) para manter a integridade relacional entre tabelas sem expor a identidade real.
  3. **GENERALIZAÇÃO / AGRUPAMENTO:** Transformar `data_nasc` em categorias macro de **Faixa Etária** (ex: `[18-29]`, `[30-45]`, `[46+]`) e coordenadas de geolocalização precisa em **Macrorregião** (ex: `Sul`, `Sudeste`).

#### Cenário B: E-commerce e Inferência Sensível Invasiva (Caso Target)
- **Problema:** Um algoritmo de recomendação nota compras combinadas de produtos rotineiros (hidratantes sem fragrância, algodão, suplementos de zinco/magnésio) e infere gravidez, disparando cupons físicos para a residência de uma menor de idade.
- **Diagnóstico:** Violação gravíssima de privacidade via *Profiling* preditivo não consentido, deduzindo condição médica íntima a partir de dados não-sensíveis.
- **Mitigação:** Exigir Opt-in transparente para recomendações preditivas personalizadas e programar **Safety Constraints** (teto de segurança) nos modelos de Machine Learning, impedindo o disparo de campanhas comerciais automatizadas associadas a temas sensíveis de saúde ou menores.

#### Cenário C: Direito ao Esquecimento vs. Requisitos Fiscais (Integridade Referencial)
- **Problema:** Um usuário exige exclusão total de seus dados (`DELETE FROM usuarios WHERE id = 10`), mas apagar o registro quebraria as chaves estrangeiras em tabelas fiscais e notas de faturamento, cujo armazenamento é obrigatório por lei durante 5 anos.
- **Solução Arquitetural:** **Soft Delete com Anonimização Lógica**:
```sql
UPDATE usuarios 
SET nome = 'ANÔNIMO', 
    email = 'anon_8f4b2@hash.internal', 
    telefone = NULL, 
    cpf = NULL, 
    is_ativo = FALSE 
WHERE id_usuario = 159;
```
*Garante o cumprimento da LGPD desvinculando o titular e preserva a integridade fiscal/contábil do sistema.*

---

# MÓDULO 2: Estatística Descritiva 1 - Posição, Dispersão e Caos

### 2.1. O Papel da Estatística Descritiva
A estatística descritiva não prevê o futuro (papel do Machine Learning); ela tira uma **fotografia diagnóstica do passado** para organizar o caos e detectar distorções nos dados antes de qualquer modelagem.

### 2.2. Medidas de Tendência Central (Posição)

#### A Média Aritmética
Ponto de equilíbrio gravitacional de todas as forças numéricas.
$$\bar{x} = \frac{\sum_{i=1}^n x_i}{n} \quad (\text{Amostra}) \qquad \mu = \frac{\sum_{i=1}^N x_i}{N} \quad (\text{População})$$
- **Ponto Fraco:** Extremamente vulnerável e puxada por valores atípicos (outliers).
- **A Mentira da Média:** 4 programadores ganham R\$ 5.000 (Média = R\$ 5.000). O CEO entra na sala ganhando R\$ 100.000. A nova média salta para R\$ 24.000. Ninguém na sala ganha R\$ 24.000.

#### A Mediana ($Md$ ou $\tilde{x}$)
O valor central que divide a distribuição exatamente ao meio (50% dos dados abaixo, 50% dos dados acima).
- **Regra Obrigatória:** Os dados **devem estar ordenados** em ordem crescente antes de localizar o centro.
- **Cálculo:**
  - *Tamanho ímpar ($n$ ímpar):* O elemento central na posição $\frac{n+1}{2}$.
  - *Tamanho par ($n$ par):* A média aritmética dos dois elementos centrais nas posições $\frac{n}{2}$ e $\frac{n}{2} + 1$.
- **Vantagem:** Imune a valores extremos/outliers (o salário do CEO de R\$ 1 milhão não afeta a posição física do indivíduo do meio da fila).

#### A Moda ($Mo$)
O elemento que aparece com maior frequência no conjunto.
- **Propriedade Única:** É a **única medida de centralidade aplicável a variáveis categóricas / strings** (ex: qual é o status HTTP mais frequente nos logs: `['404', '500', '200', '500']` $\to$ Moda = `'500'`).

### 2.3. Medidas de Dispersão (Variabilidade e Risco)
Duas empresas podem apresentar a exata mesma média salarial de R\$ 5.000. Uma pode pagar R\$ 5.000 para todos (estabilidade absoluta), enquanto a outra paga R\$ 1.000 para alguns e R\$ 9.000 para outros (desigualdade e instabilidade). Medidas de posição são cegas para isso; medidas de dispersão medem o **risco operacional**.

#### Variância ($s^2$ ou $\sigma^2$)
Calcula a média das distâncias quadráticas de cada observação até a média aritmética.
$$s^2 = \frac{\sum_{i=1}^n (x_i - \bar{x})^2}{n - 1} \quad (\text{Amostral}) \qquad \sigma^2 = \frac{\sum_{i=1}^N (x_i - \mu)^2}{N} \quad (\text{Populacional})$$
- *Por que elevar ao quadrado?* Para impedir que desvios negativos anulem os desvios positivos, o que resultaria em zero.
- *Por que dividir por $(n - 1)$ na amostra?* Conhecido como **Correção de Bessel**, corrige a tendência de subestimar a dispersão real da população ao trabalhar com amostras pequenas.
- *Ponto Fraco:* A unidade de medida é elevada ao quadrado (ex: R\$ ao quadrado, milissegundos ao quadrado), inviabilizando a leitura executiva direta.

#### Desvio Padrão ($s$ ou $\sigma$)
A raiz quadrada da variância. Restaura a medida de dispersão para a **unidade de medida original do problema**.
$$s = \sqrt{s^2} \qquad \sigma = \sqrt{\sigma^2}$$
- **Tradução Executiva:** Indica em média quanto os dados oscilam e se afastam do ponto de equilíbrio (média). Quanto menor o desvio padrão, mais homogêneo e previsível é o processo.
- **Padrão Ouro Industrial (Six Sigma - $6\sigma$):** Metodologia em que os limites de tolerância de defeitos encontram-se a 6 desvios padrões de distância da média do processo, resultando em uma taxa aceitável de apenas **3.4 peças com defeito por milhão de transações**.

---

# MÓDULO 3: Estatística Descritiva 2 - Quartis, Cercas Matemáticas e Raio-X Visual

### 3.1. Quartis e Fatiamento da População
Enquanto a mediana divide o conjunto em 2 partes (50%), os quartis dividem a base ordenada em 4 blocos de 25%:
$$\text{Mínimo} \quad \xrightarrow{25\%} \quad Q_1 \quad \xrightarrow{25\%} \quad Q_2 \text{ (Mediana)} \quad \xrightarrow{25\%} \quad Q_3 \quad \xrightarrow{25\%} \quad \text{Máximo}$$
- **$Q_1$ (Primeiro Quartil / Percentil 25):** Limite inferior onde residem os 25% menores valores da base.
- **$Q_2$ (Segundo Quartil / Percentil 50):** A **Mediana** exata.
- **$Q_3$ (Terceiro Quartil / Percentil 75):** Limite a partir do qual estão os 25% maiores valores da base.

### 3.2. Intervalo Interquartil (IQR - *Interquartile Range*)
$$IQR = Q_3 - Q_1$$
- **Significado Técnico:** Representa a amplitude que engloba os **50% centrais mais homogêneos e estáveis** da base de dados.
- **A Blindagem do IQR:** Se inserirmos uma anomalia astronômica (ex: salário de 1 bilhão de reais), a Média e o Desvio Padrão explodem, mas o IQR permanece praticamente **inalterado**, pois ele ignora as pontas e avalia apenas o comportamento do miolo da população.

### 3.3. As Cercas Matemáticas de John Tukey (Detecção Algorítmica de Anomalias)
Algoritmos de detecção de fraudes e higienização de dados não utilizam estimativas subjetivas; utilizam as **Cercas de Tukey**:
$$\text{Limite Inferior } (LI) = Q_1 - 1.5 \times IQR$$
$$\text{Limite Superior } (LS) = Q_3 + 1.5 \times IQR$$
- **Regra de Julgamento de Negócio:**
  - Qualquer dado menor que o Limite Inferior ($x < LI$) ou estritamente maior que o Limite Superior ($x > LS$) é marcado formalmente como **Outlier (Anomalia)**.
  - Em sistemas de cibersegurança ou detecção de fraudes financeiras, requisições além do $LS$ são alvos de bloqueio automatizado ou acionamento de step-up authentication.

### 3.4. Anatomia do Gráfico de Caixa (Boxplot)
```
          Outlier (Ponto isolado)
             *  
             |          <- Limite Superior (Q3 + 1.5 * IQR)
        +----+----+     <- Q3 (75% dos dados)
        |         |
        |---------|     <- Q2 / Mediana (50% dos dados)
        |         |
        +----+----+     <- Q1 (25% dos dados)
             |          <- Limite Inferior (Q1 - 1.5 * IQR)
```
- A **Caixa** desenha fisicamente a área ocupada pelo **IQR** ($Q_1$ a $Q_3$).
- A **Linha Central** interna indica o valor da **Mediana**.
- Os **Bigodes** (*whiskers*) estendem-se até o menor e maior valores contidos dentro das cercas aceitáveis.
- **Marcadores Externos (Bolinhas):** Qualquer observação desenhada além dos bigodes é uma anomalia matemática explícita.

### 3.5. Histogramas, Regra de Sturges e Distribuições

#### A Fórmula da Regra de Sturges
Para evitar que o histograma fique visualmente estragado por excesso de barras estreitas ou compactado demais, calculamos o número ideal de compartimentos (**bins = $k$**):
$$k = 1 + 3.322 \times \log_{10}(N)$$
*(Onde $N$ é o volume total de registros na base. O resultado de $k$ deve ser sempre arredondado para o inteiro mais próximo).*
- *Exemplo com $N = 1.000$:* $\log_{10}(1000) = 3 \implies k = 1 + 3.322 \times 3 = 10.966 \to \mathbf{11 \text{ Bins}}$.
- *Exemplo com $N = 8.500$:* $\log_{10}(8500) \approx 3.929 \implies k = 1 + 3.322 \times 3.929 \approx 14.05 \to \mathbf{14 \text{ Bins}}$.

#### Assimetria e a Disputa entre Média e Mediana
```
Assimetria Positiva (À Direita)        Simétrica / Normal          Assimetria Negativa (À Esquerda)
          /\                                   /\                                   /\
         /  \                                 /  \                                 /  \
        /    \___                            /    \                            ___/    \
       /         \                          /      \                          /         \
   [Moda][Md]  [Média]               [Média = Md = Moda]               [Média]  [Md][Moda]
```
1. **Assimetria à Direita (Positiva):** A cauda da montanha alonga-se para a direita (valores altos atípicos, como distribuição de renda ou faturamento). A Média é arrastada pelos extremos:
   $$\mathbf{Média > Mediana}$$
2. **Assimetria à Esquerda (Negativa):** A cauda alonga-se para o lado esquerdo (valores baixos atípicos, como idade de aposentadoria ou notas de alunos em turma com alto desempenho):
   $$\mathbf{Média < Mediana}$$
3. **Distribuição Simétrica (Curva Normal):** Equilíbrio bilateral perfeito:
   $$\mathbf{Média \approx Mediana \approx Moda}$$

---

# MÓDULO 4: Inferência Estatística e Testes A/B (SciPy)

### 4.1. Escolha do Gráfico Correto por Tipo de Variável
| Objetivo Analítico | Tipos de Variáveis | Gráfico Recomendado | Comando Seaborn |
| :--- | :--- | :--- | :--- |
| **Volume / Frequência Absoluta** | Categórica (Texto pura) | Gráfico de Contagem | `sns.countplot(data=df, x='categoria')` *(Não use pizza!)* |
| **Comparação de Médias** | Categórica (X) vs. Numérica (Y) | Gráfico de Barras | `sns.barplot(data=df, x='versao', y='ticket')` |
| **Séries Temporais / Tendência** | Tempo/Data (X) vs. Numérica (Y) | Gráfico de Linha | `sns.lineplot(data=df, x='data', y='valor')` |
| **Formato da Distribuição** | Numérica Contínua | Histograma | `sns.histplot(data=df, x='valor', bins=k, kde=True)` |
| **Dispersão e Outliers** | Numérica Contínua | Gráfico de Caixa | `sns.boxplot(data=df, x='versao', y='valor')` |
| **Correlação entre Duas Contínuas** | Numérica (X) vs. Numérica (Y) | Gráfico de Dispersão | `sns.scatterplot(data=df, x='x', y='y', alpha=0.3)` |

> **Atenção à Haste Preta do `sns.barplot`:** Aquela linha vertical sobre a barra representa o **Intervalo de Confiança / Variabilidade Amostral**. Se a haste for desproporcionalmente longa, a variância interna daquele grupo é gigantesca e a média visual da barra não é confiável.

### 4.2. Transição: Descritiva vs. Inferencial
- **Estatística Descritiva:** Fotografia retrospectiva. Afirma que na amostra colhida ontem o grupo B teve média R\$ 122 e o grupo A teve R\$ 120. Não garante repetibilidade.
- **Inferência Estatística:** Ciência indutiva. Analisa o comportamento de uma amostra finita para calcular com rigor matemático a probabilidade de que aquela diferença seja uma propriedade perene da população real.

### 4.3. Estruturação Formal de um Teste A/B
- **Hipótese Nula ($H_0$ - O Ceticismo da Ciência):** Afirma que **não há efeito real**. As duas versões são equivalentes e qualquer superioridade numérica vista nos gráficos é mero fruto do acaso, ruído e sorte amostral.
- **Hipótese Alternativa ($H_1$ - A Evidência):** Afirma que **a diferença é estatisticamente significante**. A nova interface provocou uma mudança estrutural real no comportamento do consumidor.

### 4.4. A Batalha: Sinal vs. Ruído
O algoritmo do Teste T de Student computa uma fração fundamental:
$$\text{Estatística } t \propto \frac{\text{Sinal (Diferença entre as Médias: } \bar{x}_B - \bar{x}_A)}{\text{Ruído (Dispersão Combinada: Desvio Padrão e Variância)}}$$
- Se os dados apresentarem alta variância interna (compras variando de R\$ 10 a R\$ 5.000 na mesma tela), o **ruído esmaga o sinal**. Mesmo que a média de B pareça discretamente maior no barplot, o teste estatístico rejeitará o deploy da interface.

### 4.5. O Conceito Exato de P-Valor e a Régua de Decisão ($\alpha = 0.05$)
- **Definição Técnica:** O **P-Valor (Probability Value)** é a probabilidade exata de termos observado uma diferença igual ou mais extrema do que a encontrada, assumindo que a Hipótese Nula ($H_0$) seja a verdade absoluta da vida.
- **Tradução Executiva:** O P-Valor é a **taxa de chance de você estar sendo enganado pela sorte**.
  - P-Valor de `0.22` (22%): Há 22% de chance de ser puro ruído e coincidência. Risco inaceitável.
  - P-Valor de `0.003` (0.3%): A probabilidade de ser obra do acaso é desprezível. Efeito real.
- **A Matriz de Corte Universal ($\alpha = 0.05$ ou 5% de tolerância):**
  - **Se $p < 0.05$:** **Rejeitamos a Hipótese Nula ($H_0$)**. O efeito é estatisticamente significante. **Decisão:** Aprovar o deploy em produção e pagar o bônus de performance à equipe.
  - **Se $p \ge 0.05$:** **Falhamos em rejeitar a Hipótese Nula ($H_0$)**. A diferença observada não tem sustentação matemática. **Decisão:** Abortar a nova interface e manter a versão estável original.

---

# MÓDULO 5: Correlação, Covariância e Causalidade

### 5.1. A Regra de Ouro: "Correlação NÃO Implica Causalidade"
- Duas variáveis podem oscilar sincronizadas perfeitamente sem que uma exerça nenhuma influência causal direta sobre a outra.
- **O Paradoxo dos Tubarões e Sorvetes:** No litoral, quando as vendas de sorvete aumentam, os ataques de tubarão sobem na mesma taxa. Sorvete atrai tubarões? Não.
- **A Força Confundidora (Variável Oculta / *Confounding Variable*):** O **Verão (temperatura ambiente alta)**. O calor impulsiona a compra de sorvetes e simultaneamente atrai milhares de banhistas ao mar, elevando a probabilidade de encontros com tubarões.

### 5.2. O Gráfico de Dispersão (Scatterplot) e Geometrias Visuais
1. **Nuvem Ascendente Diagonal:** Correlação Positiva ($X$ sobe $\implies$ $Y$ sobe).
2. **Nuvem Descendente Diagonal:** Correlação Negativa ($X$ sobe $\implies$ $Y$ desce).
3. **Nuvem Dispersa Esférica/Caótica:** Ausência de Correlação ($r \approx 0$).
4. **Alinhamento Horizontal Contínuo no Topo (Teto Artificial / *Cap*):** Indica **censura ou limitação técnica no sistema de captação de dados** (ex: o sistema trunca salários ou preços de imóveis no teto de R\$ 500.000). Esse ruído deve ser expurgado antes de calcular métricas de correlação.

### 5.3. Covariância vs. Coeficiente de Pearson ($r$)
- **Covariância ($Cov(X, Y)$):** Mede a tendência de duas variáveis se afastarem simultaneamente de suas médias.
  - *Problema Insuperável da Covariância:* O resultado depende das unidades de medida físicas dos eixos. Se medirmos salários em Centavos em vez de Reais, a covariância escala para centenas de milhões, impedindo qualquer comparação.
- **Correlação de Pearson ($r$):** É a covariância dividida pelo produto dos desvios padrões (Normalização).
  $$r = \frac{Cov(X, Y)}{s_x \cdot s_y}$$
  - O resultado é um indicador padronizado universal variando rigorosamente entre **$-1.0$ e $+1.0$**.

### 5.4. Guia de Bolso: Escala de Força de Pearson ($|r|$)
| Intervalo do Coeficiente ($|r|$) | Força da Relação Linear | Aplicação para Decisão de Negócios |
| :---: | :---: | :--- |
| **$0.70$ a $1.00$** | **Muito Forte / Forte** | Relação linear robusta. Variável mandatória para compor modelos preditivos de inteligência artificial. |
| **$0.40$ a $0.69$** | **Moderada** | Há clara tendência identificável, porém requer o acréscimo de variáveis auxiliares para prever com precisão. |
| **$0.00$ a $0.39$** | **Fraca / Desprezível** | Ruído ou relacionamento linear inexpressivo. Inútil para ser utilizada como motor isolado de tomada de decisão. |

### 5.5. O Ponto Cego de Pearson vs. A Solução de Spearman
- **A Fragilidade de Pearson:** O coeficiente de Pearson é cego para qualquer crescimento que não ocorra em **linha reta**. Se a relação for exponencial acelerada (ex: propagação viral $y = x^3$), o Pearson registrará um valor artificialmente baixo e é sensível a outliers pontuais.
- **O Coeficiente de Spearman:** Opera convertendo os valores brutos para **Postos e Hierarquias (Rankings ordinais)**. Ele avalia apenas a *Monotonicidade*: "quando a posição de $X$ sobe no ranking geral, a posição de $Y$ também sobe?".
  - **Vantagem de Spearman:** É imune a transformações monotônicas curvas e altamente resistente a anomalias extremas.

### 5.6. Matriz de Correlação e Heatmaps
Em Data Warehouses com dezenas de colunas, calculamos a correlação matricial completa (`df.corr()`).
- A diagonal principal é sempre $1.0$ (correlação de uma variável consigo mesma).
- **Detecção de Multicolinearidade:** Se duas variáveis preditoras (como `Qtd_Quartos` e `Qtd_Suites`) apresentarem correlação extrema entre si ($r > 0.80$), elas carregam a mesma informação redundante no banco de dados.

---

# MÓDULO 6: Machine Learning Preditivo - Regressão Linear Simples (Scikit-Learn)

### 6.1. O Salto da Correlação para a Previsão
O coeficiente de Pearson aponta que a Renda do Bairro dita o Preço do Imóvel ($r = +0.69$). Porém, ele é incapaz de responder à pergunta do CEO: *"Se a renda de um bairro novo for R\$ 8.500, qual é o valor exato em reais pelo qual o imóvel deve ser anunciado?"*. Para responder a isso, precisamos de um motor preditivo alimentado por **Aprendizado Supervisionado**.

### 6.2. A Geometria da Reta de Previsão
$$\hat{y} = w_1 X + w_0$$
- $\hat{y}$ (*y-chapéu*): A **Previsão Numérica** calculada pelo algoritmo.
- $X$: A **Variável de Entrada (Atributo Preditivo)**.
- $w_1$ (`modelo.coef_[0]`): O **Peso / Coeficiente Angular / Inclinação da Reta**.
  - *Significado Econômico:* A **Taxa de Variação Marginal**. Responde à pergunta: *"Para cada 1 unidade que $X$ aumenta, quanto $y$ sobe ou desce exatamente?"*. Se $w_1 = 25$, cada minuto adicional no site acarreta R\$ 25,00 a mais em faturamento.
- $w_0$ (`modelo.intercept_`): O **Viés / Intercepto Linear**.
  - *Significado Econômico:* O ponto de ancoragem no eixo Y. Responde à pergunta: *"Qual seria o valor do imóvel ou do gasto se a variável de entrada $X$ for rigorosamente ZERO?"*.

### 6.3. O Algoritmo OLS (*Ordinary Least Squares* / Mínimos Quadrados)
- Nenhum modelo acerta 100% dos pontos. A diferença entre a realidade observada e a previsão é o **Resíduo ($e_i = y_i - \hat{y}_i$)**.
- O método de Mínimos Quadrados ajusta o peso $w_1$ e o viés $w_0$ iterativamente com o objetivo formal de **minimizar a soma de todos os resíduos elevados ao quadrado** ($\min \sum e_i^2$).

### 6.4. O Erro Número 1 dos Desenvolvedores no Scikit-Learn: A Matriz 2D
- O framework Scikit-Learn exige que a variável explicativa ($X$) seja empacotada obrigatoriamente como uma **Matriz Bidimensional (2D)** com formato `(n_linhas, n_colunas)`.
- A variável alvo ($y$) deve ser um **Vetor Unidimensional (1D)** com formato `(n_linhas,)`.
- *Como garantir a matriz 2D no Pandas:* Usando **duplos colchetes** na seleção: `X = df[['coluna']]`.

### 6.5. O Tribunal de Avaliação do Modelo: Métricas Oficiais
1. **MAE (*Mean Absolute Error* / Erro Absoluto Médio):**
   Média das diferenças absolutas $|y - \hat{y}|$. É simples e intuitivo, mas não penaliza severamente os erros desastrosos.
2. **MSE (*Mean Squared Error* / Erro Quadrático Médio):**
   Média dos erros elevados ao quadrado. Pune com rigor máximo as previsões que erraram longe do alvo, mas sua unidade fica ao quadrado (ex: Reais ao quadrado), sendo ilegível para a diretoria.
3. **RMSE (*Root Mean Squared Error* / Raiz do Erro Quadrático Médio):**
   A raiz quadrada do MSE. **É o padrão-ouro de avaliação em regressão**. Ele devolve a penalidade dos grandes erros de volta para a **unidade financeira original do negócio (R\$)**. Representa a margem média de erro do modelo.
4. **$R^2$ Score (Coeficiente de Determinação):**
   Métrica adimensional variando entre $0$ e $1$ ($0\%$ a $100\%$).
   - *Significado Executivo:* Representa a proporção da variância total da variável alvo que é **explicada matematicamente pela nossa variável de entrada**.
   - Se $R^2 = 0.473$, significa que a Renda explica $47.3\%$ das flutuações de preços. Os $52.7\%$ restantes dependem de atributos ignorados pelo modelo (localização, conservação, metragem).

### 6.6. O Modelo em Produção: Previsão e Bandas de Incerteza Executiva
Ao apresentar projeções para a diretoria, fornecer apenas a estimativa pontual é irresponsável perante a incerteza estatística. Construímos três cenários usando o RMSE:
- **Cenário Base (Estimativa Central):** $\hat{y} = \text{modelo.predict}([[X_{\text{novo}}]])[0]$
- **Cenário Otimista (Teto Superior):** $\text{Teto} = \hat{y} + RMSE$
- **Cenário Pessimista (Piso Inferior):** $\text{Piso} = \hat{y} - RMSE$

---

# MÓDULO 7: Gabarito Completo do Simulado Integrador (Caso TechMarket)

Abaixo encontra-se a resolução integral do notebook `Desafio e Revisao - Aula 07.ipynb` (Simulado Global do 1º Bimestre), organizado fase por fase com justificativas teóricas para consulta direta na prova:

### FASE 0: Importação e Geração de Dados
```python
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error, r2_score

sns.set_theme(style="whitegrid")
```

---

### FASE 1: Adequação à LGPD (Remoção de PII)
**Enunciado:** Exclua a coluna que expõe a identidade do cliente (`Email`) gerando a base `df_seguro`.
```python
# RESOLUÇÃO OFICIAL
df_seguro = df.drop(columns=['Email'])
display(df_seguro.head())

# JUSTIFICATIVA DE NEGÓCIO:
# A coluna 'Email' é uma Informação Pessoalmente Identificável (PII).
# A equipe de ciência de dados não necessita de identificação direta para calibrar
# modelos preditivos de faturamento. Manter a coluna violaria o Princípio da Minimização.
```

---

### FASE 2: Diagnóstico Descritivo (Posição e Outliers)
**Enunciado:** Identifique a região que mais acessa o site (Moda), a Média e a Mediana de `Gasto_Site_R$`. Analise a presença de outliers.
```python
# 1. Região mais frequente (Moda Categórica)
regiao_moda = df_seguro['Regiao'].mode()[0]
print(f"Região com maior volume de acessos (Moda): {regiao_moda}")

# 2. Média de Gastos
media_gasto = df_seguro['Gasto_Site_R$'].mean()
print(f"Gasto Médio: R$ {media_gasto:.2f}")

# 3. Mediana de Gastos
mediana_gasto = df_seguro['Gasto_Site_R$'].median()
print(f"Mediana de Gastos: R$ {mediana_gasto:.2f}")

# JUSTIFICATIVA DE NEGÓCIO / PROVA:
# A Média (ex: ~R$ 560,00) resultou sensivelmente maior do que a Mediana (ex: ~R$ 535,00).
# Quando Média > Mediana, a distribuição apresenta Assimetria Positiva (à direita),
# indicando a presença contundente de Outliers extremos que arrastam o equilíbrio da média.
```

---

### FASE 3: Tradução Visual Executiva
**Enunciado:** Plote um `barplot` de Gasto por Região e um `boxplot` do Gasto geral.
```python
fig, axs = plt.subplots(1, 2, figsize=(14, 5))

# 1. Barplot de Gastos por Região
sns.barplot(data=df_seguro, x='Regiao', y='Gasto_Site_R$', ax=axs[0], palette='Blues_d')
axs[0].set_title('Gasto Médio por Região')

# 2. Boxplot Geral de Gastos
sns.boxplot(data=df_seguro, y='Gasto_Site_R$', ax=axs[1], color='coral')
axs[1].set_title('Distribuição Geral e Detecção de Outliers')

plt.tight_layout()
plt.show()

# JUSTIFICATIVA DE NEGÓCIO / PROVA:
# O boxplot ratificou graficamente a hipótese da Fase 2: existem dois pontos isolados
# disparando no topo (próximos a R$ 9.000,00), situados muito além do bigode superior.
```

---

### FASE 4: O Julgamento Científico do Teste A/B
**Enunciado:** Isole o tempo de tela das versões A e B, aplique o teste de hipótese do SciPy com $\alpha = 0.05$ e emita o parecer de deploy.
```python
# 1. Isolando as arrays puras
tempo_A = df_seguro[df_seguro['Versao_Site'] == 'A']['Tempo_Tela_Min']
tempo_B = df_seguro[df_seguro['Versao_Site'] == 'B']['Tempo_Tela_Min']

# 2. Executando o Teste T de Student para amostras independentes
t_stat, p_valor = stats.ttest_ind(tempo_A, tempo_B)

print(f"Estatística T: {t_stat:.4f}")
print(f"P-Valor: {p_valor:.4f}")

# 3. Automação de Decisão Executiva (Regra do Alfa)
if p_valor < 0.05:
    print("Veredito: Diferença estatisticamente real (Rejeitamos H0). Deploy da Versão B APROVADO!")
else:
    print("Veredito: Diferença insignificante decorrente do acaso (Falhamos em rejeitar H0). Manter Versão A!")
```

---

### FASE 5.1: Prova de Correlação e Dispersão
**Enunciado:** Calcule o Pearson entre `Tempo_Tela_Min` e `Gasto_Site_R$` e plote o scatterplot.
```python
# 1. Correlação de Pearson
corr_pearson = df_seguro['Tempo_Tela_Min'].corr(df_seguro['Gasto_Site_R$'])
print(f"Correlação de Pearson: {corr_pearson:.4f}")

# 2. Gráfico de Dispersão
plt.figure(figsize=(7, 5))
sns.scatterplot(data=df_seguro, x='Tempo_Tela_Min', y='Gasto_Site_R$', alpha=0.5, color='darkgreen')
plt.title(f'Dispersão: Tempo de Tela vs Gasto (r = {corr_pearson:.2f})')
plt.show()
```

---

### FASE 5.2: Treinamento Preditivo e Métricas de Erro
**Enunciado:** Remova os outliers com gastos gigantes ($< 8000$), treine o modelo linear em matriz 2D, extraia pesos e calcule $R^2$ e $RMSE$.
```python
# 1. Higienização de Anomalias
df_limpo = df_seguro[df_seguro['Gasto_Site_R$'] < 8000]

# 2. Separação de Matrizes (Atenção ao duplo colchete no X)
X = df_limpo[['Tempo_Tela_Min']]   # Matriz 2D
y = df_limpo['Gasto_Site_R$']      # Vetor 1D

# 3. Instanciação e Treinamento
modelo = LinearRegression()
modelo.fit(X, y)

# 4. Geração de Previsões no conjunto de treino
previsoes = modelo.predict(X)

# 5. Métricas e Parâmetros
r2 = r2_score(y, previsoes)
rmse = root_mean_squared_error(y, previsoes)
peso_w1 = modelo.coef_[0]
vies_w0 = modelo.intercept_

print(f"Equação Aprendida: Gasto = ({peso_w1:.2f} * Tempo_Tela) + ({vies_w0:.2f})")
print(f"Coeficiente R²: {r2:.4f} (Explica {r2*100:.1f}% da variância)")
print(f"Margem de Erro (RMSE): R$ {rmse:.2f}")

# INTERPRETAÇÃO DOS COEFICIENTES:
# Peso w1 (~25.0): A cada 1 minuto adicional de permanência na tela, o cliente gasta R$ 25,00 a mais.
# Viés w0 (~150.0): Se o cliente passar zero minutos (apenas abre e fecha), o gasto base teórico estimado é de R$ 150,00.
```

---

### FASE 6 (FINAL BOSS): Previsão em Produção com Bandas de Incerteza
**Enunciado:** Preveja o gasto de um usuário que fica 45 minutos no site, informando o valor central, o cenário otimista e o cenário pessimista com base no RMSE.
```python
# 1. Previsão Pontual (Entrada OBRIGATORIAMENTE em matriz 2D [[45]])
entrada_minutos = [[45]]
previsao_central = modelo.predict(entrada_minutos)[0]

# 2. Cenários com Margem de Erro Financeira
cenario_otimista = previsao_central + rmse
cenario_pessimista = previsao_central - rmse

print("===== RELATÓRIO PREDITIVO DE PRODUÇÃO =====")
print(f"Previsão Pontual (45 min): R$ {previsao_central:.2f}")
print(f"Cenário Otimista (Teto):    R$ {cenario_otimista:.2f}")
print(f"Cenário Pessimista (Piso):   R$ {cenario_pessimista:.2f}")
print(f"Margem de Risco Financeiro: ± R$ {rmse:.2f}")
```

---

# MÓDULO 8: Arsenal de Código - Problemático vs. Corrigido & Trap Guide

Neste módulo estão reunidos os **erros mais comuns de prova** cometidos por estudantes em código e sintaxe, acompanhados da respectiva **correção exata**:

### Trap 1: O Erro Dimensional do Scikit-Learn (Vetor 1D no Treinamento)
O Scikit-Learn aborta com erro fatal `ValueError: Expected 2D array, got 1D array instead` quando a coluna preditora é passada com colchete simples.

```python
# [CÓDIGO PROBLEMÁTICO - FALHA NO RUNTIME]
X = df['Tempo_Tela_Min']  # Gera uma Series do Pandas (1D)
y = df['Gasto_Site_R$']
modelo = LinearRegression()
modelo.fit(X, y)          # ERRO CRÍTICO AQUI!
```

```python
# [CÓDIGO CORRIGIDO - PADRÃO DA INDÚSTRIA]
X = df[['Tempo_Tela_Min']] # Uso de DUPLO colchete força a criação de um DataFrame (Matriz 2D)
y = df['Gasto_Site_R$']
modelo = LinearRegression()
modelo.fit(X, y)          # Treina com sucesso em milissegundos!
```

---

### Trap 2: Previsão Unitária com Dimensão Inválida
Tentar prever passando um valor numérico simples ou lista plana unidimensional `[45]` resulta em falha de forma.

```python
# [CÓDIGO PROBLEMÁTICO - FALHA NO RUNTIME]
resposta = modelo.predict(45)    # Falha: Espera matriz 2D
# OU
resposta = modelo.predict([45])  # Falha: Vetor 1D
```

```python
# [CÓDIGO CORRIGIDO - ENTRADA 2D EXATA]
# Opção A (Formato do Professor): Passar como lista de listas [[45]] e extrair [0]
resposta = modelo.predict([[45]])[0] 
print(f"Valor previsto: R$ {resposta:.2f}")

# Opção B (Mais elegante, evita UserWarning de colunas no Scikit-Learn):
entrada_df = pd.DataFrame({'Tempo_Tela_Min': [45]})
resposta = modelo.predict(entrada_df)[0]
print(f"Valor previsto: R$ {resposta:.2f}")
```

---

### Trap 3: Extração da Moda Categórica Retornando Objeto Pandas
O comando `.mode()` não devolve um escalar simples, mas uma `pd.Series` (porque podem existir conjuntos multimodais). Se tentar concatenar em strings diretamente, polui a saída de dados.

```python
# [CÓDIGO PROBLEMÁTICO - RETORNA UMA SERIES]
moda_regiao = df['Regiao'].mode()
print(f"A região é: {moda_regiao}")
# Saída feia no terminal:
# A região é: 0    Sudeste
# dtype: object
```

```python
# [CÓDIGO CORRIGIDO - ACESSA O PRIMEIRO VALOR ESCALAR]
moda_regiao = df['Regiao'].mode()[0]
print(f"A região mais frequente é: {moda_regiao}")
# Saída perfeita: A região mais frequente é: Sudeste
```

---

### Trap 4: Erro de Sintaxe em Filtro Booleano de Outliers no Pandas
No Python nativo usamos as palavras-chave `and` / `or`. No Pandas, filtros em DataFrames exigem operadores bitwise (`&` e `|`) e parênteses obrigatórios em volta de cada cláusula lógica.

```python
# [CÓDIGO PROBLEMÁTICO - OPERADOR ERRADO OU FALTA DE PARÊNTESES]
# Falha 1: Usar 'and' do Python
df_limpo = df[df['ticket'] <= limite_sup and df['ticket'] >= limite_inf] # ValueError!

# Falha 2: Esquecer parênteses com '&'
df_limpo = df[df['ticket'] <= limite_sup & df['ticket'] >= limite_inf]   # Erro de precedência de operadores!
```

```python
# [CÓDIGO CORRIGIDO - PARÊNTESES E OPERADOR BITWISE '&']
df_limpo = df[(df['ticket'] <= limite_sup) & (df['ticket'] >= limite_inf)]
```

---

### Trap 5: Injeção de Dados no Teste T do SciPy
Passar o DataFrame inteiro ou colunas sem filtrar as categorias quebra o algoritmo de comparação de médias.

```python
# [CÓDIGO PROBLEMÁTICO - NÃO SEPARA AS COORTES]
# O SciPy não sabe quem é 'A' e quem é 'B' se você passar o DF completo:
stat, p = stats.ttest_ind(df['Versao_Site'], df['Tempo_Tela_Min']) # Erro de tipos e lógica!
```

```python
# [CÓDIGO CORRIGIDO - FILTRAGEM PRÉVIA DAS ARRAYS NUMÉRICAS]
amostra_A = df[df['Versao_Site'] == 'A']['Tempo_Tela_Min']
amostra_B = df[df['Versao_Site'] == 'B']['Tempo_Tela_Min']

stat, p_valor = stats.ttest_ind(amostra_A, amostra_B)
```

---

### Trap 6: Cálculo do RMSE Usando a API Legada vs. Moderna do Scikit-Learn
Versões anteriores do Scikit-Learn usavam `mean_squared_error(y, y_pred, squared=False)`. Em versões recentes do Scikit-Learn (a partir da 1.4), o parâmetro `squared` foi descontinuado em favor da nova função direta `root_mean_squared_error`.

```python
# [CÓDIGO PROBLEMÁTICO / OBSOLETO EM VERSÕES RECENTES]
from sklearn.metrics import mean_squared_error
rmse = mean_squared_error(y, previsoes, squared=False) # Emite aviso de depreciação ou erro
# OU pior: esquecer o squared=False e calcular o MSE (bilhões de reais) em vez do RMSE!
```

```python
# [CÓDIGO CORRIGIDO - FUNÇÃO OFICIAL DA DISCIPLINA]
from sklearn.metrics import root_mean_squared_error
rmse = root_mean_squared_error(y, previsoes) # Retorna direto na escala monetária real!
```

---

### Trap 7: Eliminação de PII Sem Atribuir a Variável ou Esquecer `columns=`
O comando `df.drop('Email')` tenta deletar uma linha no índice 0 por padrão (`axis=0`), falhando com `KeyError: "['Email'] not found in axis"`.

```python
# [CÓDIGO PROBLEMÁTICO - BUSCA LINHA EM VEZ DE COLUNA]
df.drop('Email') # KeyError! Além disso, não salva o resultado e o df continua desprotegido.
```

```python
# [CÓDIGO CORRIGIDO - DECLARAÇÃO EXPLÍCITA DE COLUNA E ARMAZENAMENTO]
df_seguro = df.drop(columns=['Email']) # Especifica explicitamente que é uma coluna e salva em novo objeto.
```

---

### Trap 8: Cálculo Manual de Quartis e Esquecer a Ordenação dos Dados
Calcular quartis ou medianas manualmente na folha de papel sem ordenar os dados do menor para o maior resulta em nota zero imediata.

```python
# [CÁLCULO PROBLEMÁTICO - DADOS BRUTOS DESORDENADOS]
dados = [45, 12, 60, 20, 30, 15, 80]
# Erro: Tentar pegar o meio direto da lista bruta: dados[3] -> 20 (TOTALMENTE ERRADO!)
```

```python
# [CÁLCULO CORRIGIDO - ORDENAÇÃO MANDATÓRIA]
dados_ordenados = sorted([45, 12, 60, 20, 30, 15, 80])
# [12, 15, 20, 30, 45, 60, 80]
# Elemento central exato: 30 (Mediana / Q2 = 30)
# Metade inferior: [12, 15, 20] -> Q1 = 15
# Metade superior: [45, 60, 80] -> Q3 = 60
# IQR = Q3 - Q1 = 60 - 15 = 45
```

---

## 🎯 GUIA DE CHEAT SHEET DE 1 LINHA PARA A PROVA

```python
# ESTATÍSTICA DESCRITIVA BÁSICA
df['col'].describe()                                   # Resumo completo (count, mean, std, min, 25%, 50%, 75%, max)
df['col'].mean()                                       # Média
df['col'].median()                                     # Mediana
df['col'].mode()[0]                                    # Moda
df['col'].std()                                        # Desvio Padrão
df['col'].var()                                        # Variância

# CERCAS DE TUKEY
q1 = df['col'].quantile(0.25); q3 = df['col'].quantile(0.75); iqr = q3 - q1
li = q1 - 1.5 * iqr; ls = q3 + 1.5 * iqr
df_limpo = df[(df['col'] >= li) & (df['col'] <= ls)]   # Base sem anomalias

# GRÁFICOS SEABORN
sns.countplot(data=df, x='cat')                        # Frequência de categoria (texto)
sns.barplot(data=df, x='cat', y='num')                 # Média de número por categoria
sns.boxplot(data=df, x='cat', y='num')                 # Caixa e outliers
sns.histplot(data=df, x='num', bins=11, kde=True)      # Histograma com Sturges
sns.scatterplot(data=df, x='x', y='y', alpha=0.3)      # Nuvem de dispersão
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f") # Matriz térmica

# TESTE A/B
from scipy import stats
t_stat, p = stats.ttest_ind(df[df['v']=='A']['y'], df[df['v']=='B']['y']) # Se p < 0.05: Deploy!

# REGRESSÃO LINEAR SCIKIT-LEARN
from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error, r2_score
mod = LinearRegression().fit(df[['X']], df['y'])       # X SEMPRE em [[ ]]
y_pred = mod.predict(df[['X']])
r2 = r2_score(df['y'], y_pred)
rmse = root_mean_squared_error(df['y'], y_pred)
previsao = mod.predict([[45]])[0]                      # Previsão pontual para X=45
```
