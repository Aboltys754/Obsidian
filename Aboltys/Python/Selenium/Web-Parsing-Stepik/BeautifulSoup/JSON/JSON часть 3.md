В этой части мы поговорим о том, как извлекать значения атрибута. Именно его значение, а не текст, который заключен в теге. Этим методом можно собирать любые значения атрибутов, `class=""`, `name=""`, `src=""`, `href=""`, `id=""`, не имеет значения какой тег. Чтоб далеко не ходить, мы будем тренироваться на нашем [тренажёре](http://parsinger.ru/html/watch/1/1_1.html).

![](https://ucarecdn.com/cbef70c3-7476-4d7a-988e-d0a9c2f5f815/)

В результате выполнения кода у нас получится вот такой список:  `['brand', 'model', 'type', 'display', 'material_frame', 'material_bracer', 'size', 'site']`. Это понадобится вам для решения задачи, которая ждет вас далее.

```python
import requests
from bs4 import BeautifulSoup

response = requests.get('http://parsinger.ru/html/watch/1/1_1.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
description = soup.find('ul', id='description').find_all('li')

for li in description:
    print(li['id'])


>>> brand
    model
    type
    display
    material_frame
    material_bracer
    size
    site
```

В первую очередь нам необходимо найти и получить родительский элемент, в этом примере это `<ul id="description">`, `description = soup.find('ul', id='description').find_all('li')` - будет хранить список всех дочерних элементов `<li>`, давайте на них посмотрим.

![](https://ucarecdn.com/64e9ae38-6b8b-45b9-816a-6fb3502ace68/)

Далее мы проходимся по каждому элементу в этом списке и обращаемся с ним как с элементами словаря - `li['id']`. Мы можем добавлять элементы в список на каждой итерации, а можем использовать **list comprehension** `li_id = [x['id'] for x in description]` и получить готовый список без лишнего кода.

```python
import requests
from bs4 import BeautifulSoup

response = requests.get('http://parsinger.ru/html/watch/1/1_1.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
description = soup.find('ul', id='description').find_all('li')
li_id = [x['id'] for x in description]
print(li_id)


>>> ['brand', 'model', 'type', 'display', 'material_frame', 'material_bracer', 'size', 'site']
```