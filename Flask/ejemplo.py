from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "¡I am the Senate!"

app.run(host='0.0.0.0')
