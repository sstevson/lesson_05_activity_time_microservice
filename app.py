"""A simple microservice that shows epoch time"""
import time

from flask import Flask

app = Flask(__name__)


@app.route('/')
def show_epoch_time():
    epoch_time = time.time()
    return f"<h1>Epoch Time: {epoch_time}</h1>"


if __name__ == '__main__':
    app.run()
