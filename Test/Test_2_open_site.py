# import line
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://saucedemo.com/")

# поиск элемента
input = driver.find_element(By.ID, 'user-name')
if input is None:
    print('Элемент не найден')
else:
    print('Элемент найден')

# поиск элемента
input = driver.find_element(By.NAME, 'password')
if input is None:
    print('Элемент не найден')
else:
    print('Элемент найден')

# поиск элемента
input = driver.find_element(By.ID, 'login-button')
if input is None:
    print('Элемент не найден')
else:
    print('Элемент найден')
