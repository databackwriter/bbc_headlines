from flask import Flask, jsonify
from app.scraper import fetch_bbc_headlines

app = Flask(__name__)

@app.route("/headlines", methods=["GET"])
def headlines():
    try:
        headlines = fetch_bbc_headlines()
        return jsonify({"headlines": headlines})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/actuator/health", methods=["GET"])
def health():
    return {"status": "UP"}, 200

if __name__ == "__main__":
    app.run(debug=True, port=5000)
