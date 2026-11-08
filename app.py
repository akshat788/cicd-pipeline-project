from flask import Flask, jsonify

app = Flask(__name__)


def add(a, b):
    """Pure function: easy to unit test."""
    return a + b


@app.route("/")
def home():
    return jsonify(message="Hello from the CI/CD pipeline!", version="1.0.0")


@app.route("/health")
def health():
    # Health endpoint: used later to verify the deployed container is alive
    return jsonify(status="ok")


@app.route("/add/<int:a>/<int:b>")
def add_route(a, b):
    return jsonify(result=add(a, b))


if __name__ == "__main__":
    # 0.0.0.0 lets the app be reached from outside a Docker container later
    app.run(host="0.0.0.0", port=5000)