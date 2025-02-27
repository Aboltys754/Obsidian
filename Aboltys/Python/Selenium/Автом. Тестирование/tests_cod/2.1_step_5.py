from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try: 
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    value_x = browser.find_element(By.ID, "input_value")
    time.sleep(1)

    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(calc(value_x.text))
    time.sleep(1)

    input_checkbox = browser.find_element(By.ID, "robotCheckbox")
    input_checkbox.click()
    time.sleep(1)

    input_checkbox = browser.find_element(By.ID, "robotsRule")
    input_checkbox.click()
    time.sleep(1)

    input_checkbox = browser.find_element(By.TAG_NAME, "button")
    input_checkbox.click()

    time.sleep(1)

    alert = browser.switch_to.alert
    text_alert = alert.text
    text_answer = text_alert[(text_alert.index(': ')) + 2:]
    alert.accept()
    print(text_answer)
    

finally:
    time.sleep(10)
    browser.close()
    browser.quit()