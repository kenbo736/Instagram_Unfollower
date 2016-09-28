from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Firefox()

def log_in():
    driver.get("https://www.instagram.com/accounts/login")
    sleep(2)
    elem = driver.find_element_by_name("username")
    elem.send_keys("put_username")
    elem = driver.find_element_by_name("password")
    elem.send_keys("add_password")
    elem.send_keys(Keys.RETURN)
    sleep(10)
    #driver.close()

def un_follow():
    sleep(4)
    print("HELLO")
    elem = driver.find_element_by_class_name("_4zhc5")
    elem.click()
    sleep(3)
    elem = driver.find_element_by_class_name("_aj7mu")
    elem.click()
    sleep(2)
    driver.get("https://www.instagram.com")
    sleep(4)
    #driver.execute_script("arguments[0].click();", elem)
    
log_in()
for i in range(1, 1000):
    un_follow()
driver.close()
