venv# ROTEIRO - PARTE 1 DA APRESENTAÇÃO
## Projeto de Disciplina de Redes Neurais com TensorFlow
### Classificação de Câncer de Mama

---

## 1. MEMBROS DO GRUPO

- **Mateus Teixeira Ramos da Silva** - [GitHub](https://github.com/GitMateusTeixeira/03-ml-modeling)
- [Adicionar outros membros conforme necessário]

---

## 2. PROBLEMA DE NEGÓCIO

### 2.1 Contexto e Relevância

O câncer de mama é uma das principais causas de morte por câncer em mulheres mundialmente. A detecção precoce é fundamental para aumentar as chances de cura e reduzir a mortalidade. Atualmente, o diagnóstico depende da análise manual de características morfológicas de células, um processo que pode ser:

- **Subjetivo**: Dependente da experiência do patologista
- **Demorado**: Análise manual consome tempo valioso
- **Custoso**: Requer especialistas altamente qualificados
- **Variável**: Pode haver inconsistências entre diferentes profissionais

### 2.2 Tipo de Problema

**CLASSIFICAÇÃO BINÁRIA SUPERVISIONADA**

**Por que Classificação?**
- Temos uma variável target categórica (diagnosis) com duas classes distintas:
  - **B (Benigno)**: Tumor não canceroso
  - **M (Maligno)**: Tumor canceroso
- O objetivo é predizer a categoria/classe do tumor baseado nas características morfológicas

**Por que Supervisionada?**
- Possuímos dados rotulados (ground truth) com diagnósticos confirmados
- O modelo aprenderá padrões a partir de exemplos conhecidos
- Podemos avaliar a performance comparando predições com diagnósticos reais

**Alternativas Consideradas e Rejeitadas:**
- **Regressão**: Rejeitada pois não queremos predizer valores contínuos
- **Agrupamento (Clustering)**: Rejeitada pois temos labels conhecidos
- **Classificação Multiclasse**: Não aplicável pois temos apenas duas classes

---

## 3. BASE DE DADOS

### 3.1 Origem e Credibilidade

**Fonte**: [Kaggle - Breast Cancer Dataset](https://www.kaggle.com/datasets/wasiqaliyasir/breast-cancer-dataset)

**Origem Original**: Wisconsin Diagnostic Breast Cancer (WDBC) Database
- Criado por: Dr. William H. Wolberg, University of Wisconsin
- Amplamente utilizado na literatura científica
- Benchmark padrão para algoritmos de classificação médica

### 3.2 Tamanho da Amostra

- **569 amostras** (pacientes)
- **33 colunas** (32 features + 1 target)
- **Sem dados faltantes** nas colunas relevantes
- **1 coluna nula** (Unnamed: 32) que será removida

**Justificativa do Tamanho:**
- Tamanho adequado para redes neurais simples
- Suficiente para validação cruzada robusta
- Permite divisão treino/validação/teste sem overfitting
- Comparável a outros estudos na área médica

### 3.3 Colunas / Features / Atributos

**Estrutura dos Dados:**
Cada feature é calculada para:
1. **Mean** (média): Valor médio da característica
2. **SE** (standard error): Erro padrão da característica  
3. **Worst** (pior valor): Maior valor (mais extremo) da característica

**10 Características Morfológicas Base:**

1. **radius**: Distância média do centro aos pontos do perímetro
2. **texture**: Desvio padrão dos valores de escala de cinza
3. **perimeter**: Perímetro do núcleo celular
4. **area**: Área do núcleo celular
5. **smoothness**: Variação local nos comprimentos dos raios
6. **compactness**: (perímetro² / área) - 1.0
7. **concavity**: Severidade das porções côncavas do contorno
8. **concave_points**: Número de porções côncavas do contorno
9. **symmetry**: Simetria do núcleo celular
10. **fractal_dimension**: "Aproximação da linha costeira" - 1

**Total: 30 features numéricas** (10 características × 3 estatísticas)

---

## 4. ANÁLISE EXPLORATÓRIA

### 4.1 Distribuição da Variável Target (Y)

**Distribuição das Classes:**
- **Benigno (B)**: 357 casos (62.7%)
- **Maligno (M)**: 212 casos (37.3%)

**Análise:**
- **Desbalanceamento moderado**: Razão aproximada 1.7:1
- **Não crítico**: Não requer técnicas especiais de balanceamento
- **Representativo**: Ambas as classes têm amostras suficientes
- **Realista**: Reflete a distribuição real na população

**Implicações para o Modelo:**
- Usar métricas balanceadas (F1-score, AUC-ROC)
- Considerar precision e recall para ambas as classes
- Stratified sampling na divisão treino/teste

### 4.2 Distribuição das Features (X)

**Características Observadas:**

1. **Escalas Diferentes**: 
   - Area: 143.5 - 2501.0
   - Smoothness: 0.05 - 0.16
   - **Necessidade**: Normalização obrigatória

2. **Distribuições Variadas**:
   - Algumas features seguem distribuição normal
   - Outras apresentam assimetria (skewness)
   - **Solução**: StandardScaler para padronização

3. **Outliers Presentes**:
   - Identificados através de boxplots
   - **Estratégia**: Manter (podem ser informativos clinicamente)

### 4.3 Atributos Mais e Menos Relevantes

**MAIS RELEVANTES (Baseado em Correlação e Importância Clínica):**

1. **concave_points_worst**: Alta correlação com malignidade
   - **Justificativa**: Tumores malignos tendem a ter contornos mais irregulares

2. **perimeter_worst**: Forte indicador de malignidade
   - **Justificativa**: Tumores maiores frequentemente são malignos

3. **concavity_worst**: Relacionado à forma irregular
   - **Justificativa**: Malignidade associada a bordas côncavas

4. **radius_worst**: Tamanho máximo do tumor
   - **Justificativa**: Tumores malignos tendem a crescer mais

5. **area_worst**: Área máxima do núcleo
   - **Justificativa**: Correlacionado com agressividade

**MENOS RELEVANTES:**

1. **fractal_dimension_mean**: Baixa correlação
   - **Justificativa**: Medida complexa, menos interpretável clinicamente

2. **symmetry_se**: Variabilidade baixa
   - **Justificativa**: Erro padrão da simetria pouco discriminativo

3. **smoothness_se**: Pouco poder discriminativo
   - **Justificativa**: Variação da suavidade menos informativa

**Metodologia de Seleção:**
- Análise de correlação com target
- Matriz de correlação entre features
- Conhecimento médico especializado
- Testes estatísticos (ANOVA, Chi-quadrado)

### 4.4 Representação Escolhida

**ESTRATÉGIA: Usar TODAS as 30 features numéricas**

**Justificativas:**

1. **Redes Neurais são Robustas**: Podem lidar com alta dimensionalidade
2. **Regularização**: Dropout e L2 previnem overfitting
3. **Informação Complementar**: Features "menos relevantes" podem ter valor em combinação
4. **Benchmark**: Permite comparação com literatura existente
5. **Custo Computacional Baixo**: 30 features é gerenciável

**Pré-processamento Aplicado:**
- Remoção da coluna 'id' (identificador único)
- Remoção da coluna 'Unnamed: 32' (valores nulos)
- Codificação da target: B=0, M=1
- StandardScaler nas features numéricas

---

## 5. TREINAMENTO

### 5.1 Topologia Escolhida

**ARQUITETURA: Rede Neural Feedforward Densa**

```
Camada de Entrada: 30 neurônios (features)
    ↓
Camada Oculta 1: 64 neurônios + ReLU + Dropout(0.3)
    ↓
Camada Oculta 2: 32 neurônios + ReLU + Dropout(0.3)
    ↓
Camada de Saída: 1 neurônio + Sigmoid
```

### 5.2 Justificativas da Arquitetura

**Por que Feedforward?**
- Dados tabulares não têm dependência sequencial
- Estrutura mais simples e interpretável
- Adequada para classificação binária
- Menor risco de overfitting

**Por que 2 Camadas Ocultas?**
- **1 camada**: Pode ser insuficiente para padrões complexos
- **2 camadas**: Balanceio entre capacidade e simplicidade
- **3+ camadas**: Risco de overfitting com dataset pequeno

**Por que 64 → 32 neurônios?**
- **Redução gradual**: Permite extração hierárquica de features
- **64 neurônios**: ~2x o número de features de entrada
- **32 neurônios**: Compressão intermediária antes da saída
- **Baseado em heurísticas**: Regras empíricas da literatura

**Por que ReLU?**
- **Não saturação**: Evita vanishing gradient
- **Computacionalmente eficiente**: Operação simples
- **Esparsidade**: Alguns neurônios ficam inativos
- **Estado da arte**: Padrão atual em deep learning

**Por que Dropout 0.3?**
- **Regularização**: Previne overfitting
- **30%**: Balanceio entre regularização e capacidade
- **Aplicado em treino**: Desabilitado na inferência

**Por que Sigmoid na saída?**
- **Classificação binária**: Output entre 0 e 1
- **Interpretabilidade**: Pode ser vista como probabilidade
- **Compatibilidade**: Funciona bem com binary_crossentropy

### 5.3 Referências e Benchmarks

**Literatura Científica:**

1. **Street, W.N., Wolberg, W.H. and Mangasarian, O.L. (1993)**
   - "Nuclear feature extraction for breast tumor diagnosis"
   - **Resultado**: 97.5% de acurácia com linear programming
   - **Nossa meta**: Superar com redes neurais

2. **Wolberg, W.H., Street, W.N. and Mangasarian, O.L. (1995)**
   - "Machine learning techniques to diagnose breast cancer"
   - **Comparação**: Múltiplos algoritmos no mesmo dataset
   - **Baseline**: Nosso ponto de referência

3. **Estudos Recentes com Deep Learning:**
   - CNNs: 95-98% acurácia
   - MLPs: 93-96% acurácia
   - **Nossa expectativa**: 94-97% acurácia

**Modelos de Comparação no Projeto:**

1. **Dummy Classifier**: Baseline simples (classe majoritária)
2. **Logistic Regression**: Baseline linear clássico
3. **Keras Padrão**: Rede neural sem otimização
4. **Grid Search**: Rede neural otimizada

**Métricas de Avaliação:**
- **Acurácia**: Métrica principal
- **Precision**: Importante para reduzir falsos positivos
- **Recall**: Crítico para não perder casos malignos
- **F1-Score**: Balanceio entre precision e recall
- **AUC-ROC**: Avaliação independente do threshold

### 5.4 Estratégia de Validação

**Validação Cruzada Estratificada (5-fold)**
- Mantém proporção das classes em cada fold
- Reduz variância das estimativas
- Uso eficiente dos dados limitados

**Grid Search para Hiperparâmetros:**
- Learning rate: [0.001, 0.01, 0.1]
- Batch size: [16, 32, 64]
- Epochs: Early stopping com patience
- Otimizador: Adam vs RMSprop

---

## 6. EXPECTATIVAS E PRÓXIMOS PASSOS

### 6.1 Resultados Esperados
- **Acurácia**: 94-97%
- **Recall para Malignos**: >95% (crítico clinicamente)
- **Precision**: >90% (reduzir falsos alarmes)

### 6.2 Contribuições do Projeto
- Comparação sistemática de abordagens
- Implementação reproduzível
- Interface Streamlit para demonstração
- Documentação completa do processo

### 6.3 Limitações Reconhecidas
- Dataset relativamente pequeno
- Dados de uma única instituição
- Falta de validação externa
- Ausência de features clínicas adicionais

---

**Este roteiro fornece a base sólida para a apresentação da Parte 1, demonstrando compreensão técnica profunda e justificativas bem fundamentadas para cada decisão do projeto.**