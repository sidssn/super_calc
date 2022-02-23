from flask import Flask, session
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World! This is done by azure pipelines"

@app.route("/logout")
def logout():
    session.clear()
    return "Logout success!"
