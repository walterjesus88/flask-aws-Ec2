from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Worded! This is a Flask app deployed with GitHub Actions on EC2."

if __name__ == '__main__':
    app.run()
