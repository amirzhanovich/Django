import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/weather")
def weather():
    response = requests.get('https://www.meteoprog.com/ru/weather/Astana/')
    soup = BeautifulSoup(response.text, "html.parser")
    temperature = soup.find('div', class_="today-temperature").find('span').text

    return render_template('weather.html', temperature=temperature)

@app.route("/exchange_parcing")
def exchange_parcing():
    response_usd = requests.get('https://finance.rambler.ru/calculators/converter/1-USD-KZT/')
    soup_usd = BeautifulSoup(response_usd.text, "html.parser")
    exchange_to_usd = soup_usd.find('span', class_="_2-g7-").text

    response_eur = requests.get('https://finance.rambler.ru/calculators/converter/1-EUR-KZT/')
    soup_eur = BeautifulSoup(response_eur.text, "html.parser")
    exchange_to_eur = soup_eur.find('span', class_="_2-g7-").text

    response_rub = requests.get('https://finance.rambler.ru/calculators/converter/1-RUB-KZT/')
    soup_rub = BeautifulSoup(response_rub.text, "html.parser")
    exchange_to_rub = soup_rub.find('span', class_="_2-g7-").text

    response_cny = requests.get('https://finance.rambler.ru/calculators/converter/1-CNY-KZT/')
    soup_cny = BeautifulSoup(response_cny.text, "html.parser")
    exchange_to_cny = soup_cny.find('span', class_="_2-g7-").text

    return render_template('exchange_parcing.html', exchange_to_usd=exchange_to_usd,
                                                    exchange_to_eur=exchange_to_eur,
                                                    exchange_to_rub=exchange_to_rub,
                                                    exchange_to_cny=exchange_to_cny,
                                                    )

@app.route("/exchange_api")
def exchange_api():
    data = requests.get('https://www.cbr-xml-daily.ru/latest.js').json()
    exchange_to_kzt = data['rates']['KZT']
    exchange_to_usd = data['rates']['USD']
    exchange_to_eur = data['rates']['EUR']
    exchange_to_cny = data['rates']['CNY']

    return render_template('exchange_api.html', exchange_to_kzt=exchange_to_kzt,
                                                exchange_to_usd=exchange_to_usd,
                                                exchange_to_eur=exchange_to_eur,
                                                exchange_to_cny=exchange_to_cny
                                                )


