from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Congratulations, it's a web app!

if __name__ == "__main__":
    app.run(port=8080)"
