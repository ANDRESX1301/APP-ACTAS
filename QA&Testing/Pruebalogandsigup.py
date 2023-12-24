# Importa la clase `webdriver` del módulo `selenium`, que proporciona la interfaz para interactuar con navegadores web.
from selenium import webdriver
# Importa la clase `Keys` del módulo `selenium.webdriver.common.keys`, que proporciona acceso a las teclas del teclado.
from selenium.webdriver.common.keys import Keys
# Importa la clase `WebDriverWait` del módulo `selenium.webdriver.support.ui`, que permite esperar dinámicamente hasta que se cumpla una condición antes de continuar con el script.
from selenium.webdriver.support.ui import WebDriverWait
# Importa la clase `expected_conditions` del módulo `selenium.webdriver.support`, que proporciona condiciones esperadas (utilizadas con WebDriverWait).
from selenium.webdriver.support import expected_conditions as EC
# Importa la clase `Faker` del módulo `faker`, que se utiliza para generar datos ficticios como nombres, direcciones, direcciones de correo electrónico, etc.
from faker import Faker

def print_green(text):
    print("\033[92m{}\033[0m".format(text))  # Código ANSI para texto verde

def print_red(text):
    print("\033[91m{}\033[0m".format(text))  # Código ANSI para texto rojo

def prueba_login_exitoso(driver):
    # Tu código de prueba para inicio de sesión exitoso
    driver.get("http://localhost:3000/")
    # Resto del código...
    # Encontrar los campos de usuario y contraseña e ingresar información
    username_field = driver.find_element("xpath", "//input[@type='email']")
    password_field = driver.find_element("xpath", "//input[@type='password']")
    # Ingresar información en los campos
    username_field.send_keys("rr@gmail.com")
    password_field.send_keys("Prueba321")
    # Enviar el formulario
    password_field.send_keys(Keys.RETURN)

    try:
        WebDriverWait(driver, 3).until(EC.url_contains("http://localhost:3000/home"))
        print_green("Prueba Login OK")
    except:
        print_red("Fallo en la prueba Login")

def prueba_usuario_errado(driver):
    # Tu código de prueba para inicio de sesión exitoso
    driver.get("http://localhost:3000/")
    # Resto del código...
    # Encontrar los campos de usuario y contraseña e ingresar información
    username_field = driver.find_element("xpath", "//input[@type='email']")
    password_field = driver.find_element("xpath", "//input[@type='password']")
    # Ingresar información en los campos
    username_field.send_keys("rr@gmail.com")
    password_field.send_keys("Prueba31")
    # Enviar el formulario
    password_field.send_keys(Keys.RETURN)
    
    # Utilizar WebDriverWait para esperar hasta que aparezca el mensaje de error
    try:
        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(("xpath", "//p[@style='color: red;']"))
        )
        
        # Extraer el contenido del elemento
        error_message_text = error_message.text
        
        if "Credenciales incorrectas" in error_message_text:
            print_green("Prueba de usuario incorrecto OK")
        else:
            print_red("Fallo en la Prueba de usuario incorrecto")
    except Exception as e:
        print_red(f"Fallo en la Prueba de usuario incorrecto (excepcion): {e}")


def prueba_nuevo_usuario(driver):
    # Tu código de prueba para inicio de sesión exitoso
    driver.get("http://localhost:3000/signup")
    # Resto del código...
    # Encontrar los campos de usuario y contraseña e ingresar información
    name_field = driver.find_element("xpath", "//label[text()='Nombre:']/input")
    apellido_field = driver.find_element("xpath", "//label[text()='Apellido:']/input")
    username_field = driver.find_element("xpath", "//input[@type='email']")
    password_field = driver.find_element("xpath", "//input[@type='password']")
    
    # Ingresar información en los campos
    name_field.send_keys(random_name)
    apellido_field.send_keys(random_apellido)
    username_field.send_keys(random_email)
    password_field.send_keys("Prueba321")
    # Enviar el formulario
    password_field.send_keys(Keys.RETURN)
    
    # Utilizar WebDriverWait para esperar hasta que aparezca el mensaje de error
    try:
        error_message = WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(("xpath", "//p[@style='color: green;']"))
        )
        
        # Extraer el contenido del elemento
        error_message_text = error_message.text
        
        if "Usuario registrado con exito" in error_message_text:
            print_green("Prueba de Registro NUEVO OK")
        else:
            print_red("Fallo en la Prueba de Registro NUEVO")
    except Exception as e:
        print_red(f"Fallo en la Prueba de Registro NUEVO (excepcion): {e}")

def prueba_usuario_yaexiste (driver):
    # Tu código de prueba para inicio de sesión exitoso
    driver.get("http://localhost:3000/signup")
    # Resto del código...
    # Encontrar los campos de usuario y contraseña e ingresar información
    name_field = driver.find_element("xpath", "//label[text()='Nombre:']/input")
    apellido_field = driver.find_element("xpath", "//label[text()='Apellido:']/input")
    username_field = driver.find_element("xpath", "//input[@type='email']")
    password_field = driver.find_element("xpath", "//input[@type='password']")
    
    # Ingresar información en los campos
    name_field.send_keys('Ya')
    apellido_field.send_keys('Existe')
    username_field.send_keys('random_email@random.com')
    password_field.send_keys("Prueba321")
    # Enviar el formulario
    password_field.send_keys(Keys.RETURN)
    
    # Utilizar WebDriverWait para esperar hasta que aparezca el mensaje de error
    try:
        error_message = WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(("xpath", "//p[@style='color: red;']"))
        )
        
        # Extraer el contenido del elemento
        error_message_text = error_message.text
        
        if "Ya existe un usuario con ese correo electronico" in error_message_text:
            print_green("Prueba de Registro Repetido OK")
        else:
            print_red("Fallo en la Prueba Prueba de Registro Repetido")
    except Exception as e:
        print_red(f"Fallo en la Prueba Prueba de Registro Repetido (excepcion): {e}")



if __name__ == '__main__':
    fake = Faker()
    random_name = fake.name()
    random_apellido = fake.last_name()
    random_email = fake.email()
    
    
    brave_options = webdriver.ChromeOptions()
    brave_options.binary_location = 'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe'  # Ajusta la ruta según tu instalación
    # Configuración específica para Brave en modo headless
    brave_options.add_argument('--headless')  # Habilita el modo headless

    # Inicializa el controlador de Chrome con las opciones de Brave
    driver = webdriver.Chrome(options=brave_options)

    # Ejecutar pruebas
    prueba_login_exitoso(driver)
    prueba_usuario_errado(driver)
    prueba_nuevo_usuario(driver)
    prueba_usuario_yaexiste(driver)

    # Cerrar el navegador al final de todas las pruebas
    driver.quit()