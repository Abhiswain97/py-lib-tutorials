from flask import Flask, render_template, request, redirect, url_for, flash

import pymongo
from pymongo import MongoClient


app = Flask(__name__)
app.secret_key = "123"


def send(name, score):
    client = pymongo.MongoClient(
        "mongodb+srv://abhishek:abcd@cluster0.inxuz.mongodb.net/test?retryWrites=true&w=majority",
    )

    print(name, score)

    db = client.test
    collection = db.test

    collection.insert_one({"name": name, "score": score})

    print("Data sent")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/data", methods=["GET", "POST"])
def get_data():
    if request.method == "POST":
        name = request.form.get("name")
        score = request.form.get("score")

        send(name, score)

        flash(f"Data sent to database with name: {name} & score: {score}")

        return redirect(url_for("home"))
    else:
        return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
