from flask import Flask, jsonify

app = Flask(__name__)

APP_VERSION = "1.0"

@app.route("/")
def home():
    return jsonify({
        "message": "Hello from DevOps!",
        "version": APP_VERSION
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)