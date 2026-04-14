from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

DJANGO_API_URL = "http://127.0.0.1:8000/api"

@app.route('/')
def home():
    return jsonify({
        "message": "Bem-vindo ao API Gateway do Projeto REST",
        "endpoints": {
            "tarefas": "/tarefas",
            "categorias": "/categorias"
        }
    })


@app.route('/tarefas', methods=['GET', 'POST'])
def get_tarefas():
    if request.method == 'GET':

        response = requests.get(f"{DJANGO_API_URL}/tarefas/")
        return jsonify(response.json()), response.status_code
    
    if request.method == 'POST':
        response = requests.post(f"{DJANGO_API_URL}/tarefas/", json=request.json)
        return jsonify(response.json()), response.status_code
    

@app.route('/categorias', methods=['GET'])
def get_categorias():
    response = requests.get(f"{DJANGO_API_URL}/categorias/")
    return jsonify(response.json()), response.status_code

if __name__ == '__main__':
    app.run(port=5000, debug=True)