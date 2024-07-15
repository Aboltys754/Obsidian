https://habr.com/ru/companies/otus/articles/596071/
https://www.lambdatest.com/learning-hub/selenium-locators
https://selenium-python.readthedocs.io/index.html

Установка
```python
pip install selenium
```
Импорт
``` python
from selenium import webdriver
```
**Инициализация дайвера в Python**
```python
driver = webdriver.Chrome()

driver = webdriver.Firefox()

driver = webdriver.Safari()

driver = webdriver.Ie()
```
Если местоположения драйвера браузера нет в переменной PATH (или если его нет в System Path), нужно добавить следующие аргументы:

1. `executable_path`: Путь к вашему веб-драйверу Selenium (бинарный файл)    
2. `options`: Параметры, касающиеся выполнения веб-браузеров
```python
driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver/", options=chrome_options )
```

**Настройка параметров Selenium WebDriver**

Класс `Options` в Selenium обычно используется в сочетании с желаемыми возможностями кастомизации Selenium WebDriver.

Так вы можете выполнять различные операции, такие как открытие браузера (Chrome, Firefox, Safari, IE, Edge и т.д.) в режиме увеличения, включение и отключение расширений браузера, отключение режима GPU, отключение всплывающих окон и многое другое. Поэтому важно хорошо разобраться в этом разделе шпаргалки по Selenium в Python, поскольку так вы сможете решить проблемы автоматизации, связанные с изменением свойств браузера, о которых мы говорили ранее.







