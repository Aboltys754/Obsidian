[[#Историческая справка]]
[[#Тип данных OrderedDict]]
[[#Изменение OrderedDict словаря]]
[[#Итерирование по OrderedDict словарю]]
[[#Методы popitem() и move_to_end()]]
[[#Сравнение словарей]]
[[#Примечания]]
## Историческая справка

В Python 3.6 словари (тип `dict`) были переработаны так, чтобы повысилась их производительность. Следствием такой переработки явился один очень интересный побочный эффект — словари стали упорядоченными, то есть стали сохранять порядок вставки элементов, хотя на тот момент официально этот порядок не гарантировался. «Официально не гарантируется» означает, что это была просто деталь реализации, которая могла быть изменена в будущих версиях Python. Но начиная с Python 3.7, в спецификации языка гарантируется сохранение порядка вставки элементов в словарь.

После переработки тип `dict` стал использовать на 2020-25%25% меньше памяти.

В далеком 20082008 году, задолго до переработки устройства словарей в рамках релиза Python 3.1 в стандартную библиотеку был добавлен тип `OrderedDict`, который на тот момент решал проблему неупорядоченности обычных словарей (тип `dict`).

## Тип данных OrderedDict

Тип `OrderedDict` является подтипом типа `dict`, сохраняющий порядок, в котором пары "ключ-значение" вставляются в словарь. Когда мы перебираем объект типа `OrderedDict`, его элементы перебираются в исходном порядке. Если мы обновим значение существующего ключа, то порядок останется неизменным. Если мы удалим элемент и вставим его снова, то этот элемент будет добавлен в конец словаря.

Тип `OrderedDict` будучи подтипом `dict` наследует все методы, предоставляемые обычным словарем. При этом в `OrderedDict` также есть дополнительные методы, о которых мы поговорим ниже.

В отличие от `dict`, тип `OrderedDict` не является встроенным типом и для использования его необходимо импортировать из модуля `collections`.

Приведенный ниже код:

```python
from collections import OrderedDict

numbers = OrderedDict()

numbers['one'] = 1
numbers['two'] = 2
numbers['three'] = 3

print(numbers)
```

выводит:

```no-highlight
OrderedDict([('one', 1), ('two', 2), ('three', 3)])
```

Как и `defaultdict`, эти словари можно создавать любым из доступных способов, как и обычные словари:

```python
from collections import OrderedDict

numbers1 = OrderedDict({'one': 1, 'two': 2, 'three': 3})
numbers2 = OrderedDict([('one', 1), ('two', 2), ('three', 3)])
numbers3 = OrderedDict(one=1, two=2, three=3)
```

## Изменение OrderedDict словаря

Тип `OrderedDict` является изменяемым. Мы можем вставлять новые элементы, обновлять и удалять существующие элементы. Если мы вставим новый элемент в существующий `OrderedDict` словарь, то этот элемент добавится в конец словаря.

Приведенный ниже код:

```python
from collections import OrderedDict

numbers = OrderedDict(one=1, two=2, three=3)

print(numbers)

numbers['four'] = 4

print(numbers)
```

выводит:

```no-highlight
OrderedDict([('one', 1), ('two', 2), ('three', 3)])
OrderedDict([('one', 1), ('two', 2), ('three', 3), ('four', 4)])
```

Если мы удалим элемент из существующего `OrderedDict` словаря и снова вставим его, то он будет помещен в конец словаря.

Приведенный ниже код:

```python
from collections import OrderedDict

numbers = OrderedDict(one=1, two=2, three=3)
print(numbers)

del numbers['one']

print(numbers)
numbers['one'] = 1
print(numbers)
```

выводит:

```no-highlight
OrderedDict([('one', 1), ('two', 2), ('three', 3)])
OrderedDict([('two', 2), ('three', 3)])
OrderedDict([('two', 2), ('three', 3), ('one', 1)])
```

Если мы обновляем значение по существующему ключу, то ключ сохраняет свою позицию.

Приведенный ниже код:

```python
from collections import OrderedDict

numbers = OrderedDict(one=1, two=2, three=3)
print(numbers)

numbers['one'] = 1.0
print(numbers)

numbers.update(two=2.0)
print(numbers)
```

выводит:

```no-highlight
OrderedDict([('one', 1), ('two', 2), ('three', 3)])
OrderedDict([('one', 1.0), ('two', 2), ('three', 3)])
OrderedDict([('one', 1.0), ('two', 2.0), ('three', 3)])
```

Обновить значение по нужному ключу можно либо с помощью квадратных скобок, либо с помощью словарного метода `update()`.

## Итерирование по OrderedDict словарю

Доступ к элементам и итерирование по `OrderedDict` словарям работает так же, как и у обычных словарей. Мы можем перебирать ключи напрямую или можем использовать словарные методы `items()`, `keys()` и `values()`.

Приведенный ниже код:

```python
from collections import OrderedDict

numbers = OrderedDict(one=1, two=2, three=3)

# обращение по ключу
print(numbers['one'])
print(numbers['three'])

print()

# перебор ключей напрямую
for key in numbers:
    print(key, '->', numbers[key])

print()

# перебор пар (ключ, значение) через метод
for key, value in numbers.items():
    print(key, '->', value)

print()

# перебор ключей через метод
for key in numbers.keys():
    print(key, '->', numbers[key])

print()

# перебор значений через метод
for value in numbers.values():
    print(value)
```

выводит:

```no-highlight
1
3

one -> 1
two -> 2
three -> 3

one -> 1
two -> 2
three -> 3

one -> 1
two -> 2
three -> 3

1
2
3
```

При итерировании по `OrderedDict` словарям мы можем использовать встроенную функцию `reversed()`.

Приведенный ниже код:

```python
from collections import OrderedDict

numbers = OrderedDict(one=1, two=2, three=3)

# перебор ключей напрямую
for key in reversed(numbers):
    print(key, '->', numbers[key])

print()

# перебор пар (ключ, значение) через метод
for key, value in reversed(numbers.items()):
    print(key, '->', value)

print()

# перебор ключей через метод
for key in reversed(numbers.keys()):
    print(key, '->', numbers[key])

print()

# перебор значений через метод
for value in reversed(numbers.values()):
    print(value)
```

выводит:

```no-highlight
three -> 3
two -> 2
one -> 1

three -> 3
two -> 2
one -> 1

three -> 3
two -> 2
one -> 1

3
2
1
```

Обычные словари (тип `dict`) начиная с Python 3.8 также поддерживают использование встроенной функции `reversed()`.

## Методы popitem() и move_to_end()

`OrderedDict` словари имеют два полезных метода:

- метод `move_to_end()` позволяет переместить существующий элемент либо в конец, либо в начало словаря
- метод `popitem()` позволяет удалить и вернуть элемент либо из конца, либо из начала словаря

### Метод move_to_end()

Методу `move_to_end()` можно передать два аргумента:

- `key` (обязательный аргумент) – ключ, который идентифицирует перемещаемый элемент
    
- `last` (необязательный аргумент) – логическое значение (тип `bool`), которое определяет, в какой конец словаря мы перемещаем элемент, значение `True` (по умолчанию) перемещает элемент в конец, значение `False` – в начало
    

Если при вызове метода `move_to_end()` переданный ключ отсутствует в словаре, то возникает ошибка `KeyError`.

Приведенный ниже код:

```python
from collections import OrderedDict

numbers = OrderedDict(one=1, two=2, three=3)
print(numbers)

numbers.move_to_end('one')       # last=True
print(numbers)

numbers.move_to_end('three', last=False)       # last=False
print(numbers)
```

выводит:

```no-highlight
OrderedDict([('one', 1), ('two', 2), ('three', 3)])
OrderedDict([('two', 2), ('three', 3), ('one', 1)])
OrderedDict([('three', 3), ('two', 2), ('one', 1)])
```

С помощью метода `move_to_end()` мы можем сортировать `OrderedDict` словарь по ключам.

Приведенный ниже код:

```python
from collections import OrderedDict

letters = OrderedDict(b=2, d=4, a=1, c=3)

for key in sorted(letters):
    letters.move_to_end(key)

print(letters)
```

выводит:

```no-highlight
OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
```

### Метод popitem()

Метод `popitem()` по умолчанию удаляет и возвращает элемент в порядке [LIFO](https://ru.wikipedia.org/wiki/LIFO) (Last-In/First-Out, последний пришел/первый ушел). Другими словами, метод `popitem()` удаляет элементы с конца словаря.

Приведенный ниже код:

```python
from collections import OrderedDict

numbers = OrderedDict(one=1, two=2, three=3)

print(numbers.popitem())
print(numbers)

print(numbers.popitem())
print(numbers)
```

выводит:

```no-highlight
('three', 3)
OrderedDict([('one', 1), ('two', 2)])
('two', 2)
OrderedDict([('one', 1)])
```

Если методу `popitem()` передать необязательный аргумент `last=False`, то он начнет удалять и возвращать элементы в порядке [FIFO](https://ru.wikipedia.org/wiki/FIFO) (First-In/First-Out, первый пришел/первый ушел).

Приведенный ниже код:

```python
from collections import OrderedDict

numbers = OrderedDict(one=1, two=2, three=3)

print(numbers.popitem(last=False))
print(numbers)

print(numbers.popitem(last=False))
print(numbers)
```

выводит:

```no-highlight
('one', 1)
OrderedDict([('two', 2), ('three', 3)])
('two', 2)
OrderedDict([('three', 3)])
```

## Сравнение словарей

При сравнении на равенство обычных словарей (тип `dict`) порядок расположения их элементов **неважен**.

Приведенный ниже код:

```python
letters1 = dict(a=1, b=2, c=3, d=4)
letters2 = {'b': 2, 'a': 1, 'c': 3, 'd': 4}
letters3 = dict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])

print(letters1 == letters2)
print(letters1 == letters3)
```

выводит:

```no-highlight
True
True
```

При сравнение на равенство `OrderedDict` словарей порядок расположения их элементов **важен**.

Приведенный ниже код:

```python
from collections import OrderedDict

letters1 = OrderedDict(a=1, b=2, c=3, d=4)
letters2 = OrderedDict({'b': 2, 'a': 1, 'c': 3, 'd': 4})
letters3 = OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])

print(letters1 == letters2)
print(letters1 == letters3)
```

выводит:

```no-highlight
False
True
```

При сравнении на равенство обычного словаря (тип `dict`) и `OrderedDict` словаря порядок расположения их элементов **неважен**.

Приведенный ниже код:

```python
from collections import OrderedDict

letters1 = OrderedDict(a=1, b=2, c=3, d=4)
letters2 = {'b': 2, 'a': 1, 'c': 3, 'd': 4}

print(letters1 == letters2)
```

выводит:

```no-highlight
True
```

## Примечания

**Примечание 1.** Прекрасная статья по типу `OrderedDict` доступна по [ссылке](https://realpython.com/python-ordereddict/).

**Примечание 2.** Послушать о текущей реализации словарей можно по [ссылке](https://www.youtube.com/watch?v=37S53yFg9wc).

**Примечание 3.** У обычных словарей (тип `dict`) есть методы `pop()` и `popitem()`, о которых можно почитать по [ссылке](https://stepik.org/lesson/446696/step/1?unit=437002).

**Примечание 4.** Мы можем использовать метод `fromkeys()` для создания `OrderedDict` словарей.

Приведенный ниже код:

```python
from collections import OrderedDict

keys = ['one', 'two', 'three']
numbers = OrderedDict.fromkeys(keys, 0)
print(numbers)
```

выводит:

```no-highlight
OrderedDict([('one', 0), ('two', 0), ('three', 0)])
```

**Примечание 5.** В Python 3.9 появились операторы `|` и `|=` которые реализуют операцию конкатенации словарей, как обычных, так и `OrderedDict`.

Приведенный ниже код:

```python
from collections import OrderedDict

physicists = OrderedDict(newton='1642-1726', einstein='1879-1955')
biologists = OrderedDict(darwin='1809-1882', mendel='1822-1884')

scientists = physicists | biologists
print(scientists)
```

выводит:

```no-highlight
OrderedDict([('newton', '1642-1726'), ('einstein', '1879-1955'), ('darwin', '1809-1882'), ('mendel', '1822-1884')])
```

Приведенный ниже код:

```python
from collections import OrderedDict

physicists = OrderedDict(newton='1642-1726', einstein='1879-1955')
physicists1 = OrderedDict(newton='1642-1726/1727', hawking='1942-2018')

physicists |= physicists1

print(physicists)
```

выводит:

```no-highlight
OrderedDict([('newton', '1642-1726/1727'), ('einstein', '1879-1955'), ('hawking', '1942-2018')])
```

**Примечание 6.** Тип данных `OrderedDict` написан на языке C и реализован в виде двусвязного списка для сохранения порядка элементов.

**Примечание 7.** Тип данных `OrderedDict` проигрывает типу `dict` по производительности:

- примерно на 40%40% медленнее
- примерно на 50%50% занимает больше памяти

**Примечание 8.** `OrderedDict` словари содержат дополнительный атрибут `__dict__`, которого нет у обычного словаря. Данный атрибут используется для динамического наделения объектов дополнительным функционалом.

Приведенный ниже код:

```python
from collections import OrderedDict

letters = OrderedDict(b=2, d=4, a=1, c=3)
print(letters)
print(letters.__dict__)

letters.__dict__['advanced'] = '144'
print(letters)
print(letters.__dict__)
```

выводит:

```no-highlight
OrderedDict([('b', 2), ('d', 4), ('a', 1), ('c', 3)])
{}
OrderedDict([('b', 2), ('d', 4), ('a', 1), ('c', 3)])
{'advanced': '144'}
```

Приведенный ниже код:

```python
letters = dict(b=2, d=4, a=1, c=3)

print(letters.__dict__)    # у обычных словарей нет атрибута __dict__
```

приводит к возникновению ошибки:

```no-highlight
AttributeError: 'dict' object has no attribute '__dict__'
```

Для динамического задания новых атрибутов мы можем использовать два синтаксиса:

- в стиле словаря: `ordered_dict.__dict__['attr'] = value`
- через точечную нотацию: `ordered_dict.attr = value`

Приведенный ниже код:

```python
from collections import OrderedDict

letters = OrderedDict(b=2, d=4, a=1, c=3)

letters.sorted_keys = lambda: sorted(letters.keys())

print(letters)
print(letters.sorted_keys())

letters['e'] = 5
print(letters)
print(letters.sorted_keys())

for key in letters.sorted_keys():
    print(key, '->', letters[key])
```

выводит:

```no-highlight
OrderedDict([('b', 2), ('d', 4), ('a', 1), ('c', 3)])
['a', 'b', 'c', 'd']
OrderedDict([('b', 2), ('d', 4), ('a', 1), ('c', 3), ('e', 5)])
['a', 'b', 'c', 'd', 'e']
a -> 1
b -> 2
c -> 3
d -> 4
e -> 5
```

Таким образом, мы наделили  `OrderedDict` словарь (переменная `letters`) дополнительным методом (атрибутом) `sorted_keys()`, который возвращает список упорядоченных ключей.

**Примечание 9.** Различия и особенности типов `dict` и `OrderedDict` отражены в таблице:

|Функционал|Тип OrderedDict|Тип dict|
|---|---|---|
|сохранность порядка вставки ключей|да (начиная с Python 3.1)|да (начиная с Python 3.6)|
|удобочитаемость и сигнализация о намерениях|высокая|низкая|
|возможность менять порядок элементов|да (метод `move_to_end()`)|нет|
|производительность операций|низкая|высокая|
|потребление памяти|высокое|низкое|
|учет порядка элементов при сравнении на равенство|да|нет|
|перебор ключей в обратном порядке|да (начиная с Python 3.5)|да (начиная с Python 3.8)|
|возможность добавления пользовательских атрибутов|да (атрибут `.__dict__`)|нет|
|возможность использовать операторы `\|` и `\|=`|да (начиная с Python 3.9)|да (начиная с Python 3.9)|

**Примечание 10.** Исходный код `OrderedDict` доступен по [ссылке](https://github.com/python/cpython/blob/main/Lib/collections/__init__.py). Рекомендуем вам ознакомиться с ним, тогда вопросов точно не останется 😎.

**Примечание 11.** С релизом Python 3.12 тип `OrderedDict` был обновлен. Так в новой версии языка объект типа `OrderedDict` получил новое строковое представление.

Приведенный ниже код:

```python
from collections import OrderedDict

numbers = OrderedDict()

numbers['one'] = 1
numbers['two'] = 2
numbers['three'] = 3

print(numbers)
```

в Python 3.11 выводит:

```no-highlight
OrderedDict([('one', 1), ('two', 2), ('three', 3)])
```

в то время как в Python 3.12 выводит:

```no-highlight
OrderedDict({('one', 1), ('two', 2), ('three', 3)})
```