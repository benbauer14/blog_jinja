from flask import Flask, render_template
import random
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    year = datetime.date.today().year
    randomNumber = random.randint(1,10)
    return render_template("index.html", randomNumber=randomNumber, year=year)

if __name__ == "__main__":
    app.run(debug=True)