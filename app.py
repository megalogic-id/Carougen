import os
from flask import Flask, render_template, request
from helpers import generate

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("pages/index.html")


@app.route("/generate-content", methods=["POST"])
def generate_content():
    input_text = request.form["text"]
    generated_content = generate(input_text)
    return generated_content


@app.errorhandler(500)
def internal_server_error(error):
    return render_template("pages/500.html"), 500


if __name__ == "__main__":
    app.run(debug=True,
            host="0.0.0.0",
            port=int(os.environ.get("PORT", 8080)))
