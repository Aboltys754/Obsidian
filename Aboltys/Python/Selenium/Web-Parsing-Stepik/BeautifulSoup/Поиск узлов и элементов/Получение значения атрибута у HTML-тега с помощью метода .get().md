
`tag.get(key, default=None)` - в BeautifulSoup используется для получения значения атрибута у HTML-тега. Этот метод предлагает безопасный и удобный способ доступа к атрибутам, возвращая `None`, если атрибут отсутствует, что помогает избежать ошибок.  
Метод `.get()` применяется к объектам типа `bs4.element.Tag` и позволяет получить значение указанного атрибута.  
Синтаксис:

```csharp
tag.get('attribute_name')
```

где, `'attribute_name'` - имя атрибута, значение которого вы хотите получить.  
  
**Пример 1**: Получение ссылки из тега `<a>`

```python
from bs4 import BeautifulSoup

html_doc = '<a href="https://example.com">Visit example.com</a>'
soup = BeautifulSoup(html_doc, 'html.parser')

a_tag = soup.find('a')
href_value = a_tag.get('href')

print("Href value:", href_value)  # Href value: https://example.com
```

В этом примере демонстрировалось получение значение атрибута `href` у первого тега `<a>`.  
 

**Пример 2**: Извлечение данных из пользовательского атрибута

```python
html_doc = '<div data-info="12345">Some content</div>'
soup = BeautifulSoup(html_doc, 'html.parser')

div_tag = soup.find('div')
data_info = div_tag.get('data-info')

print("Data-info value:", data_info)  # Data-info value: 12345
```

Здесь метод `.get()` был использован для получения значения пользовательского атрибута `data-info`.  
 

**Пример 3**: Попытка получить несуществующий атрибут

```bash
html_doc = '<p>Simple paragraph</p>'
soup = BeautifulSoup(html_doc, 'html.parser')

p_tag = soup.find('p')
class_attr = p_tag.get('class')

print("Class attribute:", class_attr)  # Class attribute: None
```

Поскольку у тега `<p>` нет атрибута `class`, метод `.get()` вернул `None`.  
  
Метод `.get()` особенно полезен в ситуациях, где атрибут может отсутствовать, поскольку в таких случаях метод предотвращает возникновение ошибок, возвращая `None`.