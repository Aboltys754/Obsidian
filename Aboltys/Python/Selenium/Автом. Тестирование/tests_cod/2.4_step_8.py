from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)

    
    price_house = WebDriverWait(browser, 12).until(
       EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )    
    button = browser.find_element(By.ID, 'book')
    button.click()

    value_math = browser.find_element(By.ID, 'input_value').text

    input_field = browser.find_element(By.ID, 'answer')
    input_field.send_keys(calc(value_math))

    submit = browser.find_element(By.ID, 'solve').click()

    alert = browser.switch_to.alert
    text_alert = alert.text

    answer_alert = text_alert[(text_alert.index(': ')) + 2:]
    print(answer_alert)
    alert.accept()

finally:
    time.sleep(10)
    browser.close()
    browser.quit()