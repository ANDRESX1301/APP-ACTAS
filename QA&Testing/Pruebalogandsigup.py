from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def print_green(text):
    print("\033[92m{}\033[0m".format(text))  # Código ANSI para texto verde

def print_red(text):
    print("\033[91m{}\033[0m".format(text))  # Código ANSI para texto rojo

# Configuración específica para Brave en modo headless
brave_options = webdriver.ChromeOptions()
brave_options.binary_location = 'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe'  # Ajusta la ruta según tu instalación
#brave_options.add_argument('--headless')  # Habilita el modo headless

# Inicializa el controlador de Chrome con las opciones de Brave
driver = webdriver.Chrome(options=brave_options)

# Abrir la página de inicio de sesión
driver.get("http://localhost:3000/")

# Encontrar los campos de usuario y contraseña e ingresar información
username_field = driver.find_element("xpath", "//input[@type='email']")
password_field = driver.find_element("xpath", "//input[@type='password']")

#---------------------------
#importante si se hace headless test se deshabilitan las lineas time.slep ya que no 
#se tiene ambiente grafico
#---------------------------
# Ingresar información en los campos
#time.sleep(1)
username_field.send_keys("rr@gmail.com")
#time.sleep(1)
password_field.send_keys("Prueba321")

# Espera adicional para observar la acción antes de enviar el formulario
#time.sleep(1)

# Enviar el formulario
password_field.send_keys(Keys.RETURN)

# Espera adicional para ver la página de inicio de sesión (ajusta según sea necesario)
#time.sleep(3)

# Verificar si el inicio de sesión fue exitoso y mostrar un mensaje de color
#pilas por que si el enfoque es que valide por el acceso a una nueva pagina es perceptiva a mayusculas 
try:
    WebDriverWait(driver, 3).until(EC.url_contains("http://localhost:3000/home"))
    print_green("Inicio de sesión exitoso")
except:
    print_red("Fallo en el inicio de sesión")

# Cerrar el navegador
driver.quit()


'''
import time
from selenium import webdriver

# Configuración específica para Brave
brave_options = webdriver.ChromeOptions()
brave_options.binary_location = 'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe'  # Ajusta la ruta según tu instalación

# Inicializa el controlador de Chrome con las opciones de Brave
driver = webdriver.Chrome(options=brave_options)

# Resto del código
driver.get('http://www.facebook.com/')

time.sleep(5)

search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()

time.sleep(5)

# Cierra el navegador
driver.quit()
'''