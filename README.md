# 🧠 Projeto de Disciplina - Redes Neurais com TensorFlow

<div align="center">
  <img src="imagens/Modelos-Instagram-Infnet.png" alt="Instituto Infnet" height="80"/>
</div>

<img src="https://img.shields.io/badge/python-v3.11.5-blue?style=flat-square&logo=python&logoColor=white" alt="Python Version" height="25"/>
<img src="https://img.shields.io/badge/jupyter-v5.7.2-blue?style=flat-square&logo=jupyter&logoColor=white" alt="Jupyter Version" height="25"/>
<img src="https://img.shields.io/badge/anaconda-v23.7.4-blue?style=flat-square&logo=anaconda&logoColor=white" alt="Anaconda Version" height="25"/>
<img src="https://img.shields.io/badge/tensorflow-2.20.0-orange?style=flat-square&logo=tensorflow&logoColor=white" alt="TensorFlow Version" height="25"/>
<img src="https://img.shields.io/badge/scikit--learn-1.7.1-orange?style=flat-square&logo=scikit-learn&logoColor=white" alt="Scikit-learn Version" height="25"/>
<img src="https://img.shields.io/badge/pandas-2.3.2-blue?style=flat-square&logo=pandas&logoColor=white" alt="Pandas Version" height="25"/>

## 📋 Sobre o Projeto

Este projeto implementa um modelo de **aprendizagem supervisionada** para **classificação binária** utilizando dados relacionados ao **Câncer de Mama**. O objetivo principal é desenvolver e comparar diferentes modelos de redes neurais usando TensorFlow/Keras para predizer se um tumor é maligno ou benigno.

### 🎯 Objetivos

- ✅ Implementar modelos de classificação binária para diagnóstico de câncer de mama
- ✅ Realizar análise exploratória de dados (EDA) completa
- ✅ Aplicar técnicas de pré-processamento e normalização de dados
- ✅ Desenvolver modelos baseline e otimizados com Grid Search
- ✅ Comparar performance entre diferentes arquiteturas de redes neurais
- ✅ Validar modelos usando validação cruzada

## 📊 Dataset

### 🔗 Fonte dos Dados
Os dados são obtidos diretamente do **Kaggle** através da API:
- **Dataset**: [Breast Cancer Dataset](https://www.kaggle.com/datasets/wasiqaliyasir/breast-cancer-dataset)
- **Registros**: 569 amostras
- **Features**: 32 características (30 numéricas + 1 target + 1 ID)
- **Classes**: Benigno (B) / Maligno (M)

### 📈 Características do Dataset
- Dados completamente numéricos (exceto target)
- Sem valores ausentes
- Features baseadas em características de imagem de núcleos celulares
- Distribuição de classes: ~63% Benignos, ~37% Malignos

## 🗂️ Estrutura do Projeto

```
pd-infnet-rnn/
├── 📊 data/
│   └── 01-raw/                    # Dados brutos do Kaggle
├── 📓 rnn-project.ipynb          # Notebook principal
├── 📋 requirements.txt           # Dependências do projeto
├── 📝 README.md                  # Documentação do projeto
├── 🎯 apresentacao_*.html        # Apresentações do projeto
├── 📋 considerações.md           # Considerações do projeto
├── ❓ perguntas_apresentacao.md  # FAQ da apresentação
└── 📖 roteiro_apresentacao_*.md  # Roteiros das apresentações
```

## 🔧 Configuração do Ambiente

### 🐍 Pré-requisitos
- Python 3.11.5+
- Anaconda ou Miniconda (recomendado)
- Git

### 🚀 Passo a Passo da Instalação

#### 1️⃣ Clone o Repositório
```bash
git clone <url-do-repositorio>
cd pd-infnet-rnn
```

#### 2️⃣ Criar Ambiente Virtual

##### Opção A: Com Anaconda (Recomendado)
```bash
# Criar ambiente virtual
conda create --name rnn-project python=3.11.5

# Ativar ambiente
conda activate rnn-project
```

##### Opção B: Com venv
```bash
# Criar ambiente virtual
python -m venv rnn-project

# Ativar ambiente (Windows)
rnn-project\Scripts\activate

# Ativar ambiente (Linux/Mac)
source rnn-project/bin/activate
```

#### 3️⃣ Instalar Dependências
```bash
# Atualizar pip
pip install --upgrade pip

# Instalar dependências do projeto
pip install -r requirements.txt
```

#### 4️⃣ Configurar API do Kaggle

##### Método 1: Arquivo de Credenciais
1. Acesse [Kaggle Account Settings](https://www.kaggle.com/account)
2. Clique em "Create New API Token"
3. Salve o arquivo `kaggle.json` em:
   - **Windows**: `C:\Users\<username>\.kaggle\kaggle.json`
   - **Linux/Mac**: `~/.kaggle/kaggle.json`

##### Método 2: Variáveis de Ambiente
```bash
# Windows
set KAGGLE_USERNAME=seu_username
set KAGGLE_KEY=sua_api_key

# Linux/Mac
export KAGGLE_USERNAME=seu_username
export KAGGLE_KEY=sua_api_key
```

#### 5️⃣ Iniciar Jupyter Notebook
```bash
# Iniciar Jupyter
jupyter notebook

# Ou Jupyter Lab (alternativa moderna)
jupyter lab
```

## 📚 Estrutura do Notebook

O notebook está organizado nas seguintes seções:

### 1. 📦 Importação de Pacotes
Importação de todas as bibliotecas necessárias: TensorFlow, Pandas, Scikit-learn, etc.

### 2. 📥 Download e Leitura dos Dados
Configuração da API Kaggle e download automático do dataset.

### 3. 🔍 Análise Exploratória
- Estatísticas descritivas
- Visualizações dos dados
- Análise de distribuições
- Identificação de padrões

### 4. 🛠️ Tratamento dos Dados
- Remoção de colunas nulas
- Limpeza de dados inconsistentes
- Codificação de variáveis categóricas

### 5. 🔗 Análise de Correlação
Matriz de correlação entre features para identificar multicolinearidade.

### 6. ✂️ Separação de Features
Divisão entre variáveis preditoras (X) e target (y).

### 7. 📏 Normalização
Aplicação de StandardScaler para padronizar as features.

### 8. 🎯 Modelos Baseline
- **8.1** Modelo Dummy (classe majoritária)
- **8.2** Modelo Keras padrão sem otimização

### 9. 🔍 Grid Search com Validação Cruzada
Otimização de hiperparâmetros usando Grid Search e K-Fold.

### 10. 📊 Comparação de Modelos
Análise comparativa de performance entre diferentes modelos.

### 11. 🌐 Interface Streamlit
Desenvolvimento de interface web para deploy do modelo.

## 📊 Principais Bibliotecas Utilizadas

| Biblioteca | Versão | Propósito |
|------------|---------|-----------|
| **TensorFlow** | 2.20.0 | Framework principal para redes neurais |
| **Keras** | 3.11.3 | API de alto nível para deep learning |
| **Scikit-learn** | 1.7.1 | Machine learning e pré-processamento |
| **Pandas** | 2.3.2 | Manipulação e análise de dados |
| **NumPy** | 2.3.2 | Computação científica |
| **Matplotlib** | 3.10.5 | Visualização de dados |
| **Seaborn** | 0.13.2 | Visualizações estatísticas |
| **Kaggle** | 1.7.4.5 | API para download de datasets |

## 🎯 Métricas de Avaliação

O projeto utiliza as seguintes métricas para avaliação dos modelos:

- ✅ **Acurácia**: Percentual de predições corretas
- ✅ **Precisão**: Verdadeiros positivos / (VP + Falsos positivos)
- ✅ **Recall (Sensibilidade)**: Verdadeiros positivos / (VP + Falsos negativos)
- ✅ **F1-Score**: Média harmônica entre precisão e recall
- ✅ **AUC-ROC**: Área sob a curva ROC
- ✅ **Matriz de Confusão**: Visualização de erros de classificação

## 🔬 Metodologia

### 🎲 Reprodutibilidade
- **Seed fixo**: `SEED = 42` para garantir resultados consistentes
- **Divisão estratificada**: Manutenção da proporção de classes
- **Validação cruzada**: K-Fold estratificado para validação robusta

### 🧪 Estratégia de Validação
1. **Divisão inicial**: 80% treino, 20% teste
2. **Validação cruzada**: 5-fold estratificado
3. **Grid Search**: Otimização de hiperparâmetros
4. **Teste final**: Avaliação no conjunto de teste

## 🚀 Execução do Projeto

### 1️⃣ Executar Análise Completa
```bash
# Ativar ambiente virtual
conda activate rnn-project

# Iniciar Jupyter
jupyter notebook

# Abrir rnn-project.ipynb e executar células sequencialmente
```

### 2️⃣ Executar Seções Específicas
O notebook permite execução modular das diferentes etapas:
- EDA isolada
- Apenas treinamento de modelos
- Comparação de resultados
- Interface Streamlit

## 👥 Equipe de Desenvolvimento

- **Mateus Teixeira Ramos da Silva** [![GitHub](https://img.shields.io/badge/Github-151b23?style=flat-square&logo=github)](https://github.com/GitMateusTeixeira/03-ml-modeling)
- **Fabio Ferreira Figueiredo** [![GitHub](https://img.shields.io/badge/Github-151b23?style=flat-square&logo=github)](https://github.com/fabioffigueiredo)
- **Wilson Melo** [![GitHub](https://img.shields.io/badge/Github-151b23?style=flat-square&logo=github)](https://github.com/bakudas)
- **Thiago Vinícius** [![GitHub](https://img.shields.io/badge/Github-151b23?style=flat-square&logo=github)](https://github.com/ubyss)
- **Lauro Barbosa** [![GitHub](https://img.shields.io/badge/Github-151b23?style=flat-square&logo=github)](https://github.com/LMRocha)
- **Felipe Szczpanski** [![GitHub](https://img.shields.io/badge/Github-151b23?style=flat-square&logo=github)](https://github.com/szczpanski)
- **Iata Anderson** [![GitHub](https://img.shields.io/badge/Github-151b23?style=flat-square&logo=github)](https://github.com/AndersonSouza22/)


## 🔧 Solução de Problemas

### ❌ Erro: "No module named 'kaggle'"
```bash
pip install kaggle
```

### ❌ Erro: "Kaggle API credentials not found"
Verifique se o arquivo `kaggle.json` está no local correto ou se as variáveis de ambiente estão configuradas.

### ❌ Erro: "TensorFlow not found"
```bash
pip install tensorflow
```

### ❌ Erro de memória durante treinamento
Reduza o batch_size nos modelos ou utilize:
```python
import os
os.environ['TF_FORCE_GPU_ALLOW_GROWTH'] = 'true'
```

## 📈 Resultados Esperados

O projeto visa alcançar:
- ✅ **Acurácia > 95%** nos dados de teste
- ✅ **Recall > 95%** para detecção de casos malignos
- ✅ **Tempo de treinamento < 5 minutos**
- ✅ **Modelo interpretável** para uso clínico

## 🤝 Contribuições

Para contribuir com o projeto:

1. Fork o repositório
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto é desenvolvido para fins acadêmicos como parte do curso de Pós-graduação do Instituto Infnet.

## 📞 Suporte

Para dúvidas e suporte:
- 📧 **Email**: [adicionar email do grupo]
- 💬 **Issues**: Use o sistema de issues do GitHub
- 📚 **Documentação**: Consulte este README e os comentários no notebook

---

<div align="center">

<img src="imagens/Modelos-Instagram-Infnet.png" alt="Instituto Infnet" height="50"/>**Instituto Infnet - Pós-graduação MIT em Machine Learning, Deep Learning e Inteligência Artificial**  
**📅 Ano: 2025 | 🔬 Disciplina: Redes Neurais com TensorFlow**

</div>