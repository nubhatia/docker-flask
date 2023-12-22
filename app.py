# Simple Flask app

from flask import Flask
import os
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Hello Docker!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
    # app.run(debug=True)