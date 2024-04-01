# crypto_tracker.py

from api import coinmarketcap_api
from graphics import plots
from notifications import notifier
from utils import config

def main():
    # Получаем данные о ценах криптовалют
    crypto_data = coinmarketcap_api.get_crypto_data()

    # Визуализируем данные
    plots.plot_prices(crypto_data)

    # Проверяем наличие значительных изменений цен и отправляем уведомления
    significant_changes = notifier.check_for_significant_changes(crypto_data)
    if significant_changes:
        notifier.send_notification(significant_changes)

if __name__ == "__main__":
    main()
