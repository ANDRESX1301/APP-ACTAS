import os #se debe usar ya que vamos a usar creddenciales de entorno
from flask import Flask
from flask_mysqldb import MySQL #hay que instalarlo con pip flask-mysqldb
from acceso import acceso_bp #aqui se importan los archivos de el otro .py
from DBresponse import DBresponse_bp #aqui se importan los archivos de el otro .py
import secrets # no hay que instalarlo pero si se hace necesario para las sessiones
app = Flask(__name__)
# Configuración de la clave secreta para sesiones
app.secret_key = secrets.token_hex(16)
# Configuracion de los Blueprints o archivos satelite
app.register_blueprint(acceso_bp)
app.register_blueprint(DBresponse_bp)

# Configuración de la conexión a la base de datos MariaDB usando eviromental
app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST','localhost')
app.config['MYSQL_PORT'] = int(os.environ.get('MYSQL_PORT', 3306))  # El valor predeterminado es 3306
app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER', 'tu_usuario')
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD', 'tu_contraseña')
app.config['MYSQL_DB'] = os.environ.get('MYSQL_DB', 'tu_base_de_datos')

mysql = MySQL(app)

if __name__ == '__main__':
    app.run(debug=True)