# - Predição de Preços do Bitcoin com PyCaret e FastAPI

Este README descreve um código Python que utiliza a biblioteca PyCaret para criar um modelo de regressão e o framework FastAPI para criar uma API de predição de preços de fechamento das ações do Bitcoin. O código carrega um modelo previamente treinado e permite que os usuários façam previsões com base em dados fornecidos via API.

## Pré-requisitos
Antes de executar este código, você precisará ter instalado os seguintes componentes:

- Python: Certifique-se de ter uma versão do Python instalada em seu sistema.
- Instale as dependencias contidas no arquivo requirements.txt com o seguinte comando: `pip install -r requirements.txt`
- PyCaret: Uma biblioteca de aprendizado de máquina automatizada (AutoML) que facilita a criação de modelos de aprendizado de máquina.
- FastAPI: Um framework web rápido para criar APIs com Python. Você pode instalá-lo usando 
- Uvicorn: Um servidor ASGI para executar a aplicação FastAPI. Você pode instalá-lo usando 

## Uso do Código
Siga as etapas abaixo para executar o código e fazer previsões de preços do Bitcoin:

1. Certifique-se de que os pré-requisitos estejam instalados em seu ambiente.

2. Baixe o código e salve-o em um arquivo Python, por exemplo, `bitcoin_prediction.py`.
3. Baixe a base de dados correspondente em: `https://www.kaggle.com/datasets/jkraak/bitcoin-price-dataset`

4. Certifique-se de ter um modelo de regressão treinado pelo PyCaret e salvo em um arquivo chamado "bitcoin_models". Você pode treinar um modelo usando o PyCaret ou substituir esse arquivo por um modelo pré-treinado de sua escolha.

5. Execute o código usando o seguinte comando:
   ```
   python bitcoin_prediction.py
   ```

6. A API FastAPI estará disponível em `http://127.0.0.1:8000`. Você pode acessar a documentação da API em `http://127.0.0.1:8000/docs` para obter detalhes sobre como fazer solicitações.

7. Para fazer previsões, faça uma solicitação POST para `http://127.0.0.1:8000/predict` com os dados do Bitcoin no corpo da solicitação no formato JSON. Os campos obrigatórios são: `open`, `high`, `low`, `volume`, `number_of_trades`, `taker_buy_base_asset_volume`, `taker_buy_quote_asset_volume`.

   Exemplo de solicitação em Python:
   ```python
   import requests

   data = {
       "open": 60000.0,
       "high": 61000.0,
       "low": 59000.0,
       "volume": 50000.0,
       "number_of_trades": 1000.0,
       "taker_buy_base_asset_volume": 30000.0,
       "taker_buy_quote_asset_volume": 1800000.0
   }

   response = requests.post("http://127.0.0.1:8000/predict", json=data)
   result = response.json()

   print("Previsão de Preço do Bitcoin:", result["prediction"])
   ```
