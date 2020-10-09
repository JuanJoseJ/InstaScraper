from selenium.webdriver import Chrome
from time import sleep
import cookieManage

browser = Chrome()
browser.get("https://www.instagram.com/")
archivoCookies = "cookies.pkl"

try: #Intento usar cookies existentes
    cookieManage.use_cookies(browser, archivoCookies)
    print("Se encontraron cookies guardadas")
    browser.get("https://www.instagram.com/")
except: #Inicio seción si no hay cookies
    print("No se encontraron cookies, se procederá a iniciar seción manualmente")
    #Inicio 
    sleep(1)
    user=browser.find_element_by_name("username")
    pas=browser.find_element_by_name("password")
    user.send_keys("juan.jaramillo57@eia.edu.co")
    pas.send_keys("juanjo123")
    send=browser.find_element_by_xpath("//button[@type='submit']")
    send.click()
    sleep(2)

    #Presiono el botón de mantener seción iniciada
    guardar=browser.find_element_by_xpath("//button[@type='button']")
    guardar.click()
    sleep(1)
    
    #Guardo cookies
    print("Se creó un nuevo archivo de cookies")
    cookieManage.save_cookies(browser, archivoCookies)

#Presiono el boton de no querer notificaciones
notificaciones=browser.find_element_by_xpath("//button[@class='aOOlW   HoLwm ']")
notificaciones.click()
sleep(1)

# buscar=browser.find_element_by_xpath("//input[@class='XTCLo x3qfX ']")
# buscar.send_keys("#halloween")
# sleep(1)
# buscar.submit()

