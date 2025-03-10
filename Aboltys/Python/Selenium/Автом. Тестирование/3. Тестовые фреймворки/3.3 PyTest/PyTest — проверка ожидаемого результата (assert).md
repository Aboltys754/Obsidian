Если вы используете unittest, то для проверки ожидаемых результатов в тестах вам нужно знать и использовать большой набор assert-методов, например, таких: assertEqual, assertNotEqual, assertTrue, assertFalse и [другие](https://docs.python.org/3/library/unittest.html#assert-methods%EF%BB%BF).

В PyTest используется стандартный assert метод из языка Python, что делает код более очевидным.

Давайте сравним два подхода. Проверим, что две переменные равны друг другу.

**unittest:**
```
self.assertEqual(a, b, msg="Значения разные")
```
**PyTest:**
```
assert a == b, "Значения разные"
```
С помощью assert можно проверять любую конструкцию, которая возвращает True/False. Это может быть проверка равенства, неравенства, содержания подстроки в строке или любая другая вспомогательная функция, которую вы опишете самостоятельно. Все это делает код проверок приятным и понятным для чтения: 
```
assert user_is_authorised(), "User is guest"
```
Если нужно проверить, что тест вызывает ожидаемое исключение (довольно редкая ситуация для UI-тестов, и вам этот способ, скорее всего, никогда не пригодится), мы можем использовать специальную конструкцию **with pytest.raises()**. Например, можно проверить, что на странице сайта не должен отображаться какой-то элемент:

```python
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def test_exception1():
    try:
        browser = webdriver.Chrome()
        browser.get("http://selenium1py.pythonanywhere.com/")
        with pytest.raises(NoSuchElementException):
            browser.find_element(By.CSS_SELECTOR, "button.btn")
            pytest.fail("Не должно быть кнопки Отправить")
    finally: 
        browser.quit()

def test_exception2():
    try:
        browser = webdriver.Chrome()
        browser.get("http://selenium1py.pythonanywhere.com/")
        with pytest.raises(NoSuchElementException):
            browser.find_element(By.CSS_SELECTOR, "no_such_button.btn")
            pytest.fail("Не должно быть кнопки Отправить")
    finally: 
        browser.quit()
```

В первом тесте элемент будет найден, поэтому ошибка **NoSuchElementException**, которую ожидает контекстный менеджер pytest.raises, не возникнет, и тест упадёт.
```
test_3_3_9_pytest_raises.py:8 (test_exception1)
E   Failed: Не должно быть кнопки Отправить
```
Во втором тесте, как мы и ожидали, кнопка не будет найдена, и тест пройдет.