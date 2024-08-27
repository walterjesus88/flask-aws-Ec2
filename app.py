from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, soy un developer maste. Deploy on EC2."

if __name__ == '__main__':
    app.run()
