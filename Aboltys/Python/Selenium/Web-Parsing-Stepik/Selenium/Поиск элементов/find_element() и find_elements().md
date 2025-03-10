
Методы `.find_element()` и `find_elements()` вы будете использовать всегда при написании парсеров с помощью Selenium. Поэтому их нужно хорошо понимать.

У нас есть страница на [сайте](http://parsinger.ru/selenium/3/3.html) с очень простой структурой дерева HTML. На этой странице есть 100 блоков  
`<div class="text">`, в каждом три тега `<p>`, которые не имеют ни `class`, ни `id`. Допустим мы хотим  собрать каждый первый элемент `<p>`. Мы могли бы пройти в цикле и использовать срезы, как мы делаем с простыми списками, наверняка подумали вы.

![](https://ucarecdn.com/9ada896d-868d-4ae2-8a7f-ffa2f0d67a21/)

Давайте разбираться, почему срезы не сработают.

`.find_element()` вернет нам объект веб-элемента, который не поддерживает срезы.

Выполним следующий код:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'http://parsinger.ru/selenium/3/3.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    link = browser.find_element(By.CLASS_NAME, 'text')
    print(type(link))

>>> <class 'selenium.webdriver.remote.webelement.WebElement'>
```

Мы видим, что возвращаемый тип объекта  - это экземпляр класса,  который содержит в себе список элементов `<p>` в количестве трех штук, как показано на первом скриншоте. Но это не простой список.

Давайте посмотрим на возвращаемый объект. 

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'http://parsinger.ru/selenium/3/3.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    link = browser.find_element(By.CLASS_NAME, 'text')
    print(link)
```

Вывод:

```php-template
<selenium.webdriver.remote.webelement.WebElement (session="67761109be77b893aa1625e9d9ddafd4", element="5B0B853EFAAA1FE058CCA69B4278A2CE_element_2")>
```

Это объект **WebElement**, который не поддерживает срезы и работу с индексами. Давайте попробуем получить элемент с индексом **[1]** у этого объекта и посмотрим на результат. Напоминаю, мы пытаемся обратиться к элементу с индексом [1] в теге `<div class="text">`, в котором находятся три тега `<p>`.  
![](https://ucarecdn.com/fef900fe-8709-49a3-8fed-5b8221dc34a7/)

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'http://parsinger.ru/selenium/3/3.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    link = browser.find_element(By.CLASS_NAME, 'text')
    print(link[0])

```

Вывод ошибки:

```python
Traceback (most recent call last):
  File "E:\Async course\aiohttp\requests-html.py", line 8, in <module>
    print(link[1])
          ~~~~^^^
TypeError: 'WebElement' object is not subscriptable
```

Эта ошибка говорит о том, что объект типа `WebElement` не поддерживает индексацию или "срезы". В других словах, мы пытаемся использовать объект `WebElement` так, как если бы это был список или массив, но Python вам сообщает, что это недопустимо.

Так происходит, потому что все элементы `<p>`, которые мы храним в этом объекте, являются как бы одним целым. А вот извлечь из этого объекта текст очень просто, достаточно применить к нему метод `.text`.

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'http://parsinger.ru/selenium/3/3.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    link = browser.find_element(By.CLASS_NAME, 'text')
    print(link.text)
```

Вывод:

```python
191817
121314
151715
```

 `.find_element()` - Возвращает **первый** найденный элемент, соответствующий нашим критериям поиска (имеется в виду элемент веб-драйвера, который содержит внутри себя элемент/тег DOM).

 `.find_element**s**()` -  Возвращает **все** найденные элементы, соответствующие критериям поиска, и сохраняет результат в список `<class 'list'`>. Но список будет наполнен не элементами `<p>`, а элементами веб-драйвера, которые будут содержать в себе элементы DOM.

#### Как всё-таки быть, если нам нужен каждый второй или третий элемент на странице?

Мы всегда можем решить эту задачу при помощи **XPath.**

1. `.find_element(By.XPATH, "//div[@class='text']/p[2]")` - эта команда найдет второй тег `<p>` внутри первого тега `<div>` с классом `'text'`, который будет обнаружен на странице первым, и вернет его как объект WebElement.   
      
    Давай разберем, что означает каждая часть этого XPath выражения `**//div[@class='text']/p[2]**`.
    - `**//**`: Символы двойного слэша указывают на то, что нужно искать элемент на всей странице, начиная с корневого элемента.
        
    - `**div[@class='text']**`: Эта часть означает, что мы ищем элемент `<div>`, у которого атрибут `class` равен `'text'`.
        
    - `**/p[2]**`: Эта часть указывает, что мы хотим найти второй дочерний элемент `<p>` внутри ранее найденного `<div>` с классом `'text'`.
        

![](https://ucarecdn.com/dd5d212f-92c3-4fcf-b7f9-5ca9ce40bf84/)

`.find_element**s**(By.XPATH, "//div[@class='text']/p[2]")` - соответственно, вернёт все найденные элементы `<p>`, расположенные на вторых позициях, во всех найденных `<div class="text">`.

В самом XPath выражении `**//div[@class='text']/p[2]**` происходит следующее:

- `**//div[@class='text']**`: Этот фрагмент ищет _все_ `<div>` элементы с атрибутом `class`, значение которого равно `'text'`. Здесь двойной слэш `//` означает, что поиск будет осуществляться по всему дереву DOM, а не только среди дочерних элементов какого-то конкретного элемента.
    
- **`/p[2]`**: Этот фрагмент уточняет, что нам нужен именно второй `<p>` элемент внутри каждого найденного `<div>` с классом `'text'`.
    

![](https://ucarecdn.com/1d7e1517-91c7-4949-ba8a-9c44abfdbbcd/)

В итоге, `.find_elements(By.XPATH, "**//div[@class='text']****/p[2]**")` вернет список объектов `WebElement`, каждый из которых будет представлять второй `<p>` элемент внутри каждого `<div>` с классом `'text'` на странице.  
  
Пример кода:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

# URL веб-страницы для парсинга
url = 'http://parsinger.ru/selenium/3/3.html'

# Инициализируем драйвер Chrome
with webdriver.Chrome() as browser:
    # Открываем веб-страницу по заданному URL
    browser.get(url)

    # Используем метод .find_elements() для поиска всех элементов, соответствующих нашему XPath
    p_elements = browser.find_elements(By.XPATH, "//div[@class='text']/p[2]")

    # Проходимся по списку найденных элементов и выводим их текст
    for i, p_element in enumerate(p_elements):
        print(f"Текст второго p тега в {i + 1}-м div с классом 'text': {p_element.text}")
```

Это можно сделать ещё проще с использованием относительного пути XPATH.

```ini
first_p = div.find_element(By.XPATH, './p[1]')
third_p = div.find_element(By.XPATH, './p[3]')
```

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'http://parsinger.ru/selenium/3/3.html'

# Инициализация драйвера в контексте with, чтобы он закрылся после завершения работы
with webdriver.Chrome() as browser:
    # Открываем URL
    browser.get(url)
    
    # Ищем все div с классом 'text'
    divs = browser.find_elements(By.CLASS_NAME, 'text')
    
    # Проходимся по каждому div
    for i, div in enumerate(divs):
        # Получаем первый и третий теги <p> внутри каждого div
        first_p = div.find_element(By.XPATH, './p[1]')
        third_p = div.find_element(By.XPATH, './p[3]')
        
        # Выводим их текст
        print(f"Для div #{i+1}, первый p: {first_p.text}, третий p: {third_p.text}")

```

Вывод:

```less
Для div #1, первый p: 191817, третий p: 151715
Для div #2, первый p: 292827, третий p: 252725
Для div #3, первый p: 393837, третий p: 353735
Для div #4, первый p: 494847, третий p: 454745
...
...
...
```

В этом коде, XPath выражения `./p[1]` и `./p[3]` относятся к первому и третьему элементу `<p>` внутри каждого найденного `<div>` с классом `text`.

- `./` — указывает на текущий элемент, в контексте которого происходит поиск. В данном случае, текущим элементом является каждый отдельный `<div>` с классом `text`.
    
- `p[1]` и `p[3]` — это собственно фильтры, которые указывают, какой именно элемент `<p>` нам нужен. В XPath, индексация начинается с 1, так что `p[1]` это первый `<p>` элемент, а `p[3]` это третий.
    

Таким образом, когда вы выполняете `div.find_element(By.XPATH, './p[**1**]')`, вы ищете первый тег `<p>` внутри текущего `<div>` с классом `text`. Аналогично, `div.find_element(By.XPATH, './p[**3**]')` находит третий тег `<p>` внутри этого же `<div>`.

Эти выражения позволяют вам очень гибко и точно указать, какие именно элементы вам нужны, не прибегая к использованию циклов и сложных срезов.