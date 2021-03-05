from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Merhaba Dünyalı"

@app.route('/hi')
def hi():
    return "Merhaba Kübra"

if __name__ == '__main__' :
    app.run(debug=True)
    