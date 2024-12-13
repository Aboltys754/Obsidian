Давайте разберем еще один пример кода по извлечению данных с сайта и формированию словаря для дальнейшего дампа в `.json.`

```python
import requests
from bs4 import BeautifulSoup
import json

# 1 ------------------------------------------------------
url = 'http://parsinger.ru/html/index3_page_1.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
# 1 ------------------------------------------------------

# 2 ------------------------------------------------------
name = [x.text.strip() for x in soup.find_all('a', class_='name_item')]
description = [x.text.strip().split('\n') for x in soup.find_all('div', class_='description')]
price = [x.text for x in soup.find_all('p', class_='price')]
# 2 ------------------------------------------------------

result_json = []
# 3 ------------------------------------------------------
for list_item, price_item, name in zip(description, price, name):
    result_json.append({
        'name': name,
        'brand': [x.split(':')[1] for x in list_item][0],
        'type': [x.split(':')[1] for x in list_item][1],
        'connect': [x.split(':')[1] for x in list_item][2],
        'game': [x.split(':')[1] for x in list_item][3],
        'price': price_item

    })

# 3 ------------------------------------------------------

# 4 ------------------------------------------------------
with open('res.json', 'w', encoding='utf-8') as file:
    json.dump(result_json, file, indent=4, ensure_ascii=False)
# 4 ------------------------------------------------------
```

В этом коде активно применялись list comprehension для извлечения необходимых данных и формирования списка словарей.

1. В блоке №1 нет ничего нового для вас;
2. В блоке №2 мы извлекаем информацию с каждой карточки на сайте [тренажёре](http://parsinger.ru/html/index3_page_1.html), извлекаем наименование товара, его описание и стоимость. Если мы посмотрим на элементы страницы HTML, мы увидим,  что `description`  извлекается методом `find_all()` и получается список списков, который необходимо записать в наш список словарей;
3. В этом блоке мы инициируем цикл, в котором проходимся по трём основным спискам, мы создали их в блоке 2, и на каждой итерации записываем значение в соответствующий ключ нашего словаря. 

В результате выполнения этого кода мы получаем файл `res.json` в каталоге с нашим проектом, который выглядит вот так:

![](https://ucarecdn.com/19bb0a82-cd51-4b84-8d2f-21681e010228/)