#!/usr/bin/python3
"""Script that start a Flask web application
listening on 0.0.0.0, port 5000
"""
from flask import Flask, render_template

app = Flask("__name__")


@app.route('/', strict_slashes=False)
def hello():
    """Return a given string hello"""
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """"Return a given string"""
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def cText(text):
    """Return C followed by the value of the text"""
    return ("C {}".format(text.replace("_", " ")))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythonText(text="is cool"):
    """Return Python followed by the value of the text"""
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def isNumber(n):
    """display “n is a number” only if n is an integer"""
    if isinstance(n, int):
        return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """display a HTML page only if n is an integer"""
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    is_even = n % 2 == 0
    """Return even or odd"""
    return render_template('6-number_odd_or_even.html', n=n, is_even=is_even)


if __name__ == "__main__":
    app.run()
