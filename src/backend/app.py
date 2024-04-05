from flask import Flask, request, redirect, url_for, render_template, jsonify
from tinydb import TinyDB, Query

app = Flask(__name__)

# Inicializa o banco de dados TinyDB
db = TinyDB('db.json')
logs = db.all()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/ping', methods=['GET'])
def ping():
    db.insert({'action': 'ping'})
    return jsonify({'resposta': 'pong'})

@app.route('/echo', methods=['POST'])
def echo():
     textUser = request.form.get('textUser')
     db.insert({'action': 'echo', 'text': textUser})
     return jsonify({'resposta': textUser})

@app.route('/info')
def info():
    return render_template("logs.html", logs=logs)

@app.route('/dash', methods=['GET'])
def dash():
    logs = db.all()
    return jsonify(logs)

if __name__ == '__main__':
    app.run(debug=True)
