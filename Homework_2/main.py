from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/pricing")
def pricing():

    json_file_path = 'static/prices.json'
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    print(data)

    old_data = data["data"]
    print(type(old_data), old_data)
    new_data = sorted(old_data, key=lambda x: x["name"])

    for i in new_data:
        print(i)

    return render_template('pricing.html', new_data=new_data)


@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/signup")
def signup():
    return render_template('signup.html')

@app.route("/details")
def details():
    return render_template('details.html')

