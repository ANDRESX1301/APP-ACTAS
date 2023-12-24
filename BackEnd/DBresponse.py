# En tu archivo .py
from flask import  jsonify, Blueprint
from flask_mysqldb import MySQL #hay que instalarlo con pip flask-mysqldb
from flask_cors import CORS # hay que instalar pip flaskcors

DBresponse_bp = Blueprint("DBresponse",__name__)
CORS(DBresponse_bp)


mysql = MySQL()
# Ruta para obtener opciones desde la base de datos
@DBresponse_bp.route('/opciones', methods=['GET'])
def obtener_opciones():
    try:
        # Realiza la lógica para obtener las opciones desde la base de datos
        cur = mysql.connection.cursor()
        # Consultar la base de datos para obtener las opciones del usuario
        cur.execute("SELECT * FROM OPERADORES WHERE email = %s", ('rr@gmail.com',))
        opciones = cur.fetchall()
        # Transformar los resultados en un formato adecuado para el JSON
        opciones_list = [{'email': opcion[1], 'apellido': opcion[3]} for opcion in opciones]
        #print(opciones_list) 
        return jsonify({
            'success': True,
            'message': 'Opciones obtenidas', 
            'opciones': opciones_list
            })
    except Exception as e:
        return jsonify({'success': False, 'message': f'Error al obtener opciones: {e}'})
    finally:
        cur.close()

if __name__ == '__main__':
    DBresponse_bp.run(debug=True)