**Отметить тест как падающий**

Теперь добавим в наш тестовый класс тест, который проверяет наличие кнопки "Избранное":

```python
def test_guest_should_see_search_button_on_the_main_page(self, browser): 
     browser.get(link)
     browser.find_element(By.CSS_SELECTOR, "button.favorite")
```

Предположим, что такая кнопка должна быть, но из-за изменений в коде она пропала. Пока разработчики исправляют баг, мы хотим, чтобы результат прогона ﻿всех ﻿наших тестов был успешен, но падающий тест помечался соответствующим образом, чтобы про него не забыть. Добавим маркировку **@pytest.mark.xfail** для падающего теста.

**test_fixture10.py:**

```python
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():

    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

    @pytest.mark.xfail
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "button.favorite")

```

Запустим наши тесты:

```no-highlight
pytest -v test_fixture10.py
```

Наш упавший тест теперь отмечен как **xfail**, но результат прогона тестов помечен как успешный:

![](https://ucarecdn.com/929c02c8-d2ab-4ecd-a8db-e94d93caecaa/)

Когда баг починят, мы это узнаем, ﻿﻿так как теперь тест будет отмечен как **XPASS** (“unexpectedly passing” — неожиданно проходит). После этого маркировку **xfail** для теста можно удалить. Кстати, к маркировке **xfail** можно добавлять параметр **reason**. Чтобы увидеть это сообщение в консоли, при запуске нужно добавлять параметр pytest **-rx**.

**test_fixture10a.py:**

```python
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():

    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

    @pytest.mark.xfail(reason="fixing this bug right now")
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "button.favorite")

```

Запустим наши тесты:

```no-highlight
pytest -rx -v test_fixture10a.py
```

Сравните вывод в первом и во втором случае.

![](https://ucarecdn.com/0bf951ab-4bad-4d1f-9856-6e0090714627/)

**XPASS-тесты**

Поменяем селектор в последнем тесте, чтобы тест начал проходить.

**test_fixture10b.py:**

```python
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():

    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

    @pytest.mark.xfail(reason="fixing this bug right now")
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "input.btn.btn-default")

```

Запустите тесты. Здесь мы добавили символ X в параметр -r, чтобы получить подробную информацию по XPASS-тестам:

```bash
pytest -rX -v test_fixture10b.py
```

И изучите отчёт: 

![](https://ucarecdn.com/727f6e0f-ef30-4f61-b3ab-65d8d2f7e8d3/)

Дополнительно об использовании этих меток можно почитать в документации: [Skip and xfail: dealing with tests that cannot succeed](https://pytest.org/en/stable/skipping.html).  Там есть много разных интересных особенностей, например, как пропускать тест только при выполнении условия, как сделать так, чтобы внезапно прошедший xfailed тест в отчете стал красным, и так далее.