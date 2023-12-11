# app.py

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas las rutas

# Lista para almacenar instancias de la clase Registro
registros = []

# Definición de la clase Registro
class Registro:
    def __init__(self, numero, email, nombre, apellido, contraseña):
        self.numero = numero
        self.email = email
        self.nombre = nombre
        self.apellido = apellido
        self.contraseña = contraseña

# Función para crear un nuevo registro y agregarlo a la lista
@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    numero = 1 if not registros else registros[-1].numero + 1
    email = data.get('email')
    nombre = data.get('nombre')
    apellido = data.get('apellido')
    contraseña = data.get('contraseña')

    # Crea una instancia de la clase Registro con la información proporcionada
    registro = Registro(numero, email, nombre, apellido, contraseña)
    # Agrega el registro a la lista de registros
    registros.append(registro)

    return jsonify({'success': True, 'message': 'Registro '+email+' creado con éxito'})

# Función para autenticar un usuario
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')

    # Busca el registro en la lista de registros
    registro = next((r for r in registros if r.email == email), None)
    
    # Muestra la información si el registro se encuentra, de lo contrario, imprime un mensaje
    if registro:
        return jsonify({
            'success': True,
            'message': 'Inicio de sesión exitoso',
            'data': {'numero': registro.numero, 'nombre': registro.nombre, 'apellido': registro.apellido}
        })
    else:
        return jsonify({'success': False, 'message': 'Credenciales incorrectas'})

if __name__ == '__main__':
    app.run(debug=True)
