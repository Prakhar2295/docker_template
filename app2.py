import os
from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello():
    return "my first image!!@"


@app.route("/container")
def container():
    return "container running successfully!!"



if __name__ == "__main__":
    print("print 2nd image")
    app.run()


