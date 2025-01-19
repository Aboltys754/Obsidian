В Selenium представлены различные действия, которые можно выполнить с помощью клавиатуры. В основном, можно выполнять два действия:

- Нажать клавишу,
- Отпустить нажатую клавишу.

**Нажатие клавиши (Key down)**

```python
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = ... # инициализация драйвера
ActionChains(driver).key_down(Keys.SHIFT).send_keys("abc").perform()
```

**Отпускание клавиши (Key up)**

```python
ActionChains(driver).key_down(Keys.SHIFT).send_keys("a").key_up(Keys.SHIFT).send_keys("b").perform()
```

Импортируем:  

```javascript
from selenium.webdriver import Keys 

или 

from selenium.webdriver.common.keys import Keys
```

Откроем наш [сайт](http://parsinger.ru/scroll/1/). На нём находится 100 тегов `<input>`, с которыми мы будем взаимодействовать с помощью класса `Keys`. Таким образом взаимодействовать можно только с интерактивными элементами:

- **Интерактивные элементы** предназначены для взаимодействия с пользователем. Это могут быть кнопки, которые можно нажать, ссылки, по которым можно перейти, или поля ввода, в которые можно ввести текст. Они реагируют на действия пользователя, такие как клики мышью или нажатия клавиш. Примеры таких элементов включают в себя кнопки (`<button>`), ссылки (`<a>`), поля ввода (`<input>`) и другие подобные элементы.  
     
- **Неинтерактивные элементы**, напротив, предназначены в основном для отображения информации. Они не реагируют на действия пользователя так, как это делают интерактивные элементы. Примеры включают в себя абзацы с текстом (`<p>`), элементы списка (`<li>`), табличные элементы (`<tr>`, `<td>`) и так далее.

```python
import time
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/scroll/1/')
    browser.find_element(By.TAG_NAME, 'input').send_keys(Keys.TAB)
    time.sleep(10)
```

`.send_keys(Keys.TAB)` симулирует ввод с клавиатуры. В данном случае симулируется нажатие клавиши TAB. Это может переместить фокус на следующий интерактивный элемент на странице после найденного `<input>`.

Чтобы взаимодействовать подобным образом с остальными элементами `<input>`, нам потребуется цикл `while`, если мы не знаем точного количества элементов, или цикл `for`, если точное количество элементов нам известно(не забываем фактор бесконечной загрузки элементов в боевых условиях).

```python
import time
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/scroll/1/')
    tags_input = browser.find_elements(By.TAG_NAME, 'input')

    for input in tags_input:
        input.send_keys(Keys.DOWN)
        time.sleep(1)
```

В цикле `for` код проходит по каждому найденному элементу `input` и выполняет следующие действия:

- `input.send_keys(Keys.DOWN)`: "нажимает" клавишу "Вниз" (`DOWN`) в текущем элементе `input`. Это может привести к изменению значения элемента или к другому действию, в зависимости от типа и функционала элемента.

Запустите этот код у себя, и вы увидите, что он поочередно выделяет (берет в фокус) все элементы `<input>` на странице. Страница сайта-тренажера сразу отображает весь список тегов `<input>`.

Для понимания следующего примера откройте любой степ на Степике с более чем 100 комментариями и попробуйте пролистать до самого последнего комментария. Вы увидите несколько загрузок с сервера. Приведенный выше пример с циклом `for` обработал бы только первые 17 элементов, так как они были загружены при открытии страницы. Чтобы решить эту проблему и обрабатывать все подгружаемые элементы, давайте модифицируем этот код.

```python
import time
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get(r"https://parsinger.ru/selenium/5.7/3/test/index.html")

    list_input = []  # Инициализируем пустой список для хранения обработанных элементов ввода
    while True:  # Начинаем бесконечный цикл

        # Ищем все элементы input на веб-странице и добавляем их в список input_tags
        input_tags = browser.find_elements(By.TAG_NAME, 'input')

        # Обходим каждый элемент input в списке
        for tag_input in input_tags:
            # Проверяем, не обрабатывали ли мы уже этот элемент ранее
            if tag_input not in list_input:
                # Вариант 1 Клавиша вниз
                tag_input.send_keys(Keys.DOWN)  # Отправляем клавишу "Вниз"
                
                # Вариант 2 Скроллинг к элементу перед кликом
                # browser.execute_script("return arguments[0].scrollIntoView(true);", tag_input)

                # Использование небольшой задержки для исключения ошибки недоступности элемента
                time.sleep(0.1)
                tag_input.click()  # Кликаем на элемент
                list_input.append(tag_input)  # Добавляем элемент в список обработанных элементов
```

Обратите внимание, что [страница](https://parsinger.ru/selenium/5.7/3/test/index.html) имитирует "бесконечную" ленту. Перейдите на неё вручную и прокрутите вниз, наблюдая за появляющимися HTML-тегами. В тот момент, когда вы достигнете финала прокрутки, именно так ведёт себя "бесконечная" прокрутка ([Infinite scroll](https://en.wikipedia.org/wiki/Scrolling)).

Пояснение к коду.

- Создаём пустой список `list_input`, который будет использоваться для хранения элементов `<input>`, с которыми уже произведены какие-либо действия (нажатия клавиш или клики).
    
    ```ini
    list_input = []  # Инициализируем пустой список для хранения обработанных элементов ввода
    ```
    
- Выполняем поиск всех элементов с тегом `<input>` на текущей веб-странице и сохраняет их в список `input_tags`.
    
    ```python
    input_tags = browser.find_elements(By.TAG_NAME, 'input')
    ```
    
- Перебираем каждый найденный элемент `<input>`.
    
    ```python
    for tag_input in input_tags:
    ```
    
- Проверяем, находится ли текущий элемент `tag_input` в списке `list_input`. Если элемент уже был обработан ранее, он будет в этом списке, и следующие действия с ним производиться не будут.
    
    ```python
    if tag_input not in list_input:
    ```
    
- Симулируем нажатие клавиши "Вниз" (`Keys.DOWN`) в текущем элементе `tag_input`, для прокрутки элементов вниз.
    
    ```python
    tag_input.send_keys(Keys.DOWN)  # Отправляем клавишу "Вниз"
    ```
    
- В тексте скрипта приведен и второй вариант. Иногда элемент может быть перекрыт из-за его расположения за пределами видимой области страницы. Чтобы решить это, можно использовать метод JavaScript для скроллинга.
    
    ```bash
    browser.execute_script("arguments[0].scrollIntoView(true);", tag_input)
    ```
    
- Для того, чтобы избежать ситуации, когда происходит попытка кликнуть по элементу, который к этому еще не готов, можно использовать небольшое ожидание `time.sleep(0.1)` (Другие способы ожидания будут рассмотрены в курсе немного позже).
- Затем симулируется клик по текущему элементу `tag_input`, если это необходимо вашей задачей.
    
    ```python
    tag_input.click()  # Кликаем на элемент
    ```
    
- Наконец, текущий элемент `tag_input` добавляется в список `list_input`, чтобы в будущем не обрабатывать его повторно.
    
    ```python
    list_input.append(tag_input)  # Добавляем элемент в список обработанных элементов
    ```
    

Запустите последний пример у себя в терминале и понаблюдайте за происходящим. Всё гораздо проще, чем кажется.

#### Доступные к применению клавиши

|   |   |   |
|---|---|---|
|ADD|ALT|ARROW_DOWN|
|ARROW_LEFT|ARROW_RIGHT|ARROW_UP|
|BACKSPACE|BACK_SPACE|CANCEL|
|CLEAR|COMMAND|CONTROL|
|DECIMAL|DELETE|DIVIDE|
|DOWN|UP|ENTER|
|EQUALS|ESCAPE|F1|
|F10|F11|F12|
|F2|F3|F4|
|F5|F6|F7|
|F8|F9|HELP|
|HOME|INSERT|LEFT|
|LEFT_ALT|LEFT_CONTROL|LEFT_SHIFT|
|META|MULTIPLY|NULL|
|NUMPAD0|NUMPAD1|NUMPAD2|
|NUMPAD3|NUMPAD4|NUMPAD5|
|NUMPAD6|NUMPAD7|NUMPAD8|
|NUMPAD9|PAGE_DOWN|PAGE_UP|
|PAUSE|RETURN|RIGHT|
|SEMICOLON|SEPARATOR|SHIFT|
|SPACE|SUBTRACT|TAB|
|END|||