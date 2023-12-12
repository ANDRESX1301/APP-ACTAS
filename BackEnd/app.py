# app.py

from flask import Flask, request, jsonify # hay que instalar pip flask
from flask_cors import CORS # hay que instalar pip flaskcors
import bcrypt # hay que instalar pip bcrypt esto es para hashear las pass y agreegarle sales

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas las rutas

# Lista para almacenar instancias de la clase Registro
registros = []

# Definición de la clase Registro
class Registro:
    def __init__(self, numero, email, nombre, apellido, password):
        self.numero = numero
        self.email = email
        self.nombre = nombre
        self.apellido = apellido
        #almacenamos la pass con hash
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# Función para crear un nuevo registro y agregarlo a la lista
@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    email = data.get('email')
    # Verifica si ya existe un registro con el mismo correo electrónico
    if any(registro.email == email for registro in registros):
        return jsonify({'success': False, 'message': 'Ya existe un usuario con este correo electrónico'})
    # Si no existe, procede a crear un nuevo registro
    numero = 1 if not registros else registros[-1].numero + 1
    nombre = data.get('nombre')
    apellido = data.get('apellido')
    password = data.get('password')

    # Crea una instancia de la clase Registro con la información proporcionada
    registro = Registro(numero, email, nombre, apellido, password)
    # Agrega el registro a la lista de registros
    registros.append(registro)

    return jsonify({'success': True, 'message': 'Registro #:'+str(numero)+' '+email+' creado con éxito '})

# Función para autenticar un usuario
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')# Agrega la obtención de la password desde la solicitud

    # Busca el registro en la lista de registros
    registro = next((r for r in registros if r.email == email), None)

    # Muestra la información si el registro se encuentra, de lo contrario, imprime un mensaje
    if registro and bcrypt.checkpw(password.encode('utf-8'), registro.password):
        return jsonify({
            'success': True,
            'message': 'Inicio de sesión exitoso',
            'data': {'pass':registro.password, 'numero': registro.numero, 'nombre': registro.nombre, 'apellido': registro.apellido}
        })
    else:
        return jsonify({'success': False, 'message': 'Credenciales incorrectas'})

if __name__ == '__main__':
    app.run(debug=True)
