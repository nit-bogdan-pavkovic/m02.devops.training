from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to the Flask App!"


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


@app.route("/add", methods=["POST"])
def add():
    data = request.get_json()
    result = data.get("a", 0) + data.get("b", 0)
    return jsonify({"result": result})


@app.route("/subtract", methods=["POST"])
def subtract():
    data = request.get_json()
    result = data.get("a", 0) - data.get("b", 0)
    return jsonify({"result": result})


@app.route("/multiply", methods=["POST"])
def multiply():
    data = request.get_json()
    result = data.get("a", 1) * data.get("b", 1)
    return jsonify({"result": result})


@app.route("/divide", methods=["POST"])
def divide():
    data = request.get_json()
    b = data.get("b", 1)
    if b == 0:
        return jsonify({"error": "Division by zero"}), 400
    result = data.get("a", 0) / b
    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(debug=True)
