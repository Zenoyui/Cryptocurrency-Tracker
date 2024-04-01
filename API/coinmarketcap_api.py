# coinmarketcap_api.py
import requests
from utils import config
from tqdm import tqdm
import time

def get_crypto_data():
    # Загрузка конфигурационных параметров, включая API ключ
    api_key = config.COINMARKETCAP_API_KEY
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

    # Формирование параметров запроса
    parameters = {
        'start':'1',
        'limit':'10',
        'convert':'USD'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key,
    }

    # Отправка запроса и обработка ответа
    response = requests.get(url, headers=headers, params=parameters)
    if response.status_code == 200:
        data = response.json()
        # Добавляем Litecoin к списку криптовалют
        for crypto in tqdm(data['data'], desc='Загрузка данных с CoinMarketCap', ncols=100):
            print(f"Запрос для {crypto['symbol']}...")
            if crypto['symbol'] == 'LTC':  # Проверяем, что это Litecoin
                continue
            elif crypto['symbol'] in ['ETH', 'XRP', 'BCH', 'ADA', 'DOT']:  # Добавляем еще 5 популярных криптовалют
                new_crypto_data = requests.get(f"https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol={crypto['symbol']}&convert=USD&CMC_PRO_API_KEY={api_key}")
                new_crypto_data = new_crypto_data.json()
                if 'data' in new_crypto_data:
                    data['data'].append(new_crypto_data['data'][crypto['symbol']])
                else:
                    print(f"Ошибка при получении данных для {crypto['symbol']}: {new_crypto_data}")
        time.sleep(1)  # Добавляем небольшую задержку для имитации обработки данных
        return data['data']
    else:
        print("Ошибка при получении данных:", response.status_code)
        return None

# Пример использования
if __name__ == "__main__":
    crypto_data = get_crypto_data()
    print(crypto_data)
