from flask import Flask

app = Flask("passcrack_backend")

@app.route("/")
def home():
    return "hello world"

app.run()