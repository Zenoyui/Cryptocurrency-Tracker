# plots.py
import matplotlib.pyplot as plt

def plot_prices(crypto_data):
    # Извлечение данных о ценах криптовалют
    names = [crypto['name'] for crypto in crypto_data]
    prices = [float(crypto['quote']['USD']['price']) for crypto in crypto_data]

    # Создание графика
    plt.figure(figsize=(10, 6))
    plt.bar(names, prices, color='blue')

    # Настройка осей и заголовка графика
    plt.xlabel('Криптовалюта')
    plt.ylabel('Цена (USD)')
    plt.title('Цены на криптовалюты')

    # Поворот названий криптовалют для лучшей читаемости
    plt.xticks(rotation=45, ha='right')

    # Отображение графика
    plt.tight_layout()
    plt.show()

# Пример использования
if __name__ == "__main__":
    # Пример данных о криптовалютах (можно заменить на реальные данные)
    example_crypto_data = [
        {'name': 'Bitcoin', 'quote': {'USD': {'price': '50000'}}},
        {'name': 'Ethereum', 'quote': {'USD': {'price': '2000'}}},
        {'name': 'Ripple', 'quote': {'USD': {'price': '1.5'}}}
    ]

    # Создание графика цен криптовалют
    plot_prices(example_crypto_data)
