`soup.**find_all()**` - это метод Beautiful Soup, который ищет все элементы в HTML-документе, соответствующие переданным параметрам. Возвращает список элементов Beautiful Soup, которые удовлетворяют условиям поиска.

Синтаксис:

`soup.**find_all**(**name**, **attrs={}**, **recursive=True**, **string=None**, **limit=None**, **kwargs)`

Параметры:

- `**name**` - имя тега HTML, который нужно найти. Может быть строкой с именем тега, регулярным выражением, списком имен тегов и другими типами фильтров. Опциональный параметр.
- `**attrs={}**` - словарь атрибутов и их значений, которые нужно найти. Опциональный параметр.
- `**recursive=True**` - определяет, будут ли поиск проводиться рекурсивно по всем вложенным элементам или только среди прямых потомков. Если `True`, поиск будет проводиться по всем дочерним элементам, если `False` — только среди прямых потомков. По умолчанию установлено значение `True`. Опциональный параметр.
- `**string=None**` - параметр используется для поиска элементов с определенным текстом. Может быть строкой, регулярным выражением и другими типами фильтров. Если параметр `string` не установлен или установлен в `None`, то текстовое содержимое элементов не учитывается при поиске. Опциональный параметр.
- `**limit=None**` - максимальное количество элементов, которые будут найдены. Например, если установлено `limit=2`, `find_all` вернет не более двух элементов. `None` - поиск будет происходить без ограничений на количество возвращаемых элементов. Опциональный параметр.

### **Пример 1**

Код ищет теги `<p>` с помощью метода `find_all()`.

```python
result = soup.find_all('p')
```

Также происходит поиск тегов `<p>` с атрибутами `class='text-class'` и `id='text-id'`.

```python
result = soup.find_all('p', attrs={'class': 'text-class'})
```

Текст каждого найденного тега выводится в консоль.

```python
for tag in result:
    print(tag.text)
```

```python
soup = BeautifulSoup(html, 'html.parser')

# Найти все теги `p`
result = soup.find_all('p')
for tag in result:
    print(tag.text)

print('----разделитель----')

# Найти все теги `p` с атрибутом class='text-class'
result = soup.find_all('p', attrs={'class': 'text-class'})
for tag in result:
    print(tag.text)

print('----разделитель----')

# Найти все теги `p` с атрибутом id='text-id'
result = soup.find_all('p', attrs={'id': 'text-id'})
for tag in result:
    print(tag.text)
```

### **Пример 2**

Используем метод `.find_all` для поиска всех тегов `<a>` с атрибутом `href`.Результат записывается в переменную `result`

```python
result = soup.find_all('a', href=True)
```

Далее в цикле `for` перебирается список тегов и выводится значение атрибута `href` и текст внутри тега.

```python
soup = BeautifulSoup(html, 'html.parser')

# Найти все теги `a` с атрибутом href
result = soup.find_all('a', href=True)
for tag in result:
    print(tag['href'], tag.text)
```

### **Пример 3 с применением `recursive=True`**

Код ищет все теги `<p>` в HTML-документе, включая те, что находятся внутри вложенных тегов, используя метод `find_all()` с параметром `recursive=True`. Наконец, эти теги выводятся в консоль.

```python
from bs4 import BeautifulSoup

html_doc = """
<html>
    <head>
        <title>Example Page</title>
    </head>
    <body>
        <div id="main">
            <h1>Hello World</h1>
            <p class="info">This is a paragraph.</p>
            <p class="info">This is another paragraph.</p>
            <ul>
                <li>Item 1</li>
                <li>Item 2</li>
                <li>Item 3</li>
            </ul>
        </div>
        <div id="secondary">
            <p>Some additional information.</p>
        </div>
    </body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# Найти все теги p в HTML-документе, включая те, что находятся внутри вложенных тегов.
all_p_tags = soup.find_all('p', recursive=True)
print(all_p_tags)
```

### **Пример 4 с применением `text`**

Код ищет все теги `'p'`, содержащие текст `'Текст 1'` или содержащие текст, содержащий `'Текст'` с помощью метода `.find_all()`. Найденные теги перебираются в цикле и выводится их текст.

```python
soup = BeautifulSoup(html, 'html.parser')

# Найти все теги `p` с текстом 'Текст 1'
result = soup.find_all('p', text='Текст 1')
for tag in result:
    print(tag.text)

print('----разделитель----')

# Найти все теги `p` с текстом, содержащим 'Текст'
result = soup.find_all('p', text=lambda x: 'Текст' in x)
for tag in result:
    print(tag.text)
```

### **Пример 5**

С помощью метода `find_all()` ищутся все теги `p` с указанными атрибутами `class` или `id`. Найденные теги циклом перебираются, а текст каждого тега выводится в консоль.

```python
# Найти все теги `p` с классом `text-class`
result = soup.find_all('p', {'class': 'text-class'})
for tag in result:
    print(tag.text)

print('----разделитель----')

# Найти все теги `p` с атрибутом `class`
result = soup.find_all('p', class_=True)
for tag in result:
    print(tag.text)

print('----разделитель----')

# Найти все теги `p` с атрибутом `id`
result = soup.find_all('p', id=True)
for tag in result:
    print(tag.text)
```