
`tag.parent` - это свойство объекта Beautiful Soup, которое используется для получения родительского элемента (тега) текущего элемента в HTML-документе. Когда вы вызываете `.parent` для конкретного элемента, он возвращает родительский элемент этого тега.

### **Пример:**

```python
from bs4 import BeautifulSoup

html = '''
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Пример .parent</title>
</head>

<body>
<div id="parent-container">
    <h1 id="main-heading">Заголовок (.parent)</h1>
    <p id="paragraph">Текст абзаца ()</p>
    
    <ul id="list">
        <li class="list-item">Элемент списка 1</li>
        <li class="list-item">Элемент списка 2</li>
    </ul>
</div>

</body>
</html>

'''

soup = BeautifulSoup(html, "html.parser")
li_elem = soup.find('li', class_='list-item')
parent_elem = li_elem.parent

# Выводим содержимое родительского элемента
print(parent_elem)
```

```bash
soup.find('li', class_='list-item')  # Находим элемент <li> с классом .list-item
```

```ini
parent_elem = li_elem.parent # Получаем родительский элемент с помощью .parent
```

В данном примере будет найден родительский элемент `<ul>` с идентификатором `"list"`, будет найден сам тег и его дети(**child**) т.е. все вложенные элементы `<li>`.