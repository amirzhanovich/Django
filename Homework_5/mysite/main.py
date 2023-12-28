import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/exchange_parcing")
def exchange_parcing():
    # proxies = {
    #     'http': 'proxy.server:3128',
    #     'https': 'proxy.server:3128',
    # }
    #
    # response_usd = requests.get('https://finance.rambler.ru/calculators/converter/1-USD-KZT/', proxies=proxies)
    # soup_usd = BeautifulSoup(response_usd.text, "html.parser")
    # exchange_to_usd = soup_usd.find('span', class_="_2-g7-").text
    #
    # response_eur = requests.get('https://finance.rambler.ru/calculators/converter/1-EUR-KZT/', proxies=proxies)
    # soup_eur = BeautifulSoup(response_eur.text, "html.parser")
    # exchange_to_eur = soup_eur.find('span', class_="_2-g7-").text
    #
    # response_rub = requests.get('https://finance.rambler.ru/calculators/converter/1-RUB-KZT/', proxies=proxies)
    # soup_rub = BeautifulSoup(response_rub.text, "html.parser")
    # exchange_to_rub = soup_rub.find('span', class_="_2-g7-").text
    #
    # response_cny = requests.get('https://finance.rambler.ru/calculators/converter/1-CNY-KZT/', proxies=proxies)
    # soup_cny = BeautifulSoup(response_cny.text, "html.parser")
    # exchange_to_cny = soup_cny.find('span', class_="_2-g7-").text

    bot_token = "6714990097:AAHcQjprc_VMYp1CWo2NDSo0tgCxo7W4no4"
    users = '494266800'  # 494266800(amirzhanovich)

    currency_info = ["1 USD = 457,6307 KZT", "1 EUR = 504,5924 KZT", "1 RUB = 4,9901 KZT", "1 CNY = 63,8424 KZT"]
    # currency_info = [exchange_to_usd, exchange_to_eur, exchange_to_rub, exchange_to_cny]

    for user in [str(x).strip() for x in users.split(',')]:
        for info in currency_info:
            response = requests.get(f'https://api.telegram.org/bot{bot_token}/sendMessage',
                                    params={'chat_id': user, 'text': info})
            if response.status_code == 200:
                json_response = response.json()
            else:
                print(f"Failed to send message to user {user}. Status code: {response.status_code}")

    return render_template('exchange_parcing.html', currency_info=currency_info)

