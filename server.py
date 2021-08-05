from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    year = datetime.date.today().year
    randomNumber = random.randint(1,10)
    return render_template("index.html", randomNumber=randomNumber, year=year)

@app.route("/guess/<name>")
def guess(name):
    genderdata = requests.get(f"https://api.genderize.io?name={name}")
    gender = genderdata.json()
    agedata = requests.get(f"https://api.agify.io?name={name}")
    age = agedata.json()
    return render_template("guess.html", name=name, myage=age["age"], probability=gender["probability"], gender=gender["gender"])

if __name__ == "__main__":
    app.run(debug=True)