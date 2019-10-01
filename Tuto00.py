from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def receive_message():
    return 'Hello World!'


@app.route('/Home', methods=['GET', 'POST'])
def home():
    return 'My Sweet Home!'


if __name__ == '__main__':
    app.run(port=5000)
