
[JSON](https://www.json.org/json-en.html) - **(англ. JavaScript Object Notation)** — текстовый формат обмена данными, основанный на **JavaScript**. При этом формат независим от **JS** и может использоваться в любом языке программирования.

**JSON** входит в стандартный пакет python, устанавливать его не нужно, достаточно просто импортировать  `import json`

Сегодня мы будем рассматривать **JSON** с точки зрения сохранения информации. В этом уроке мы будем говорить о JSON-объектах: как их создавать, сохранять, генерировать и как манипулировать ими.

**JSON**-объект выглядит так, заключается в фигурные скобки. Он очень похож на словарь в Python, если вы с ними уже знакомы, то освоить этот раздел будет очень просто.

```json
[{
"name": "Иван",
"age": 27
}]
```

`"name"` - это ключ(**key**), а `"Иван"` - это значение(**value**),  ключ и значение разделяются двоеточием, каждая пара ключ:значение, отделены друг от друга запятой.

Значение(**value**) может быть...

- Строкой;
- Числом;
- True или False;
- Null;
- Другим объектом, в том числе списком или словарем и может иметь какую угодно вложенность. 

Один из простых примеров генерирования **JSON** объекта во время парсинга(#2):

```python
import requests
from bs4 import BeautifulSoup
import json

# 1 ------------------------------------------------------
url = 'http://parsinger.ru/html/mouse/3/3_11.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
# 1 ------------------------------------------------------

# 2 ------------------------------------------------------
result_json = {
    'name': soup.find('p', id='p_header').text,
    'price': soup.find('span', id='price').text}
# 2 ------------------------------------------------------

# 3 ------------------------------------------------------
with open('res.json', 'w', encoding='utf-8') as file:
    json.dump(result_json, file, indent=4, ensure_ascii=False)
# 3 ------------------------------------------------------


>>> {
    "name": "Мышь Logitech G PRO HERO Black USB проводная",
    "price": "5100 руб"
}
```

В результате выполнения кода мы получили аккуратно собранные данные, которые мы запрашивали во время парсинга:

1. В этом блоке мы совершили `get` запрос на страницу и передали результат запроса в конструктор `BeautifulSoup`;
2. Создали простой словарь `result_json={}` , вручную обозначили ключи, а значения для словаря мы получили из объекта `soup` с помощью тегов;
3. В менеджере контекста `with`  обозначили название файла с расширением `.json`, указали кодировку `"utf-8"`.

### Методы `JSON`:

- `json.dump()` - преобразует объекты **python** (в нашем примере это словарь) в соответствующий объект **JSON**. Метод `.dump()` первым параметром ожидает словарь, который мы будем записывать в файл, а вторым параметром - файл, куда мы будем записывать наш словарь.
- 1. `indent=4` улучшает читаемость файла `json`, и обозначает отступ в пробелах;
    2. `ensure_ascii=False` - если не указать, могут возникнуть проблемы с кодировкой. Если установить значение `True`, то кириллические символы будут отображены в **ascii**, примерно вот так `\u041c\u044b\u0448\u044c`.
- `json.dumps()` - отличается лишь тем, что кодирует наши данные в **Python string**  и служит для преобразования примитивных типов данных. В ваших парсерах вы, скорее всего, будете использовать именно первый вариант;
- `json.load()` - метод считывает файл в формате **JSON** и возвращает объекты Python, про метод **load()** подробнее мы поговорим позже когда, будем считывать **json**-файлы;
- `json.load**s**()` - метод считывает **строку** в формате JSON и возвращает объекты Python.