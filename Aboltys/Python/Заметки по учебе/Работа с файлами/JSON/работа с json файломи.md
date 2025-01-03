[[#Синтаксис json формата]]
[[#Модуль json]]
- [[#Функция dumps()]]
- [[#Функция dump()]]
- [[#Необязательные аргументы indent, sort_keys и separators]]
- [[#Функция loads()]]
- [[#Функция load()]]
[[#Типы данных в json]]
- [[#Изменение типа данных]]
- [[#Ограничение по типам данных]]
- [[#Кириллические символы в json]]
## Синтаксис json формата

Значениями в `json` формате могут быть не только строки. Это могут быть числа, списки значений, литералы `true/false/null`, а также вложенные объекты:

```python
{ 
 "firstName": "Тимур", 
 "lastName": "Гуев", 
 "age": 29, 
 "gender": "мужской", 
 "smoke": false, 
 "address": { 
			 "streetAddress": "Часовая 25, кв. 127", 
			 "city": "Москва", 
			 "postalCode": 125315 
			 }, 
"phoneNumbers": ["+7 (919) 424-84-34", "+7 (916) 928-92-34"] 
}
```
Вложенность данных может быть бесконечной. То есть значением ключа может быть список, а элементом этого списка — объект и т.д

В формате JSON используются только двойные кавычки.

Итак, в качестве значений в JSON могут быть использованы:
- число (целое или вещественное)
- литералы `true` (истина), `false` (ложь), `null` (отсутствие значения)
- строка (последовательность символов, заключенная в двойные кавычки)
- список (заключается в квадратные скобки `[ ]`, значения разделяются запятыми). Список может быть пустым, значения в пределах одного списка могут иметь разный тип
- вложенный объект (неупорядоченное множество пар ключ: значение, заключённое в фигурные скобки `{ }`). Ключ описывается строкой, между ним и значением стоит символ `:`. Пары ключ-значение отделяются друг от друга запятыми.


JSON — это текстовый формат, который может быть представлен не только в виде пар ключ-значение. Он так же может содержать список, строку, число и т.д. Но чаще всего используется структура ключ-значение

## Модуль json

Преобразование переменных программы (Python-объектов) в формат для хранения называется «сериализацией», а обратное преобразование — «десериализацией». В Python для сериализации и десериализации в формат `json` есть модуль, который так и называется — `json`

### Функция dumps()
Для сериализации данных в `json` строку используется функция `dumps()` из модуля `json`. Для того, чтобы сериализовать данные с ее помощью, достаточно передать в нее аргументом любой сериализуемый Python объект.
Так как `json` — текстовый формат, то сериализация в него — это по сути преобразование данных в строку.

```python
import json
data = {'name': 'Russia', 'phone_code': 7, 'capital': 'Moscow', 'currency': 'RUB'}
json_data = json.dumps(data)            # сериализуем словарь data в json строку

print(type(json_data))
print(json_data)
```
выводит:
```no-highlight
<class 'str'>
{"name": "Russia", "phone_code": 7, "capital": "Moscow", "currency": "RUB"}
```
### Функция dump()
В отличие от функции `dumps()`, которая преобразует (сериализует) Python объект в `json` строку, функция `dump()` записывает переданный Python объект в файл.
```python
import json 
data = {'name': 'Russia', 'phone_code': 7, 'capital': 'Moscow', 'currency': 'RUB'} 
with open('countries.json', 'w') as file: 
	json.dump(data, file)
```
создает файл `countries.json` и сохраняет в него информацию из словаря `data` в `json` формате.
Если открыть файл `countries.json`, мы увидим, что `json` выведен в одну строку без форматирования:
```json
{"name": "Russia", "phone_code": 7, "capital": "Moscow", "currency": "RUB"}
```
### Необязательные аргументы indent, sort_keys и separators

Функции записи `dumps()` и `dump()` имеют необязательные аргументы `indent`, `sort_keys` и `separators`, которые можно использовать для более удобного чтения человеком.

Аргумент `indent` задает отступ от левого края. По умолчанию имеет значение `None` для более компактного представления без отступов.

```python
import json
data = {'name': 'Russia', 'phone_code': 7, 'capital': 'Moscow', 'currency': 'RUB'}

json_data1 = json.dumps(data, indent=2)
json_data2 = json.dumps(data, indent=10)

print(json_data1)
print(json_data2)
```
выводит:
```no-highlight
{
  "name": "Russia",
  "phone_code": 7,
  "capital": "Moscow",
  "currency": "RUB"
}
{
          "name": "Russia",
          "phone_code": 7,
          "capital": "Moscow",
          "currency": "RUB"
}
```
Если значением `indent` является строка, то она используется в качестве отступа.

```python
import json
data = {'name': 'Russia', 'phone_code': 7, 'capital': 'Moscow', 'currency': 'RUB'}
json_data = json.dumps(data, indent='++++')

print(json_data)
```
выводит:
```no-highlight
{
++++"name": "Russia",
++++"phone_code": 7,
++++"capital": "Moscow",
++++"currency": "RUB"
}
```
Отступов также не будет, если значение аргумента `indent` равно 00, отрицательному числу или пустой строке.

Аргумент `sort_keys` задает сортировку ключей в результирующем `json`. По умолчанию имеет значение `False` для более быстрого создания `json`. Если установить значение аргумента в `True`, то ключи будут отсортированы в алфавитном порядке, что особенно удобно, когда ключей много.

```python
import json
data = {'name': 'Russia', 'phone_code': 7, 'capital': 'Moscow', 'currency': 'RUB'}
json_data1 = json.dumps(data, indent=3)
json_data2 = json.dumps(data, indent=3, sort_keys=True)

print(json_data1)
print(json_data2)
```
выводит:
```json
{
   "name": "Russia",
   "phone_code": 7,
   "capital": "Moscow",
   "currency": "RUB"
}
{
   "capital": "Moscow",
   "currency": "RUB",
   "name": "Russia",
   "phone_code": 7
}
```
Аргумент `separators` задает кортеж, состоящий из двух элементов `(item_separator, key_separator)`, которые представляют разделители для элементов и ключей.  По умолчанию аргумент имеет значение `(', ', ': ')`.

```python
import json
data = {'name': 'Russia', 'phone_code': 7, 'capital': 'Moscow', 'currency': 'RUB'}
json_data = json.dumps(data, indent=3, separators=(';', ' = '))

print(json_data)
```
выводит:
```json
{
   "name" = "Russia";
   "phone_code" = 7;
   "capital" = "Moscow";
   "currency" = "RUB"
}
```
### Функция loads()

Для десериализации данных нужно использовать функцию `loads()`. Ее аргумент — это строка с данными в формате `json`.
```python
import json
json_data = '{"name": "Russia", "phone_code": 7, "capital": "Moscow", "currency": "RUB"}'
data = json.loads(json_data)
print(type(data))
print(data)
```
выводит:
```no-highlight
<class 'dict'>
{'name': 'Russia', 'phone_code': 7, 'capital': 'Moscow', 'currency': 'RUB'}
```
В случае если строка для десериализации содержит данные с ошибкой, то модуль `json` не сможет правильно прочитать такую строку, и программа завершится с ошибкой.
```
json.decoder.JSONDecodeError
```
### Функция load()
В отличие от функции `loads()`, которая в качестве аргумента принимает строку с данными в формате `json`, функция `load()` принимает файловый объект и возвращает его десериализованное содержимое.
Пусть файл `data.json` имеет следующее содержимое:
```json
{
  "name": "Russia",
  "phone_code": 7,
  "capital": "Moscow",
  "cities": ["Abakan", "Almetyevsk", "Anadyr", "Anapa", "Arkhangelsk", "Astrakhan"],
  "currency": "RUB"
}
```
Приведенный ниже код:
```python
import json
with open('data.json') as file:
    data = json.load(file)                # передаем файловый объект
    for key, value in data.items():
        if type(value) == list:
            print(f'{key}: {", ".join(value)}')
        else:
            print(f'{key}: {value}')
```
читает содержимое `data.json` файла в словарь `data` и выводит его содержимое:

```no-highlight
name: Russia
phone_code: 7
capital: Moscow
cities: Abakan, Almetyevsk, Anadyr, Anapa, Arkhangelsk, Astrakhan
currency: RUB
```
## Типы данных в json
```python
import json
json_data = '''
{
   "name": "Russia",
   "phone_code": 7,
   "latitude": 60.0,
   "capital": "Moscow",
   "timezones": ["Anadyr", "Barnaul", "Moscow", "Kirov"],
   "translations": {
      "nl": "Rusland",
      "hr": "Rusija",
      "de": "Russland",
      "es": "Rusia",
      "fr": "Russie",
      "it": "Russia"
   }
}'''

data = json.loads(json_data)

print(type(data['name']))
print(type(data['phone_code']))
print(type(data['latitude']))
print(type(data['timezones']))
print(type(data['translations']))
```
выводит:
```no-highlight
<class 'str'>
<class 'int'>
<class 'float'>
<class 'list'>
<class 'dict'>
```
Таким образом модуль `json` автоматически определяет тип значения при десериализации. Такая автоматическая работа с типами данных выгодно отличает `json` от `csv`, при работе с которым таких автоматических преобразований нет.
### Изменение типа данных
Еще один важный аспект преобразования данных в формат JSON: данные не всегда будут того же типа, что исходные данные в Python. Например, кортежи при записи в JSON превращаются в списки.

Приведенный ниже код:
```python
import json
data = {
        'name': 'Russia', 
        'phone_code': 7,
        'latitude': 60.0,
        'capital': 'Moscow',
        'timezones': ('Anadyr', 'Barnaul', 'Moscow', 'Kirov')
       }

json_data = json.dumps(data)        # преобразуем dict в json
new_data = json.loads(json_data)    # преобразуем json в dict

print(data == new_data)
```
выводит:
```python
False
```

Так происходит из-за того, что в JSON используются другие типы данных, и не для всех типов данных Python есть соответствия.

Таблица конвертации типов данных Python в JSON:

|Python|JSON|
|---|---|
|`dict`|`object`|
|`list, tuple`|`array`|
|`str`|`string`|
|`int, float`|`number`|
|`True`|`true`|
|`False`|`false`|
|`None`|`null`|

Таблица конвертации JSON в типы данных Python:

|JSON|Python|
|---|---|
|`object`|`dict`|
|`array`|`list`|
|`string`|`str`|
|`number (int)`|`int`|
|`number (real)`|`float`|
|`true`|`True`|
|`false`|`False`|
|`null`|`None`|

### Ограничение по типам данных

В формат JSON нельзя записать словарь, у которого ключи – кортежи.
```python
import json
data = {
        'beegeek': 2018,
        ('Timur', 'Guev'): 29,
        ('Arthur', 'Kharisov'): 20,
        'stepik': 2013
       }
json_data = json.dumps(data)        # преобразуем dict в json

print(json_data)
```
генерирует ошибку:
```no-highlight
TypeError: keys must be str, int, float, bool or None, not tuple
```
С помощью необязательного аргумента `skipkeys` можно игнорировать подобные ключи.

```python
import json
data = {
        'beegeek': 2018,
        ('Timur', 'Guev'): 29,
        ('Arthur', 'Kharisov'): 20,
        'stepik': 2013
       }

json_data = json.dumps(data, skipkeys=True)        # преобразуем dict в json

print(json_data)
```
выводит:
```json
{"beegeek": 2018, "stepik": 2013}
```
Кроме того, в JSON ключами словаря могут быть только строки. Но, если в словаре Python использовались числа, булевы значения или None, то ошибки не будет, вместо этого они будут преобразованы в строки.
```python
import json

data = {1: 'Timur', False: 'Arthur', None: 'Ruslan'}
json_data = json.dumps(data)

print(json_data)
```
выводит:
```json
{"1": "Timur", "false": "Arthur", "null": "Ruslan"}
```
## Кириллические символы в json
```python
import json

data = {'firstName': 'Тимур', 'lastName': 'Гуев'}
s = json.dumps(data)
print(s)
```
выводит:
```no-highlight
{"firstName": "\u0422\u0438\u043c\u0443\u0440", "lastName": "\u0413\u0443\u0435\u0432"}
```
Результат, скорее всего, будет неожиданным. Каждая буква из строк `Тимур` и `Гуев` будет заменена на ее код. Эти коды стандартны, и код для каждой из букв индивидуален. Например. `0438` — код буквы `и`.  А на [этой](https://www.fileformat.info/info/unicode/char/0438/index.htm) странице можно посмотреть полное описание этого кода и символа.

Обратное преобразование из строки в словарь вернет закодированное значение в первоначальный вид.
```python
import json

data = {'firstName': 'Тимур', 'lastName': 'Гуев'}
s = json.dumps(data)
print(s)
result = json.loads(s)
print(result)
```
выводит:
```no-highlight
{"firstName": "\u0422\u0438\u043c\u0443\u0440", "lastName": "\u0413\u0443\u0435\u0432"}
{'firstName': 'Тимур', 'lastName': 'Гуев'}
```
Благодаря стандартным кодам, символы будут прочитаны и преобразованы в нужный вид любой программой на любом языке программирования.

С помощью необязательного аргумента `ensure_ascii` функций `dumps()` и `dump()` можно отказаться от такого кодирования.
```python
import json

data = {'firstName': 'Тимур', 'lastName': 'Гуев'}
s = json.dumps(data, ensure_ascii=False)
print(s)
result = json.loads(s)
print(result)
```
выводит:
```no-highlight
{"firstName": "Тимур", "lastName": "Гуев"}
{'firstName': 'Тимур', 'lastName': 'Гуев'}
```

Python преобразует такую строку обратно в словарь без проблем (поскольку использует Unicode по умолчанию), но нужно помнить, что это может привести к проблемам с преобразованием в программах, написанных на других языках программирования.



## Примечания

**Примечание 1.** Официальная документация по формату `json` доступна по [ссылке](https://www.json.org/json-ru.html).

**Примечание 2.** Официальная документация по модулю `json` в Python доступна по [ссылке](https://docs.python.org/3.10/library/json.html).

**Примечание 3.**  На [сайте](https://pymotw.com/3/json/index.html) очень хорошо расписан модуль `json`.

**Примечание 4.** JSON – это текстовый формат, что означает, что мы должны открыть файл в текстовом режиме и указать кодировку. Вы никогда не ошибетесь, используя UTF-8.

**Примечание 5.** Мы можем сериализовать любой объект, поддерживаемый форматом `json`, например число, список, строку и т.д.

Приведенный ниже код:

```python
import json

colors = ['white', 'red', 'black']

with open('list.json', 'w') as file:
    json.dump(colors, file, indent='---')
```

создает файл `list.json` со следующим содержанием:

```no-highlight
[
---"white",
---"red",
---"black"
]
```

**Примечание 6.** В формате `json` ключом может быть только строка (регистрозависимость не регулируется стандартом, это остаётся на усмотрение программного обеспечения). Как правило, регистр учитывается программами — имена с буквами в разных регистрах считаются разными. Повторяющиеся имена ключей допустимы, но не рекомендуются стандартом; обработка таких ситуаций происходит на усмотрение программного обеспечения, возможные варианты — учитывать только первый такой ключ, учитывать только последний такой ключ, генерировать ошибку.

Приведенный ниже код:

```python
import json

data = {'firstName': 'Тимур', 'lastName': 'Гуев', 'firstName': 'Теймур', 'FirstName': 'Тим'}
s = json.dumps(data, ensure_ascii=False)
print(s)
```

выводит:

```json
{"firstName": "Теймур", "lastName": "Гуев", "FirstName": "Тим"}
```

**Примечание 7.** JSON обладает рядом преимуществ, которые и сделали его популярным:

1. не занимает много места, является компактным в написании и быстро компилируется
2. создание текстового содержимого понятно человеку, просто в реализации, а чтение со стороны среды разработки не вызывает никаких проблем. Чтение может осуществляться и человеком, поскольку ничего сложного в представлении данных нет
3. структура преобразуется для чтения на любых языках программирования
4. практически все языки имеют соответствующие библиотеки или другие инструменты для чтения данных JSON

**Примечание 8.** Для удобного форматирования `json` файлов используйте [сайт](https://jsonformatter.curiousconcept.com/).

**Примечание 9.** Оба формата, как `csv`, так и `json`**,** очень популярны. Модули для работы с ними есть практически в каждом языке программирования. Также многие популярные прикладные программы поддерживают импорт и экспорт в эти форматы. Понимать, как устроены и как работать с этими двумя форматами, просто жизненно необходимо современному программисту.

**Примечание 10.** В последнее время очень распространились веб-приложения на JavaScript, JSON стал одним из самых популярных форматов, в том числе и в других языках. JSON (англ. JavaScript Object Notation) — один из самых популярных типов структурированных файлов, поддерживающих произвольную вложенность. Это формат объекта в языке JavaScript, содержащий в себе сочетание словарей и списков (в терминах Python). На самом деле все из вас пользовались данным форматом, пусть и неявно. Именно JSON обмениваются большинство приложений в Интернете.

**Примечание 11.** Мы производили преобразования между объектами языка Python и `json` объектами. Такие преобразования называются **сериализацией** (кодирование в `json` формат, то есть в поток байт) и **десериализацией** (декодирование в объект языка).

**Примечание 12.** Есть еще несколько моментов при работе с JSON, о которых стоит помнить:

1. чтобы не возникали проблемы с кодировкой, если в файл передаются данные с русскими буквами, как и во всех других случаях работы с файлом, при открытии нужно принудительно устанавливать кодировку (особенно актуально для OS семейства Windows):
    
    ```python
    with open('cats_3.json', 'w', encoding='utf8') as cat_file:
        cat_file.write(json.dumps(cats_dict))
    ```
    
2. при создании `json` файла «вручную» нужно помнить, что в нем нельзя использовать одинарные кавычки. При создании программными средствами нужные кавычки ставятся автоматически
3. ключами словаря в `json` не могут быть кортежи и числа. Но ключ-число не вызовет ошибку при сериализации, он будет просто преобразован в строку
4. помните, что при преобразовании данные будут не всегда того же типа, что были в Python


Функция для валидации json файла
```python
def is_correct_json(string: str):
    try:
        json.loads(string)
        return True
    except Exception:
        return False
```