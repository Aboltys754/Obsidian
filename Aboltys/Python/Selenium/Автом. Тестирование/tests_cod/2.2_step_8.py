from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
    first_name.send_keys('foo')

    last_name = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
    last_name.send_keys('foo')

    email = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
    email.send_keys('foo@email.foo')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    with open(file_path, 'w', encoding='utf-8'):
        pass

    email = browser.find_element(By.CSS_SELECTOR, '[type="file"]')
    email.send_keys(file_path)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()    

    alert = browser.switch_to.alert
    text_alert = alert.text
    text_answer = text_alert[(text_alert.index(': ')) + 2:]
    alert.accept()

    print(text_answer)

finally:
    time.sleep(10)
    browser.close()
    browser.quit()