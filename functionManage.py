import pickle
import selenium.webdriver
from time import sleep

def save_cookies(driver, file): #Guarda las cookies actuales en un archivo .pkl
    cookies = driver.get_cookies()
    pickle.dump(cookies,open(file,"wb"))

def use_cookies(driver, file): #Busca un archivo de cookies y las ingresa a un navegador
    cookies = pickle.load(open(file,"rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)

def pres_button_xpath(driver, xpath): #Funcion para presionar un boton buscado por su xpath. Regresa el objeto del botón
    boton = driver.find_element_by_xpath(xpath)
    boton.click()
    sleep(1)
    return boton

    