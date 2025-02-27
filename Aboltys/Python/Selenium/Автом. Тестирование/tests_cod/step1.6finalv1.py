from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration2.html"

browser = webdriver.Chrome()

try:
    browser.get(link)
    elements = browser.find_elements(By.CSS_SELECTOR, "input:required")

    for element in elements:
        element.send_keys("Hello")

    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()
    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()