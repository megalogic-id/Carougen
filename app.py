import os
from flask import Flask, render_template, request
from module import generate

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate-content", methods=["POST"])
def generate_content():
    # Get the text entered in the input field
    input_text = request.form.get("text")
    print(input_text)

    # Generate content based on input_text using your existing generate function
    generated_content = generate(input_text)

    return generated_content


if __name__ == "__main__":
    app.run(debug=True,
            host="0.0.0.0",
            port=int(os.environ.get("PORT", 8080)))
