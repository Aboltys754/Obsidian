ля следующего примера нам понадобится [jsonplaceholder](https://jsonplaceholder.typicode.com/posts), сервис, который предоставляет JSON для разработчиков. У него есть 6 ресурсов -. [/posts](https://jsonplaceholder.typicode.com/posts), [/comments](https://jsonplaceholder.typicode.com/comments), [/albums](https://jsonplaceholder.typicode.com/albums), [/photos](https://jsonplaceholder.typicode.com/photos), [/todos](https://jsonplaceholder.typicode.com/todos),  [/users](https://jsonplaceholder.typicode.com/users)

Давайте сделаем запрос на [/posts](https://jsonplaceholder.typicode.com/posts) и посмотрим на данные через [jsonviewer](http://jsonviewer.stack.hu/). Мы увидим 100 постов, где мы можем извлечь четыре поля: `"userId"`, `"id"`, `"title"`, `"body"`. Если мы хотим получить какой-либо определенный элемент, мы должны указать его в квадратных скобках- `["title"]`.

![](https://ucarecdn.com/b4c63b18-6e02-415f-8a07-e6a618116d5b/)

Для того, чтобы получить все `'userId'` и `'title'`, мы пройдемся по всем элементам в цикле `for`:

```python
import requests

url = 'https://jsonplaceholder.typicode.com/posts'

response = requests.get(url=url).json()
for item in response:
    print(item["userId"], item["title"])


>>> 1 sunt aut facere repellat provident occaecati excepturi optio reprehenderit
    1 qui est esse
    1 ea molestias quasi exercitationem repellat qui ipsa sit au
    ...
    10 at nam consequatur ea labore ea harum
```

В результате мы получили все `"userId"` и `"title"`. Обратите внимание на метод `.json()`, применяемый к переменной `response`. Мы рассмотрели метод `.json()` в разделе, посвященном библиотеке `requests`. Данный метод позволяет сериализовать информацию, полученную с сервера, в формате JSON-объекта, при условии, что сервер готов предоставить нам эти данные.

### Вложенность JSON

Для следующего примера нам понадобится результат выполнения одной из прошлых задач. Для удобства вы можете найти его по [ссылке](http://parsinger.ru/downloads/get_json/res.json).

Наша цель — извлечь из значения ключа `'description'` вложенные ключи `'brand'` и `'model'`. Для достижения этой цели, первым в списке указывается родительский ключ, а затем — дочерний. В нашем случае, это будет выглядеть как `['description']['brand']`.

![](https://ucarecdn.com/ac6916d5-686f-42b4-a8e6-104685bf4de3/)

```python
import requests

url = 'http://parsinger.ru/downloads/get_json/res.json'

response = requests.get(url=url).json()
for item in response:
    print(item["description"]["brand"], item["description"]["model"])

>>> Jet Excidium
    Huawei Band 6 FRA-B19
    Huawei Band 6 FRA-B19
    Huawei GT 3 MIL-B19V
    ...
    HP Pavilion Gaming 600
```