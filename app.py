from flask import Flask, request, jsonify
from flask_cors import CORS
import logging

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas as rotas

# Configura o logging
logging.basicConfig(level=logging.INFO)

# Lista de usuários autorizados
usuarios_autorizados = [
  "aleandro",
]

# Dicionário para rastrear visitas dos usuários
contador_visitas = {usuario: 0 for usuario in usuarios_autorizados}

@app.route('/validar_usuario', methods=['POST'])
def validar_usuario():
    data = request.get_json()
    usuario = data.get('usuario')

    if usuario in usuarios_autorizados:
        # Incrementa o contador de visitas
        contador_visitas[usuario] += 1
        visitas = contador_visitas[usuario]
        logging.info(f"Usuário autorizado: {usuario} - Visitas: {visitas}")  # Log do nome do usuário e contagem de visitas
        return jsonify({'autorizado': True, 'visitas': visitas}), 200
    else:
        logging.warning(f"Tentativa de acesso não autorizada: {usuario}")  # Log de acesso não autorizado
        return jsonify({'autorizado': False}), 403  # Forbidden

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
