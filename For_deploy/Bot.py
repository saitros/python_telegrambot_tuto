from flask import Flask
import os

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def receive_message():
    return 'Hello World!'


@app.route('/Home', methods=['GET', 'POST'])
def home():
    return 'My Sweet Home!'


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
