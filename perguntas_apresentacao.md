# Possíveis Perguntas da Apresentação
## Projeto: Classificação de Câncer de Mama com Redes Neurais

---

## 📚 PERGUNTAS CONCEITUAIS BÁSICAS

### **Q1: Por que escolheram redes neurais ao invés de algoritmos mais simples como SVM ou Random Forest?**
**R:** Testamos múltiplos algoritmos como baseline. Redes neurais oferecem:
- Capacidade de aprender padrões não-lineares complexos
- Flexibilidade na arquitetura
- Capacidade de generalização com regularização adequada
- Performance superior aos baselines (96.5% vs 95.1% da regressão logística)

### **Q2: Como vocês garantem que o modelo não está apenas "decorando" os dados (overfitting)?**
**R:** Implementamos múltiplas técnicas anti-overfitting:
- **Dropout (0.3)** em camadas ocultas
- **Validação cruzada 5-fold** estratificada
- **Train/Test split** rigoroso (80/20)
- **Early stopping** durante treinamento
- **Regularização L2** nos hiperparâmetros

### **Q3: O que significa "supervisionado" e por que não usaram aprendizado não-supervisionado?**
**R:** 
- **Supervisionado:** Temos labels conhecidos (B/M) para treinar
- **Não-supervisionado (clustering):** Seria inadequado pois:
  - Já conhecemos as classes (benigno/maligno)
  - Não queremos "descobrir" grupos, queremos predizer classes conhecidas
  - Objetivo é classificação, não exploração de padrões

---

## 🔬 PERGUNTAS TÉCNICAS SOBRE DADOS

### **Q4: Como vocês lidam com o desbalanceamento das classes (62.7% vs 37.3%)?**
**R:** 
- **Razão 1.7:1** não é crítica (< 3:1)
- Usamos **stratified sampling** para manter proporções
- Métricas balanceadas: **F1-score, Precision, Recall**
- Foco no **Recall** para casos malignos (mais crítico clinicamente)

### **Q5: Por que usar todas as 30 features? Não seria melhor fazer seleção de features?**
**R:** Decisão baseada em:
- **Redes neurais são robustas** à alta dimensionalidade
- **Features "redundantes"** podem ter valor em combinação
- **Regularização (dropout)** previne overfitting
- **Benchmark** com literatura existente
- **30 features** ainda é dimensionalidade gerenciável

### **Q6: Como vocês validaram a qualidade dos dados originais?**
**R:**
- **Fonte credível:** University of Wisconsin, >1000 citações
- **Análise de completude:** 0 dados faltantes nas features relevantes
- **Análise de outliers:** Mantidos por relevância clínica
- **Consistência:** Padrão uniforme de coleta
- **Reprodutibilidade:** Dataset público no Kaggle

### **Q7: Por que normalização é obrigatória neste caso?**
**R:**
- **Escalas muito diferentes:** area (100s-1000s) vs smoothness (0.05-0.16)
- **Sem normalização:** Features com maior escala dominam o aprendizado
- **StandardScaler:** Padroniza média=0, desvio=1
- **Melhora convergência** e estabilidade do treinamento

---

## 🏗️ PERGUNTAS SOBRE ARQUITETURA

### **Q8: Por que 64 e 32 neurônios especificamente? Testaram outras configurações?**
**R:**
- **64:** ~2x número de features de entrada (regra empírica)
- **32:** Redução gradual para compressão de informação
- **Grid Search** testou outras configurações
- **Baseado em literatura:** Arquiteturas similares para dados tabulares
- **Balanceio:** Capacidade vs simplicidade

### **Q9: Por que ReLU e não outras funções de ativação como tanh ou sigmoid?**
**R:**
- **ReLU vantagens:**
  - Evita vanishing gradient
  - Computacionalmente eficiente
  - Cria esparsidade (alguns neurônios inativos)
  - Estado da arte atual
- **Testamos outras:** Desempenho inferior no Grid Search

### **Q10: Por que Sigmoid na saída e não Softmax?**
**R:**
- **Classificação binária:** Sigmoid suficiente (0-1)
- **Softmax:** Para múltiplas classes (>2)
- **Interpretabilidade:** Output como probabilidade
- **Compatibilidade:** Funciona com binary_crossentropy

### **Q11: Como definiram a taxa de Dropout (0.3)?**
**R:**
- **Valores testados:** 0.1, 0.2, 0.3, 0.5 no Grid Search
- **0.3 = 30%:** Balanceio entre regularização e capacidade
- **Literatura:** Valores entre 0.2-0.5 são comuns
- **Validação empírica:** Melhor performance na validação cruzada

---

## 📊 PERGUNTAS SOBRE VALIDAÇÃO E MÉTRICAS

### **Q12: Por que Recall é mais importante que Precision neste contexto?**
**R:**
- **Contexto médico:** Pior perder um caso maligno (falso negativo)
- **Recall alto (97.8%):** Detectamos 97.8% dos casos malignos
- **Custo diferente:** Falso negativo = diagnóstico perdido (grave)
- **Falso positivo:** Exames adicionais (menos grave)

### **Q13: Como interpretam a matriz de confusão dos resultados?**
**R:**
- **True Negative (68):** Corretamente identificou benignos
- **True Positive (42):** Corretamente identificou malignos  
- **False Positive (3):** Benignos classificados como malignos
- **False Negative (1):** Maligno classificado como benigno
- **Resultado excelente:** Apenas 1 caso maligno perdido

### **Q14: Por que validação cruzada 5-fold e não 10-fold?**
**R:**
- **Dataset pequeno (569):** 5-fold dá splits maiores
- **Stratified:** Mantém proporção das classes
- **Balanceio:** Variance vs bias das estimativas
- **Computacionalmente eficiente** para Grid Search
- **Literatura:** 5-fold adequado para datasets deste tamanho

### **Q15: Como comparam com benchmarks da literatura científica?**
**R:**
- **Street et al. (1993):** 97.5% (linear programming)
- **Estudos recentes:** 93-98% (diversos algoritmos)
- **Nosso resultado:** 96.5% dentro da faixa esperada
- **Diferencial:** Metodologia reproduzível com validação rigorosa

---

## 🎯 PERGUNTAS SOBRE APLICAÇÃO PRÁTICA

### **Q16: Este modelo poderia ser usado em produção real?**
**R:**
- **Limitações atuais:**
  - Dataset de uma única instituição
  - Falta validação externa
  - Ausência de dados clínicos adicionais
- **Próximos passos necessários:**
  - Validação multicêntrica
  - Dados de diferentes populações
  - Interface médica adequada
  - Aprovação regulatória

### **Q17: Como explicariam os resultados para um médico?**
**R:**
- **Recall 97.8%:** "Detectamos 98 de cada 100 casos malignos"
- **Precision 95.2%:** "95% dos casos que marcamos como malignos realmente são"
- **Suporte à decisão:** Não substitui, mas auxilia o médico
- **Segunda opinião:** Ferramenta adicional de diagnóstico

### **Q18: Quais são os principais riscos/limitações do modelo?**
**R:**
- **Viés populacional:** Dados de uma única instituição
- **Fatores não incluídos:** Idade, histórico familiar, genética
- **Black box:** Dificulta interpretabilidade clínica
- **Drift:** Performance pode degradar com tempo
- **Dependência técnica:** Requer infraestrutura adequada

---

## 🔄 PERGUNTAS SOBRE PROCESSO E METODOLOGIA

### **Q19: Como garantem a reprodutibilidade do experimento?**
**R:**
- **Seeds fixas:** SEED = 42 em todas as operações aleatórias
- **Versões específicas:** Python 3.11.5, TensorFlow, etc.
- **Requirements.txt:** Todas as dependências documentadas
- **Código versionado:** GitHub com histórico completo
- **Documentação:** README detalhado

### **Q20: Se fossem fazer novamente, o que mudariam?**
**R:**
- **Dataset maior:** Buscar bases multicêntricas
- **Feature engineering:** Explorar interações entre features
- **Explicabilidade:** Implementar SHAP/LIME desde o início
- **Ensembles:** Combinar múltiplos modelos
- **Validação temporal:** Se houvesse dados longitudinais

### **Q21: Como escolheram os hiperparâmetros para o Grid Search?**
**R:**
- **Literatura:** Valores comuns em papers similares
- **Experiência prévia:** Projetos anteriores da equipe
- **Recursos computacionais:** Limitações de tempo/hardware
- **Análise exploratória:** Testes preliminares orientaram escolhas

---

## 💡 PERGUNTAS CONCEITUAIS AVANÇADAS

### **Q22: Como lidariam com concept drift em produção?**
**R:**
- **Monitoramento contínuo:** Métricas de performance
- **Retreinamento periódico:** Com novos dados
- **Detecção de drift:** Comparação distribuições
- **Versionamento de modelos:** Rollback se necessário

### **Q23: Por que não usaram técnicas de ensemble learning?**
**R:**
- **Escopo do projeto:** Foco em metodologia de RN
- **Complexidade:** Aumentaria dificuldade de interpretação
- **Performance:** Rede neural já atingiu objetivo
- **Próximos passos:** Consideraríamos em versões futuras

### **Q24: Como abordariam a questão ética de IA em medicina?**
**R:**
- **Transparência:** Médicos devem entender limitações
- **Responsabilidade:** IA auxilia, médico decide
- **Viés:** Validação em populações diversas
- **Consentimento:** Pacientes sabem sobre uso de IA
- **Auditabilidade:** Decisões devem ser rastreáveis

---

## 🎓 PERGUNTAS PARA APROFUNDAMENTO

### **Q25: Quais outras arquiteturas poderiam ser testadas?**
**R:**
- **Autoencoders:** Para detecção de anomalias
- **Attention mechanisms:** Para identificar features importantes
- **Graph Neural Networks:** Se houvesse dados relacionais
- **Transfer Learning:** De modelos pré-treinados

### **Q26: Como avaliariam a importância das features individualmente?**
**R:**
- **Correlation analysis:** Já implementado
- **Permutation importance:** Sklearn
- **SHAP values:** Explicabilidade local/global
- **Feature ablation:** Remover e medir impacto
- **Gradient-based methods:** Para redes neurais

### **Q27: Como adaptar para outros tipos de câncer?**
**R:**
- **Transfer learning:** Usar camadas pré-treinadas
- **Fine-tuning:** Ajustar última camada
- **Feature engineering:** Adaptar para novo domínio
- **Validação cruzada:** Entre tipos de câncer
- **Multi-task learning:** Múltiplos cânceres simultaneamente

---

## 📋 DICAS PARA RESPONDER BEM

1. **Seja honesto sobre limitações**
2. **Cite literatura quando relevante**
3. **Explique o raciocínio por trás das decisões**
4. **Use exemplos práticos quando possível**
5. **Conecte aspectos técnicos com impacto clínico**
6. **Mostre que consideram o contexto médico**
7. **Demonstre pensamento crítico sobre o próprio trabalho**

---

*Este documento serve como preparação para possíveis questionamentos durante a apresentação. Pratiquem as respostas, mas mantenham naturalidade e honestidade intelectual.*