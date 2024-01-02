from flask import request, jsonify, session, Blueprint, current_app  # hay que instalar pip flask
from flask_cors import CORS # hay que instalar pip flaskcors
from flask_mysqldb import MySQL #hay que instalarlo con pip flask-mysqldb
import bcrypt # hay que instalar pip bcrypt esto es para hashear las pass y agreegarle sales
from werkzeug.utils import secure_filename #se utiliza para asegurar que un nombre de archivo sea seguro para su uso en el sistema de archivos como el logo
import boto3 #se usa para subir y bajar archivos a un S3 buket y se instala desde pip
from botocore.exceptions import NoCredentialsError # se usa junto a boto 3
import tempfile # se debe usar para hacer carga de archivos temporales en el servidor de flask
import os #se debe usar ya que vamos a usar creddenciales de entorno

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
        # Extraemos el recurso o nombre de empresa del email
        self.recurso = self.email.split('@')[1].split('.')[0]
    #definicion para uso de base de datos
    def guardar_en_db(self):        
        cur = mysql.connection.cursor()
        try:
            # Verifica si ya existe un registro con el mismo correo electrónico
            cur.execute("SELECT * FROM OPERADORES WHERE email = %s", (self.email,))
            existing_record = cur.fetchone()

            if existing_record:
                return {'success': False, 'message': 'Ya existe un usuario con ese correo electronico'}
            # Si no existe, procede a crear un nuevo registro
            cur.execute(
                "INSERT INTO OPERADORES (email, nombre, apellido, password, recurso) VALUES (%s, %s, %s, %s, %s)",
                (self.email, self.nombre, self.apellido, self.password.decode('utf-8'), self.recurso)
            )
            mysql.connection.commit()
            return {'success': True, 'message': f'Registro con email {self.email} creado con éxito'}
        except Exception as e:
            print(f'Error al ejecutar la consulta SQL: {e}')
            return {'success': False, 'message': f'Error al ejecutar la consulta SQL: {e}'}
        finally:
            cur.close()

class Cliente:
    def __init__(self, nombrersocial, nfrontend, representante, recurso, nit, telefono, direccion, logo_path):
        self.nombrersocial = nombrersocial
        self.nfrontend = nfrontend
        self.representante = representante
        self.recurso = recurso
        self.nit = nit
        self.telefono = telefono
        self.direccion = direccion
        self.logo_path = logo_path

    def guardar_en_db_cliente(self):        
        cur = mysql.connection.cursor()
        try:
            # Verificar si ya existe un registro con el mismo recurso
            cur.execute("SELECT * FROM CLIENTES WHERE recurso = %s", (self.recurso,))
            existing_record = cur.fetchone()

            if existing_record:
                return {'success': False, 'message': 'Ya existe un CLIENTE con ese recurso'}
            
            # Insertar un nuevo registro en la base de datos
            cur.execute(
                "INSERT INTO CLIENTES (nombrersocial, nfrontend, representante, recurso, nit, telefono, direccion, logo_path) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                (self.nombrersocial, self.nfrontend, self.representante, self.recurso, self.nit, self.telefono, self.direccion, self.logo_path)
            )
            mysql.connection.commit()
            
            return {'success': True, 'message': f'Registro del cliente {self.nombrersocial} creado con éxito'}
        except Exception as e:
            print(f'Error al ejecutar la consulta SQL: {e}')
            return {'success': False, 'message': f'Error al ejecutar la consulta SQL: {e}'}
        finally:
            cur.close()

    def upload_to_s3(self, file_path, s3_path): 
        try:
            AWS_ACCESS_KEY_ID = current_app.config['AWS_ACCESS_KEY_ID']
            AWS_SECRET_ACCESS_KEY = current_app.config['AWS_SECRET_ACCESS_KEY']
            AWS_BUCKET_NAME = current_app.config['AWS_BUCKET_NAME']
            # Configuración de las credenciales de AWS
            s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
            
            # Subir el archivo al bucket de S3
            s3.upload_file(file_path, AWS_BUCKET_NAME, s3_path)
            
            #print(f"Archivo {file_path} subido exitosamente a {AWS_BUCKET_NAME}/{s3_path}")
            return True
        except FileNotFoundError:
            print(f"El archivo {file_path} no fue encontrado")
            return False
        except NoCredentialsError:
            print("Credenciales de AWS no disponibles")
            return False
        except Exception as e:
            print(f"Error al subir el archivo a S3: {e}")
            return False


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

# Función para crear un nuevo registro y agregarlo a la lista
@acceso_bp.route('/altacliente', methods=['POST'])
def altacliente():
    try:
        data = request.form.to_dict()
        nombrersocial = data.get('nombrersocial')
        nfrontend = data.get('nfrontend')
        representante = data.get('representante')
        recurso = data.get('recurso')
        nit = data.get('nit')
        telefono = data.get('telefono')
        direccion = data.get('direccion')

        # Puedes acceder al archivo del logo directamente desde request.files
        logo_file = request.files['logo']
        
        # Asegurar que el nombre de archivo sea seguro
        secure_logo_filename = secure_filename(logo_file.filename)
        #print(secure_logo_filename)
        logo_path = f"S3/APPACTAS/LOGOSEMPRESA/{secure_logo_filename}"
        
        # Guardar temporalmente el archivo en el servidor
        temp_file_path = os.path.join(tempfile.gettempdir(), secure_logo_filename)
        logo_file.save(temp_file_path)
        # Crear una instancia de Cliente
        nuevo_registro = Cliente(nombrersocial, nfrontend, representante, recurso, nit, telefono, direccion, logo_path)

        # Subir el archivo al bucket de S3
        if nuevo_registro.upload_to_s3(temp_file_path, logo_path):
            # Eliminar el archivo temporal después de subirlo a S3
            os.remove(temp_file_path)
            # Si la carga en S3 es exitosa, procede a almacenar en la base de datos
            resultado = nuevo_registro.guardar_en_db_cliente()

            return jsonify(resultado)
        else:
            return jsonify({'success': False, 'message': 'Error al cargar el logo en S3'})
    except Exception as e:
        print(f"Error en altacliente: {e}")
        return jsonify({'success': False, 'message': 'Error en altacliente'})
    
# Función para autenticar un usuario
@acceso_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    try:
        cur = mysql.connection.cursor()
        # Consultar la base de datos para obtener el registro del usuario
        cur.execute("SELECT * FROM OPERADORES WHERE email=%s AND habilitado='s'", (email,))
        registro = cur.fetchone()
        # Validar que el usuario existe y la contraseña coincide
        #se accede a registro que es la respuesta de SQL mediante la poscicion [] vectorial
        #y se usa encode en ambos ya que al provenir de cadenas varchar se deben autenticar en bytes
        if registro and bcrypt.checkpw(password.encode('utf-8'), registro[4].encode('utf-8')):
            # Redirigir al usuario a la página deseada después del inicio de sesión exitoso
            cur.execute("SELECT * FROM CLIENTES WHERE recurso=%s AND habilitado='s'", (registro[5],))
            cliente = cur.fetchone()

            if cliente:
                # Redirigir al usuario a la página deseada después del inicio de sesión exitoso
                return jsonify({
                    'success': True,
                    'message': 'Inicio de sesión exitoso',
                    'data': {'email': registro[1], 'nombre': registro[2], 'apellido': registro[3]}
                })
            else:
                return jsonify({'success': False, 'message': 'La empresa no ha sido dada de ALTA'})
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