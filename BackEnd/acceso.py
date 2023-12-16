import os #se debe usar ya que vamos a usar creddenciales de entorno
from flask import Flask, request, jsonify, session, Blueprint  # hay que instalar pip flask
from flask_cors import CORS # hay que instalar pip flaskcors
from flask_mysqldb import MySQL #hay que instalarlo con pip flask-mysqldb
import bcrypt # hay que instalar pip bcrypt esto es para hashear las pass y agreegarle sales

acceso_bp = Blueprint("acceso",__name__)
CORS(acceso_bp)  # Habilita CORS para todas las rutas

#mySQL el argumento esta vacio por que ya eesta configurado en app.py
mysql = MySQL()
# Lista para almacenar instancias de la clase Registro
#registros = []

# Definición de la clase Registro
class Registro:
    def __init__(self, email, nombre, apellido, password):
        #self.numero = numero
        self.email = email
        self.nombre = nombre
        self.apellido = apellido
        #almacenamos la pass con hash
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    #definicion para uso de base de datos
    def guardar_en_db(self):        
        cur = mysql.connection.cursor()
        try:
            # Verifica si ya existe un registro con el mismo correo electrónico
            cur.execute("SELECT * FROM USUARIOS WHERE email = %s", (self.email,))
            existing_record = cur.fetchone()

            if existing_record:
                return {'success': False, 'message': 'Ya existe un usuario con ese correo electronico'}
            # Si no existe, procede a crear un nuevo registro
            cur.execute(
                "INSERT INTO USUARIOS (email, nombre, apellido, password) VALUES (%s, %s, %s, %s)",
                (self.email, self.nombre, self.apellido, self.password.decode('utf-8'))
            )
            mysql.connection.commit()
            return {'success': True, 'message': f'Registro con email {self.email} creado con éxito'}
        except Exception as e:
            print(f'Error al ejecutar la consulta SQL: {e}')
            return {'success': False, 'message': f'Error al ejecutar la consulta SQL: {e}'}
        finally:
            cur.close()

#creacion de clavs secretas para sessiones unicas

 ############################# RUTAS ##########################################          
# Función para crear un nuevo registro y agregarlo a la lista
@acceso_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    email = data.get('email')
    nombre = data.get('nombre')
    apellido = data.get('apellido')
    password = data.get('password')

    nuevo_registro = Registro(email, nombre, apellido, password)
    resultado = nuevo_registro.guardar_en_db()

    return jsonify(resultado)


# Función para autenticar un usuario
@acceso_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    try:
        cur = mysql.connection.cursor()
        # Consultar la base de datos para obtener el registro del usuario
        cur.execute("SELECT * FROM USUARIOS WHERE email=%s", (email,))
        registro = cur.fetchone()
        #se accede a registro que es la respuesta de SQL mediante la poscicion [] vectorial
        #y se usa encode en ambos ya que al provenir de cadenas varchar se deben autenticar en bytes
        if registro and bcrypt.checkpw(password.encode('utf-8'), registro[4].encode('utf-8')):
            # Redirigir al usuario a la página deseada después del inicio de sesión exitoso
            return jsonify({
                'success': True,
                'message': 'Inicio de sesión exitoso',
                'data': {'email': registro[1], 'nombre': registro[2], 'apellido': registro[3]}
            })
        else:
            return jsonify({'success': False, 'message': 'Credenciales incorrectas'})
    except Exception as e:
        print(f"Error al autenticar al usuario: {e}")
        return jsonify({'success': False, 'message': 'Error al autenticar al usuario'})
    finally:
        cur.close()

# Ruta para cerrar sesión
@acceso_bp.route('/logout', methods=['POST'])
def logout():
    # Aquí podrías limpiar cualquier información de sesión o realizar otras acciones necesarias
    # Por ejemplo, podrías limpiar la información almacenada en la sesión.
    session.clear()

    return jsonify({'success': True, 'message': 'Sesión cerrada correctamente'})
############################# RUTAS ########################################## 
if __name__ == '__main__':
    acceso_bp.run(debug=True)