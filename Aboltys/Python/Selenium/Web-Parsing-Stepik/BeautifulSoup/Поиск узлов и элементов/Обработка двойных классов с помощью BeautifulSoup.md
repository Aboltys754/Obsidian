Одной из распространенных задач при работе с веб-страницами является поиск элементов по их классам. Если у элемента несколько классов, возникает необходимость в правильной обработке таких случаев.

```php-template
<!DOCTYPE html>
<html lang="ru">
<head>
    <title>Тестовая страница</title>
</head>
<body>
    <div class="class1 class2">Элемент 1</div>
    <div class="class1 class3">Элемент 2</div>
    <div class="class2 class3">Элемент 3</div>
</body>
</html>
```

### Извлечение элементов с двойными классами

Загрузим наш HTML-документ:

```php-template
from bs4 import BeautifulSoup

html = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <title>Тестовая страница</title>
</head>
<body>
    <div class="class1 class2">Элемент 1</div>
    <div class="class1 class3">Элемент 2</div>
    <div class="class2 class3">Элемент 3</div>
</body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')
```

Для поиска элементов с двойными классами можно использовать следующий синтаксис:

```python
elements = soup.find_all('div', class_='class1 class2')

# В нашем HTML-документе найдём один элемент 

[<div class="class1 class2">Элемент 1</div>]
```

Следует помнить, что порядок классов важен. Если вы ищете элементы с классами "**class1** **class2**", то элементы с классами "**class2** **class1**" не будут найдены.

Если порядок классов не важен, можно использовать CSS-селекторы:

```python
elements = soup.select('div.class2.class1')

# В нашем HTML-документе найдём тот же элемент

[<div class="class1 class2">Элемент 1</div>]
```

С использованием этого метода элементы будут найдены независимо от порядка классов.

Если нужно найти элементы, которые имеют хотя бы один из указанных классов.

```applescript
elements = soup.find_all('div', class_=['class1', 'class2'])

# Найдём элементы, имеющие хотя бы один из искомых классов

[<div class="class1 class2">Элемент 1</div>, <div class="class1 class3">Элемент 2</div>, <div class="class2 class3">Элемент 3</div>]
```