from selenium.webdriver import Chrome
from time import sleep
import functionManage as function

browser = Chrome()
browser.get("https://www.instagram.com/")
archivoCookies = "cookies.pkl"

try: #Intento usar cookies existentes
    function.use_cookies(browser, archivoCookies)
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
    function.pres_button_xpath(browser, "//button[@type='button']")


    #Guardo cookies
    print("Se creó un nuevo archivo de cookies")
    function.save_cookies(browser, archivoCookies)

#Presiono el boton de no querer notificaciones
function.pres_button_xpath(browser, "//button[@class='aOOlW   HoLwm ']")

tag = "halloween"
buscar=browser.find_element_by_xpath("//input[@class='XTCLo x3qfX ']")
buscar.send_keys("#"+tag)
sleep(1)
tag=browser.find_element_by_xpath("//a[@href='/explore/tags/"+tag+"/']")
sleep(1)
# buscar.submit()

