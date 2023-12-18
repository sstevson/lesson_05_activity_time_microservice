"""A simple microservice that shows epoch time"""
import os
import time

from flask import Flask

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY").encode()


@app.route('/')
def show_epoch_time():
    epoch_time = time.time()
    return f"<h1>The current epoch time is: {epoch_time}</h1>"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host="0.0.0.0", port=port)
