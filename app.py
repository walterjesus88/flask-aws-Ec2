from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Carlos es un idiota!!"

if __name__ == '__main__':
    app.run()
