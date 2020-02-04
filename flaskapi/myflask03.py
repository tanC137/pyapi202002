#!/usr/bin/python3

from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route("/admin")
def hello_admin():
    return "Hello admin"

@app.route("/guest/<guestname>")
def hello_guest(guestname):
    return f"Hello {guestname} as guest"

@app.route("/user/<username>")
def hello_user(username):
    if name == "admin"
        #return 302 response to redirect to /admin
        return redirect(url_for("hello_admin"))
    else
        #return 302 response to redirect to /guest/<guestname>
        return redirect(url_for("hello_guest", guestname=username))


if __name__ == "__main__"
    app.run(port=5006, debug = True)
