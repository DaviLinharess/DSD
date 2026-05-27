# Usar o Flask pra criar o servidor e o Request pra falar com o Django
from flask import Flask, jsonify, request, send_from_directory
import requests
import os

# Inicia a aplicação do Flask
app = Flask(__name__)

# URL interna do Django. Cliente externo não vê isso, apenas o gateway
DJANGO_INTERNAL_URL = "http://127.0.0.1:8000/api"

@app.route('/')
def home():                                                     # Ao acessar a raiz (/)
    return jsonify({                                            # retorna um JSON
        "projeto": "Trabalho DSD - Davi Linhares",              # Título do projeto
        "endpoints": ["/tarefas", "/categorias", "/cliente"]    # Documentação dos endpoints do gateway
    })

@app.route('/tarefas')                                          # Acessar a rota de tarefas
def get_tarefas():
    resp = requests.get(f"{DJANGO_INTERNAL_URL}/tarefas/")      # Gateway recebe a requisição e vai até o DJANGO buscar os dados
    return jsonify(resp.json())                                 # repassa para o usuário (esconde a complexidade interna)


@app.route('/categorias')                                       # Acessar a rota de Categorias     
def get_categorias():
    resp = requests.get(f"{DJANGO_INTERNAL_URL}/categorias/")   # Gateway recebe a requisição e vai até o DJANGO buscar os dados
    return jsonify(resp.json())                                 # repassa para o usuário (esconde a complexidade)


@app.route('/cliente')                                          # Rota do Cliente WEB
def serve_cliente():                                            # Gateway entrega a inteface (HTML) pro usuário
    return send_from_directory(os.getcwd(), 'index.html')       # O "os.getcwd" garante que o python ache o index.html independente de onde o servidor for iniciado

if __name__ == '__main__':                                      # Gateway rodando na porta 5000, separada do django (8000)
    app.run(port=5000, debug=True)                              # Ou seja, componentes diferente se comunicando.