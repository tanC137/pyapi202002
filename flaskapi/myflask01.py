#!/usr/bin/python3

## import Flask class from flask library
from flask import Flask

## always written at the top
app = Flask(__name__)

## @ is a decorator
# this describes WHEN the code should run
@app.route("/")
def hello_world():
    return "HELLO WORLD!"

@app.route("/hello/<name>")
def hello_user(name):
    return f"Hello {name}"

if __name__ == "__main__":
    app.run(port=5006)
