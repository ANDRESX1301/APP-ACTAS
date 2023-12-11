# Definición de la clase Registro para representar un objeto de registro
class Registro:
    def __init__(self, numero, email, nombre, apellido, contraseña):
        # Constructor que inicializa los atributos del objeto Registro
        self.numero = numero
        self.email = email
        self.nombre = nombre
        self.apellido = apellido
        self.contraseña = contraseña

# Lista para almacenar instancias de la clase Registro
registros = []

# Función para crear un nuevo registro y agregarlo a la lista
def crear_registro():
    # Solicita al usuario información para crear un nuevo registro
    print("\n**********************************************") 
    print("Ha escogido crear registro")
    numero = 1 if not registros else registros[-1].numero + 1
    cedula = int(input("Ingrese la Cedula del registro: "))
    nombre = input("Ingrese el nombre: ")
    edad = int(input("Ingrese la edad: "))
    print("*********************************************\n") 
    
    # Crea una instancia de la clase Registro con la información proporcionada
    registro = Registro(numero, cedula, nombre, edad)
    
    # Agrega el registro a la lista de registros
    registros.append(registro)
    
    # Imprime un mensaje indicando que el registro ha sido creado con éxito
    print("Registro creado con éxito.")

# Función para leer un registro específico según su ID
def leer_registro():
    # Solicita al usuario el ID del registro que desea consultar
    print("Ha escogido leer un registro")
    cedula = int(input("Ingrese la Cedula del registro a leer: "))
    
    # Busca el registro en la lista de registros
    registro = next((r for r in registros if r.cedula == cedula), None)
    
    # Muestra la información si el registro se encuentra, de lo contrario, imprime un mensaje
    if registro:
        print(f"Registro encontrado: Numero={registro.numero}, CC={registro.cedula}, Nombre={registro.nombre}, Edad={registro.edad}")
    else:
        print("Registro no encontrado.")

# Función para imprimir todos los registros almacenados
def leer_todosregistros():
    # Verifica si hay registros en la lista
    print("Ha escogido Leer todos los registros")
    if registros:
        # Itera sobre la lista e imprime los atributos de cada registro
        for registro in registros:
            print(f"Numero={registro.numero}, CC={registro.cedula}, Nombre={registro.nombre}, Edad={registro.edad}")
    else:
        print("No hay registros almacenados.")

# Función para actualizar la información de un r1egistro existente
def actualizar_registro():
    # Solicita al usuario el ID del registro que desea actualizar
    print("Ha escogido actualizar un registro")
    cedula = int(input("Ingrese la Cedula del registro a actualizar: "))
    
    # Busca el registro en la lista de registros
    registro = next((r for r in registros if r.cedula == cedula), None)
    
    # Actualiza la información del registro si se encuentra, de lo contrario, imprime un mensaje
    if registro:
        nombre = input("Ingrese el nuevo nombre: ")
        edad = int(input("Ingrese la nueva edad: "))
        registro.nombre = nombre
        registro.edad = edad
        print("Registro actualizado con éxito.")
    else:
        print("Registro no encontrado.")

# Función para eliminar un registro de la lista
def eliminar_registro():
    # Solicita al usuario el ID del registro que desea eliminar
    print("Ha escogido eliminar un registro")
    cedula = int(input("Ingrese la Cedula del registro a eliminar: "))
    
    # Busca el registro en la lista de registros
    registro = next((r for r in registros if r.cedula == cedula), None)
    
    # Elimina el registro de la lista si se encuentra, de lo contrario, imprime un mensaje
    if registro:
        registros.remove(registro)
        print("Registro eliminado con éxito.")
    else:
        print("Registro no encontrado.")

# Función para imprimir el menú de opciones
def imprimir_menu():
    print("\n**********************************************")   
    print("Menú de opciones")
    print("1. Crear registro")
    print("2. Leer registro")
    print("3. Leer registro (TODOS)")    
    print("4. Actualizar registro")
    print("5. Eliminar registro")
    print("6. Salir")
    print("**********************************************\n")   

# Bucle principal que muestra el menú y realiza acciones según la opción seleccionada
while True:
    imprimir_menu()
    opcion = input("Seleccione una opción: ")

    # Realiza la acción correspondiente según la opción seleccionada
    if opcion == "1":
        crear_registro()        
    elif opcion == "2":
        leer_registro()
    elif opcion == "3":
        leer_todosregistros()
    elif opcion == "4":
        actualizar_registro()
    elif opcion == "5":
        eliminar_registro()
    elif opcion == "6":
        break
    else:
        print("Opción no válida. Intente nuevamente.")
