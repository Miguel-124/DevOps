from flask import Flask, jsonify
import requests

app = Flask(__name__)

COIN_API_URL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"

@app.route("/")
def home():
    return "Welcome to the Crypto Tracker API!"

@app.route("/prices")
def get_prices():
    try:
        response = requests.get(COIN_API_URL)
        data = response.json()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)