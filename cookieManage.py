import pickle
import selenium.webdriver

def save_cookies(driver, file):
    cookies = driver.get_cookies()
    pickle.dump(cookies,open(file,"wb"))

def use_cookies(driver, file):
    cookies = pickle.load(open(file,"rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)