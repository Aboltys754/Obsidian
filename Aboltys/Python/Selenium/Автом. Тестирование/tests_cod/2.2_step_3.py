from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


try: 
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID, 'num1')
    num2 = browser.find_element(By.ID, 'num2')
    num1_t = int(num1.text)
    num2_t = int(num2.text)

    select = Select(browser.find_element(By.ID, 'dropdown'))
    click_select = select.select_by_value(f'{num1_t + num2_t}') 
    button = browser.find_element(By.TAG_NAME, 'button')
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