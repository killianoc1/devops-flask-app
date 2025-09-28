# hello.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return (
        '<p>Hello, World! I am a Flask app!</p>'
        '<p><a href="/about">About this app</a></p>'
        '<p>Welcome!</p>'

    )

@app.route("/about")
def about():
    return (
        '<p>This application is running on the Flask web framework.</p>'
        '<p>Learn more about Flask here: '
        '<a href="https://flask.palletsprojects.com/" target="_blank">Flask Documentation</a></p>'
        '<p><a href="/">Back to Home</a></p>'
	'<a href="https://www.python.org/"> this leads to the python website </a>'
    )

@app.route('/contact')
def contact():
    return '<p>Contact: c23412864@mytudublin.ie</p>'
