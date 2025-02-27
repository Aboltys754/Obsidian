Он сохраняет объекты в файл с определенным ключом. Затем по этому ключу может извлечь ранее сохраненный объект из файла. Процесс работы с данными через модуль shelve напоминает работу со словарями, которые также используют ключи для сохранения и извлечения объектов.

Для открытия файла модуль shelve использует функцию open():

```python
open(путь_к_файлу[, flag="c"[, protocol=None[, writeback=False]]])
```
Где параметр flag может принимать значения:

- c: файл открывается для чтения и записи (значение по умолчанию). Если файл не существует, то он создается.
    
- r: файл открывается только для чтения.
    
- w: файл открывается для записи.
    
- n: файл открывается для записи Если файл не существует, то он создается. Если он существует, то он перезаписывается
    

Для закрытия подключения к файлу вызывается метод close():

```python
import shelve
d = shelve.open(filename)
d.close()
```
Либо можно открывать файл с помощью оператора with. Сохраним и считаем в файл несколько объектов:

```python
import shelve

FILENAME = "states2"

with shelve.open(FILENAME) as states:
    states["London"] = "Great Britain"
    states["Paris"] = "France"
    states["Berlin"] = "Germany"
    states["Madrid"] = "Spain"

with shelve.open(FILENAME) as states:
    print(states["London"])
    print(states["Madrid"])
```
Запись данных предполагает установку значения для определенного ключа:
```python
states["London"] = "Great Britain"
```
А чтение из файла эквивалентно получению значения по ключу:
```python
print(states["London"])
```

### Чтение данных

При чтении данных, если запрашиваемый ключ отсутствует, то генерируется исключение. В этом случае перед получением мы можем проверять на наличие ключа с помощью оператора in:

|   |   |
|---|---|
|1<br><br>2<br><br>3<br><br>4|`with shelve.``open``(FILENAME) as states:`<br><br>    `key` `=` `"Brussels"`<br><br>    `if` `key` `in` `states:`<br><br>        `print``(states[key])`|

Также мы можем использовать метод get(). Первый параметр метода - ключ, по которому следует получить значение, а второй - значение по умолчанию, которое возвращается, если ключ не найден.

|   |   |
|---|---|
|1<br><br>2<br><br>3|`with shelve.``open``(FILENAME) as states:`<br><br>    `state` `=` `states.get(``"Brussels"``,` `"Undefined"``)`<br><br>    `print``(state)`|

Используя цикл for, можно перебрать все значения из файла:

|   |   |
|---|---|
|1<br><br>2<br><br>3|`with shelve.``open``(FILENAME) as states:`<br><br>    `for` `key` `in` `states:`<br><br>        `print``(key,``" - "``, states[key])`|

Метод keys() возвращает все ключи из файла, а метод values() - все значения:

|   |   |
|---|---|
|1<br><br>2<br><br>3<br><br>4<br><br>5<br><br>6<br><br>7|`with shelve.``open``(FILENAME) as states:`<br><br>    `for` `city` `in` `states.keys():`<br><br>        `print``(city, end``=``" "``)`        `# London Paris Berlin Madrid`<br><br>    `print``()`<br><br>    `for` `country` `in` `states.values():`<br><br>        `print``(country, end``=``" "``)`     `# Great Britain France Germany Spain`|

Еще один метод items() возвращает набор кортежей. Каждый кортеж содержит ключ и значение.

|                              |                                                                                                                             |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| 1<br><br>2<br><br>3<br><br>4 | `with shelve.``open``(FILENAME) as states:`<br><br>    `for` `state` `in` `states.items():`<br><br>        `print``(state)` |

### Обновление данных

Для изменения данных достаточно присвоить по ключу новое значение, а для добавления данных - определить новый ключ:

|   |   |
|---|---|
|1<br><br>2<br><br>3<br><br>4<br><br>5<br><br>6<br><br>7<br><br>8<br><br>9<br><br>10<br><br>11<br><br>12<br><br>13<br><br>14<br><br>15|`import` `shelve`<br><br>`FILENAME` `=` `"states2"`<br><br>`with shelve.``open``(FILENAME) as states:`<br><br>    `states[``"London"``]` `=` `"Great Britain"`<br><br>    `states[``"Paris"``]` `=` `"France"`<br><br>    `states[``"Berlin"``]` `=` `"Germany"`<br><br>    `states[``"Madrid"``]` `=` `"Spain"`<br><br>`with shelve.``open``(FILENAME) as states:`<br><br>    `states[``"London"``]` `=` `"United Kingdom"`<br><br>    `states[``"Brussels"``]` `=` `"Belgium"`<br><br>    `for` `key` `in` `states:`<br><br>        `print``(key,` `" - "``, states[key])`|

### Удаление данных

Для удаления с одновременным получением можно использовать функцию pop(), в которую передается ключ элемента и значение по умолчанию, если ключ не найден:

|   |   |
|---|---|
|1<br><br>2<br><br>3<br><br>4|`with shelve.``open``(FILENAME) as states:`<br><br>    `state` `=` `states.pop(``"London"``,` `"NotFound"``)`<br><br>    `print``(state)`|

Также для удаления может применяться оператор del:

|   |   |
|---|---|
|1<br><br>2<br><br>3|`with shelve.``open``(FILENAME) as states:`<br><br>    `del` `states[``"Madrid"``]`    `# удаляем объект с ключом Madrid`|

Для удаления всех элементов можно использовать метод clear():

|                     |                                                                         |
| ------------------- | ----------------------------------------------------------------------- |
| 1<br><br>2<br><br>3 | `with shelve.``open``(FILENAME) as states:`<br><br>    `states.clear()` |