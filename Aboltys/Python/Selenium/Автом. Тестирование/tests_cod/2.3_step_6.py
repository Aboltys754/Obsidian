from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    time.sleep(2)

    input_value = browser.find_element(By.ID, 'input_value').text

    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(calc(input_value))

    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()

    alert = browser.switch_to.alert
    text_alert = alert.text

    answer_alert = text_alert[(text_alert.index(': ')) + 2:]
    print(answer_alert)
    alert.accept()




finally:
    time.sleep(10)
    browser.close()
    browser.quit()