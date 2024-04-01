# notifier.py

def check_for_significant_changes(crypto_data):
    significant_changes = []

    # Проверяем цены криптовалют и находим те, у которых цена изменилась более чем на 10%
    for crypto in crypto_data:
        price_change = float(crypto['quote']['USD']['percent_change_24h'])
        if abs(price_change) > 10.0:
            significant_changes.append(crypto)

    return significant_changes

def send_notification(significant_changes):
    if significant_changes:
        print("Обнаружены значительные изменения цен на следующие криптовалюты:")
        for crypto in significant_changes:
            name = crypto['name']
            price_change = float(crypto['quote']['USD']['percent_change_24h'])
            print(f"{name}: {price_change:.2f}%")
    else:
        print("На рынке криптовалют нет значительных изменений цен.")

# Пример использования
if __name__ == "__main__":
    # Пример данных о криптовалютах (можно заменить на реальные данные)
    example_crypto_data = [
        {'name': 'Bitcoin', 'quote': {'USD': {'percent_change_24h': '5.0'}}},
        {'name': 'Ethereum', 'quote': {'USD': {'percent_change_24h': '-12.5'}}},
        {'name': 'Ripple', 'quote': {'USD': {'percent_change_24h': '15.3'}}}
    ]

    # Проверка наличия значительных изменений и отправка уведомлений
    significant_changes = check_for_significant_changes(example_crypto_data)
    send_notification(significant_changes)
