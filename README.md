# Cryptocurrency Tracker

Welcome to the Cryptocurrency Tracker - an application for monitoring the fluctuations in cryptocurrency prices in real-time.

## Overview

Cryptocurrency Tracker is developed to provide users with up-to-date information regarding cryptocurrency market trends. The application fetches data from CoinMarketCap through their API, visualizes the price changes, and notifies the user of significant market movements.

## Features

- Real-time cryptocurrency price data fetching from CoinMarketCap API.
- Visualization of price data using matplotlib for an intuitive understanding of market trends.
- Notifications for significant price changes, ensuring you don't miss vital market movements.
- Easy to set up and start tracking with a few simple steps.

## Installation

Before you can run the application, some setup is required:

1. Clone the repository to your local machine.
2. Ensure that Python 3.x is installed on your system.
3. Install the required dependencies with pip:

bash
pip install -r requirements.txt

4. Get an API key from [CoinMarketCap](https://coinmarketcap.com/api/) and set it in the 'config.py':

python
COINMARKETCAPAPIKEY = 'yourcoinmarketcapapikeyhere'

Please note: Do NOT share your API key publicly or upload it to public repositories. Always keep your keys confidential.

## Usage

After setting up, you can run the application using:

bash
python crypto_tracker.py

The tracker will display current prices and you will be notified of any significant changes accordingly.

## Contribution

Contributions are welcome! For bug reports or feature requests, please open an issue. If you wish to contribute to the codebase, please consider following the steps:

1. Fork the repository.
2. Create a new branch for your feature.
3. Add or change the code.
4. Write or adapt tests as needed.
5. Push your changes and open a pull request.

## License

This project is provided under the MIT License. Refer to the 'LICENSE' file for the fulltext.

---

*This README is a template and should be customized to fit your project's needs.*