# FarmTech Solutions:
**Previsão do Tempo e Cálculo de Insumos para Plantio**

Este projeto integra duas funcionalidades principais:

1. **Previsão do tempo**: A consulta a uma API para obter a previsão do tempo atual e a previsão horária de temperatura para uma localização específica (São Paulo).
2. **Cálculo de insumos**: Cálculo da quantidade necessária de insumos (fertilizante ou fosfato) para plantios de milho e soja, com base na área do terreno informado pelo usuário.

## Funcionalidades

### Previsão do Tempo
- O projeto consulta a API **Open Meteo** para obter a previsão do tempo atual e a temperatura horária para a localização de São Paulo.
- Utiliza a linguagem **R** para realizar a consulta à API e processar a resposta.

### Cálculo de Insumos
- Permite ao usuário informar os dados de plantio para culturas de **Milho** (terreno retangular) ou **Soja** (terreno circular).
- Calcula a quantidade necessária de insumos com base na área do terreno (em metros quadrados).
- Os insumos utilizados são:
  - **Milho**: Fertilizante (100 litros/m²)
  - **Soja**: Fosfato (600 litros/m²)

### Funcionalidades do Menu:
- **Informar Dados**: Permite informar os dados do plantio.
- **Resgatar Dados**: Exibe os dados armazenados do plantio.
- **Alterar Dados**: Permite atualizar os dados armazenados.
- **Deletar Dados**: Deleta os dados armazenados.
- **Consultar Previsão do Tempo**: Consulta a previsão do tempo utilizando a API Open Meteo.

## Como Usar

### Requisitos
- **Python 3.x** para executar o código de cálculo de insumos.
- **R** instalado no seu sistema para a consulta à API da previsão do tempo.
- Bibliotecas Python necessárias: `math`, `subprocess`, `sys`.

### Instalação das Dependências R
Certifique-se de que as bibliotecas necessárias estão instaladas em R:

```r
install.packages("httr")
install.packages("jsonlite")
install.packages("rlang")


project/
├── previsao_do_tempo.r    # Script R para consulta à API de previsão do tempo
├── main.py                # Código principal em Python
└── README.md              # Este arquivo


