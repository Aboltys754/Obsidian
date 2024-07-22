Если вы уже пробовали запускать примеры скриптов, то могли заметить, что браузер не всегда закрывается после выполнения кода. Поэтому обратите внимание на то, что необходимо явно закрывать окно браузера в нашем коде при помощи команды **browser.quit().** Каждый раз при открытии браузера `browser = webdriver.Chrome()` в системе создается процесс, который останется висеть, если вы вручную закроете окно браузера. Чтобы не остаться без оперативной памяти после запуска нескольких скриптов, всегда добавляйте к своим скриптам команду закрытия:
```python
from selenium import webdriver 
from selenium.webdriver.common.by import By 
link = "http://suninjuly.github.io/simple_form_find_task.html" 
browser = webdriver.Chrome() 
browser.get(link) 
button = browser.find_element(By.ID, "submit_button") 
button.click() 
# закрываем браузер после всех манипуляций 
browser.quit()
```