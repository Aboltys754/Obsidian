from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input_value = browser.find_element(By.ID, 'input_value')
    input_value_t = int(input_value.text)

    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(calc(input_value_t))

    browser.execute_script("window.scrollBy(0, 100);")

    check_box = browser.find_element(By.ID, 'robotCheckbox')
    check_box.click()

    robotsRule = browser.find_element(By.ID, 'robotsRule')
    robotsRule.click()

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
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