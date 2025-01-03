
https://ru.wikipedia.org/wiki/CSV

1. Форматы данных `csv, tsv, dsv`
2. Модуль `csv`

**Аннотация.** Урок посвящен работе с текстовыми файлами в форматах `csv, tsv, dsv`.
## Формат CSV

CSV (от англ. Comma-Separated Values — значения, разделённые запятыми) — текстовый формат, предназначенный для представления табличных данных. Строка таблицы соответствует строке текста, которая содержит одно или несколько полей, разделенных запятыми.

Например, таблица:

|Rank|Language|Share|
|---|---|---|
|1|Python|31.17%|
|2|Java|17.75%|
|3|JavaScript|8%|
|4|C#|7.05%|
|5|PHP|6.09%|

в формате `csv` будет выглядеть так:
```no-highlight
Rank,Language,Share
1,Python,31.17%
2,Java,17.75%
3,JavaScript,8%
4,C#,7.05%
5,PHP,6.09%
```
Обратите внимание, пробелов после запятой быть не должно.

## Ручная работа с файлами

Рассмотрим текстовый файл `products.csv`, содержащий информацию о товарах некоторого интернет магазина. Файл содержит информацию о трех столбцах:

- `keywords` (ключевые слова)
- `price` (цена)
- `product_name` (имя продукта)

и имеет следующее содержимое:
```no-highlight
keywords,price,product_name
Садовый стул,1699,ВЭДДО
Садовый стул,2999,ЭПЛАРО
Садовый табурет,1699,ЭПЛАРО
Садовый стол,1999,ТЭРНО
Складной стол,7499,ЭПЛАРО
Настил,1299,РУННЕН
Стеллаж,1299,ХИЛЛИС
Кружка,39,СТЕЛЬНА
Молочник,299,ВАРДАГЕН
Термос для еды,699,ЭФТЕРФРОГАД
Ситечко,59,ИДЕАЛИСК
Чайник заварочный,499,РИКЛИГ
Кофе-пресс,699,УПХЕТТА
Чашка с блюдцем,249,ИКЕА
Кружка,249,ЭМНТ
Ситечко,199,САККУННИГ
Кружка,199,ФИНСТИЛТ
Тарелка,269,ЭВЕРЕНС
```
Разделителем записей был выбран символ **новой строки**, а разделителем полей — **символ запятой.**

В результате мы получили текстовый файл, который легко читается и человеком и компьютерной программой.

Поскольку любой `csv` файл является текстовым, то нам не составит труда обработать его "руками", подобно тому, как мы обрабатываем обычный текстовый файл.

Приведенный ниже код:

```python
with open('products.csv', encoding='utf-8') as file:
    data = file.read()
    for line in data.splitlines():
        print(line.split(','))
```

```no-highlight
['keywords', 'price', 'product_name']
['Садовый стул', '1699', 'ВЭДДО']
['Садовый стул', '2999', 'ЭПЛАРО']
['Садовый табурет', '1699', 'ЭПЛАРО']
['Садовый стол', '1999', 'ТЭРНО']
['Складной стол', '7499', 'ЭПЛАРО']
['Настил', '1299', 'РУННЕН']
['Стеллаж', '1299', 'ХИЛЛИС']
['Кружка', '39', 'СТЕЛЬНА']
['Молочник', '299', 'ВАРДАГЕН']
['Термос для еды', '699', 'ЭФТЕРФРОГАД']
['Ситечко', '59', 'ИДЕАЛИСК']
['Чайник заварочный', '499', 'РИКЛИГ']
['Кофе-пресс', '699', 'УПХЕТТА']
['Чашка с блюдцем', '249', 'ИКЕА']
['Кружка', '249', 'ЭМНТ']
['Ситечко', '199', 'САККУННИГ']
['Кружка', '199', 'ФИНСТИЛТ']
['Тарелка', '269', 'ЭВЕРЕНС']
```

Для построчного разделения текста удобно использовать строковый метод `splitlines()`, вместо метода `split('\n')`.

Мы также можем создать вложенный список (таблицу) для более удобного взаимодействия с данными:

```python
with open('products.csv', encoding='utf-8') as file:
    data = file.read()
    table = [r.split(',') for r in data.splitlines()]
```

С помощью такой таблицы мы можем обратиться к цене седьмого по счету товара:

```
print(table[7][1])
```

Или мы можем также отсортировать товары по цене и напечатать 55 самых дешевых товаров.

```python
with open('products.csv', encoding='utf-8') as file:
    data = file.read()
    table = [r.split(',') for r in data.splitlines()]
    del table[0]                                        # удаляем заголовок
    table.sort(key=lambda item: int(item[1]))
    for line in table[:5]:
        print(line)
```
выводит:
```no-highlight
['Кружка', '39', 'СТЕЛЬНА']
['Ситечко', '59', 'ИДЕАЛИСК']
['Ситечко', '199', 'САККУННИГ']
['Кружка', '199', 'ФИНСТИЛТ']
['Чашка с блюдцем', '249', 'ИКЕА']
```

Обратите внимание на то, что мы удалили первый элемент из списка, так как он содержит не данные, а заголовки. Также стоит обратить внимание на то, что в лямбда-функции мы преобразуем элемент `item[1]` к числовому типу, иначе сортировка будет работать не так, как полагается.

В приведенном выше файле `products.csv` символ запятой использовался в качестве разделителя полей. Однако бывают ситуации, в которых сам символ запятой является легитимным символом. Например, столбец `keywords` может содержать (и как правило на практике содержит) несколько ключевых слов. В таком случае структура файла нарушается. Для решения такой проблемы можно использовать два подхода.

**1 подход.** Если поле содержит запятые, то это поле должно быть заключено в двойные кавычки. Если этого не сделать, то данные невозможно будет корректно обработать.

Содержимое файла `products.csv` может иметь вид:
```no-highlight
keywords,price,product_name
"Садовый стул, стул для дачи",1699,ВЭДДО
Садовый стул,2999,ЭПЛАРО
Садовый табурет,1699,ЭПЛАРО
Садовый стол,1999,ТЭРНО
"Складной стол, обеденный стол",7499,ЭПЛАРО
Настил,1299,РУННЕН
Стеллаж,1299,ХИЛЛИС
"Кружка, сосуд, стакан с ручкой",39,СТЕЛЬНА
Молочник,299,ВАРДАГЕН
Термос для еды,699,ЭФТЕРФРОГАД
Ситечко,59,ИДЕАЛИСК
Чайник заварочный,499,РИКЛИГ
Кофе-пресс,699,УПХЕТТА
Чашка с блюдцем,249,ИКЕА
"Кружка, стакан с ручкой",249,ЭМНТ
Ситечко,199,САККУННИГ
Кружка,199,ФИНСТИЛТ
"Тарелка, блюдце",269,ЭВЕРЕНС
```

Обратите внимание на записи с номерами 1, 5, 8, 15 и 18. В этих записях в столбце `keywords` используется символ запятой, и для правильной обработки данных нам необходимо соответствующее поле обрамить символом двойных кавычек.

Обратите внимание на то, что при таком содержимом файла `products.csv` наш код, написанный выше, является нерабочим, так как он разделит каждую строку через символ запятой.

**2 подход.** Использовать в качестве разделителя другой символ, например, [символ табуляции](https://ru.wikipedia.org/wiki/%D0%A2%D0%B0%D0%B1%D1%83%D0%BB%D1%8F%D1%86%D0%B8%D1%8F) `(\t)`, который весьма редко встречается в качестве валидного содержимого файла.

```no-highlight
keywords	price	product_name
Садовый стул, стул для дачи	1699	ВЭДДО
Садовый стул	2999	ЭПЛАРО
Садовый табурет	1699	ЭПЛАРО
Садовый стол	1999	ТЭРНО
Складной стол, обеденный стол	7499	ЭПЛАРО
Настил	1299	РУННЕН
Стеллаж	1299	ХИЛЛИС
Кружка, сосуд, стакан с ручкой	39	СТЕЛЬНА
Молочник	299	ВАРДАГЕН
Термос для еды	699	ЭФТЕРФРОГАД
Ситечко	59	ИДЕАЛИСК
Чайник заварочный	499	РИКЛИГ
Кофе-пресс	699	УПХЕТТА
Чашка с блюдцем	249	ИКЕА
Кружка, стакан с ручкой	249	ЭМНТ
Ситечко	199	САККУННИГ
Кружка	199	ФИНСТИЛТ
Тарелка, блюдце	269	ЭВЕРЕНС
```

Формат данных `csv`, в котором разделителем является символ табуляции, называют `tsv` (англ. tab separated values — «значения, разделенные табуляцией»).

`tsv` — текстовый формат для представления табличных данных. Каждая запись в таблице — строка текстового файла. Каждое поле записи отделяется от других символом табуляции, а точнее — горизонтальной табуляции.

`tsv` и `csv` — формы более общего формата `dsv` (англ. delimiter separated values — «значения, разграниченные разделителем»).

Приведенный ниже код правильно обрабатывает файл `products.tsv`, в котором символом разделителя выбран символ табуляции (`\t`):

```python
with open('products.tsv', encoding='utf-8') as file:
    data = file.read()
    table = [r.split('\t') for r in data.splitlines()]
    del table[0]
    table.sort(key=lambda item: int(item[1]))
    for line in table[:5]:
        print(line)
```

и выводит 5 самых дешевых товаров:

```no-highlight
['Кружка, сосуд, стакан с ручкой', '39', 'СТЕЛЬНА']
['Ситечко', '59', 'ИДЕАЛИСК']
['Ситечко', '199', 'САККУННИГ']
['Кружка', '199', 'ФИНСТИЛТ']
['Чашка с блюдцем', '249', 'ИКЕА']
```

## Модуль csv

Несмотря на то что `csv` формат очень прост и мы можем работать с ним, как с обычным текстовым файлом, на практике используется встроенный модуль `csv`.

В данном модуле есть два основных объекта: `reader` и `writer`, созданные, чтобы читать и создавать `csv` файлы соответственно.

### Чтение данных с помощью reader

Для импорта модуля мы используем строку кода:

```
import csv
```

 Этот модуль входит в стандартную библиотеку, и его не нужно устанавливать каким‑то особенным способом.

Рассмотрим все тот же файл `products.csv`, содержащий информацию о товарах интернет магазина:
```no-highlight
keywords,price,product_name
Садовый стул,1699,ВЭДДО
Садовый стул,2999,ЭПЛАРО
Садовый табурет,1699,ЭПЛАРО
Садовый стол,1999,ТЭРНО
Складной стол,7499,ЭПЛАРО
Настил,1299,РУННЕН
Стеллаж,1299,ХИЛЛИС
Кружка,39,СТЕЛЬНА
Молочник,299,ВАРДАГЕН
Термос для еды,699,ЭФТЕРФРОГАД
Ситечко,59,ИДЕАЛИСК
Чайник заварочный,499,РИКЛИГ
Кофе-пресс,699,УПХЕТТА
Чашка с блюдцем,249,ИКЕА
Кружка,249,ЭМНТ
Ситечко,199,САККУННИГ
Кружка,199,ФИНСТИЛТ
Тарелка,269,ЭВЕРЕНС
```

Приведенный ниже код:

```python
import csv

with open('products.csv', encoding='utf-8') as file:
    rows = csv.reader(file)                               # создаем reader объект
    for row in rows:
        print(row)
```

читает содержимое файла `products.csv` и выводит:

```no-highlight
['keywords', 'price', 'product_name']
['Садовый стул', '1699', 'ВЭДДО']
['Садовый стул', '2999', 'ЭПЛАРО']
['Садовый табурет', '1699', 'ЭПЛАРО']
['Садовый стол', '1999', 'ТЭРНО']
['Складной стол', '7499', 'ЭПЛАРО']
['Настил', '1299', 'РУННЕН']
['Стеллаж', '1299', 'ХИЛЛИС']
['Кружка', '39', 'СТЕЛЬНА']
['Молочник', '299', 'ВАРДАГЕН']
['Термос для еды', '699', 'ЭФТЕРФРОГАД']
['Ситечко', '59', 'ИДЕАЛИСК']
['Чайник заварочный', '499', 'РИКЛИГ']
['Кофе-пресс', '699', 'УПХЕТТА']
['Чашка с блюдцем', '249', 'ИКЕА']
['Кружка', '249', 'ЭМНТ']
['Ситечко', '199', 'САККУННИГ']
['Кружка', '199', 'ФИНСТИЛТ']
['Тарелка', '269', 'ЭВЕРЕНС']
```

Самая важная строка кода в программе — это строка с созданием `reader` объекта:

```python
rows = csv.reader(file)
```

Объект `reader` дает доступ к построчному итератору, полностью аналогичному работе с файлом или списком.

После выполнения этой строки в переменную `rows` будет записан итератор, с помощью которого можно «пробежаться» циклом по файлу. В каждой итерации цикла при этом будет доступна соответствующая строка файла, уже разбитая по запятым и представляющая собой список. При этом автоматически будут учтены все нюансы с запятыми внутри кавычек и самими кавычками.

Так как каждая строка файла, полученная из итератора, является списком, к ней можно применять все способы работы со списками.

Приведенный ниже код:

```python
import csv

with open('products.csv', encoding='utf-8') as file:
    rows = csv.reader(file)
    for keywords, price, product_name in rows:
        print(f'Ключевые слова: {keywords}, цена: {price}, название: {product_name}')
```

использует распаковку списка и выводит:

```no-highlight
Ключевые слова: keywords, цена: price, название: product_name
Ключевые слова: Садовый стул, цена: 1699, название: ВЭДДО
Ключевые слова: Садовый стул, цена: 2999, название: ЭПЛАРО
Ключевые слова: Садовый табурет, цена: 1699, название: ЭПЛАРО
Ключевые слова: Садовый стол, цена: 1999, название: ТЭРНО
Ключевые слова: Складной стол, цена: 7499, название: ЭПЛАРО
Ключевые слова: Настил, цена: 1299, название: РУННЕН
Ключевые слова: Стеллаж, цена: 1299, название: ХИЛЛИС
Ключевые слова: Кружка, цена: 39, название: СТЕЛЬНА
Ключевые слова: Молочник, цена: 299, название: ВАРДАГЕН
Ключевые слова: Термос для еды, цена: 699, название: ЭФТЕРФРОГАД
Ключевые слова: Ситечко, цена: 59, название: ИДЕАЛИСК
Ключевые слова: Чайник заварочный, цена: 499, название: РИКЛИГ
Ключевые слова: Кофе-пресс, цена: 699, название: УПХЕТТА
Ключевые слова: Чашка с блюдцем, цена: 249, название: ИКЕА
Ключевые слова: Кружка, цена: 249, название: ЭМНТ
Ключевые слова: Ситечко, цена: 199, название: САККУННИГ
Ключевые слова: Кружка, цена: 199, название: ФИНСТИЛТ
Ключевые слова: Тарелка, цена: 269, название: ЭВЕРЕНС
```

При создании `reader` объекта мы можем его настраивать, указывая:

- аргумент `delimiter` — односимвольная строка, используемая для разделения полей, по умолчанию имеет значение `','`
- аргумент `quotechar` — односимвольная строка, используемая для кавычек в полях, содержащих специальные символы, по умолчанию имеет значение `'"'`.

Пусть содержимое файла `products.csv` имеет вид (в качестве разделителя выбран символ `';'`):

```no-highlight
keywords;price;product_name
"Садовый стул, стул для дачи";1699;ВЭДДО
Садовый стул;2999;ЭПЛАРО
Садовый табурет;1699;ЭПЛАРО
Садовый стол;1999;ТЭРНО
"Складной стол, обеденный стол";7499;ЭПЛАРО
Настил;1299;РУННЕН
Стеллаж;1299;ХИЛЛИС
"Кружка, сосуд, стакан с ручкой";39;СТЕЛЬНА
Молочник;299;ВАРДАГЕН
Термос для еды;699;ЭФТЕРФРОГАД
Ситечко;59;ИДЕАЛИСК
Чайник заварочный;499;РИКЛИГ
Кофе-пресс;699;УПХЕТТА
Чашка с блюдцем;249;ИКЕА
"Кружка, стакан с ручкой";249;ЭМНТ
Ситечко;199;САККУННИГ
Кружка;199;ФИНСТИЛТ
"Тарелка, блюдце";269;ЭВЕРЕНС
```

Приведенный ниже код:

```python
import csv

with open('products.csv', encoding='utf-8') as file:
    rows = csv.reader(file, delimiter=';', quotechar='"')
    for index, row in enumerate(rows):
        if index > 5:
            break
        print(row)
```

выводит первые 6 строк файла, включая заголовок с названиями столбцов:

```no-highlight
['keywords', 'price', 'product_name']
['Садовый стул, стул для дачи', '1699', 'ВЭДДО']
['Садовый стул', '2999', 'ЭПЛАРО']
['Садовый табурет', '1699', 'ЭПЛАРО']
['Садовый стол', '1999', 'ТЭРНО']
['Складной стол, обеденный стол', '7499', 'ЭПЛАРО']
```

При создании `reader` объекта мы указываем, что символ-разделитель записей `delimiter` в нашем файле — точка с запятой, а символ кавычек `quotechar` — двойные кавычки. Кроме того, мы используем встроенную функцию `enumerate()` для нумерации строк.

Обратите внимание на то, что для корректной обработки данных мы должны все еще исключить первую строку из обработки, которая содержит названия столбцов.

### Чтение данных с помощью DictReader

Иcпользовать `reader` объект не всегда удобно, так как он возвращает сырые списки из строк файла, к тому же первой строкой является строка с названиями столбцов, которая практически всегда удаляется, так как мешает правильной обработке данных.

В модуле `csv` есть специальный объект `DictReader`, который поддерживает создание объекта-словаря на основе названий столбцов. С помощью `DictReader` объекта мы можем обращаться к полям не по индексу, а по названию, что делает код более понятным.

Пусть содержимое файла `products.csv` имеет вид (в качестве разделителя выбран символ `';'`):

```no-highlight
keywords;price;product_name
"Садовый стул, стул для дачи";1699;ВЭДДО
Садовый стул;2999;ЭПЛАРО
Садовый табурет;1699;ЭПЛАРО
Садовый стол;1999;ТЭРНО
"Складной стол, обеденный стол";7499;ЭПЛАРО
Настил;1299;РУННЕН
Стеллаж;1299;ХИЛЛИС
"Кружка, сосуд, стакан с ручкой";39;СТЕЛЬНА
Молочник;299;ВАРДАГЕН
Термос для еды;699;ЭФТЕРФРОГАД
Ситечко;59;ИДЕАЛИСК
Чайник заварочный;499;РИКЛИГ
Кофе-пресс;699;УПХЕТТА
Чашка с блюдцем;249;ИКЕА
"Кружка, стакан с ручкой";249;ЭМНТ
Ситечко;199;САККУННИГ
Кружка;199;ФИНСТИЛТ
"Тарелка, блюдце";269;ЭВЕРЕНС
```

Приведенный ниже код:

```python
import csv

with open('products.csv', encoding='utf-8') as file:
    rows = csv.DictReader(file, delimiter=';', quotechar='"')
    for row in rows:
        print(row)
```

выводит:

```no-highlight
{'keywords': 'Садовый стул, стул для дачи', 'price': '1699', 'product_name': 'ВЭДДО'}
{'keywords': 'Садовый стул', 'price': '2999', 'product_name': 'ЭПЛАРО'}
{'keywords': 'Садовый табурет', 'price': '1699', 'product_name': 'ЭПЛАРО'}
{'keywords': 'Садовый стол', 'price': '1999', 'product_name': 'ТЭРНО'}
{'keywords': 'Складной стол, обеденный стол', 'price': '7499', 'product_name': 'ЭПЛАРО'}
{'keywords': 'Настил', 'price': '1299', 'product_name': 'РУННЕН'}
{'keywords': 'Стеллаж', 'price': '1299', 'product_name': 'ХИЛЛИС'}
{'keywords': 'Кружка, сосуд, стакан с ручкой', 'price': '39', 'product_name': 'СТЕЛЬНА'}
{'keywords': 'Молочник', 'price': '299', 'product_name': 'ВАРДАГЕН'}
{'keywords': 'Термос для еды', 'price': '699', 'product_name': 'ЭФТЕРФРОГАД'}
{'keywords': 'Ситечко', 'price': '59', 'product_name': 'ИДЕАЛИСК'}
{'keywords': 'Чайник заварочный', 'price': '499', 'product_name': 'РИКЛИГ'}
{'keywords': 'Кофе-пресс', 'price': '699', 'product_name': 'УПХЕТТА'}
{'keywords': 'Чашка с блюдцем', 'price': '249', 'product_name': 'ИКЕА'}
{'keywords': 'Кружка, стакан с ручкой', 'price': '249', 'product_name': 'ЭМНТ'}
{'keywords': 'Ситечко', 'price': '199', 'product_name': 'САККУННИГ'}
{'keywords': 'Кружка', 'price': '199', 'product_name': 'ФИНСТИЛТ'}
{'keywords': 'Тарелка, блюдце', 'price': '269', 'product_name': 'ЭВЕРЕНС'}
```

Обратите внимание на то, что переменная `row` имеет тип `dict` в Python 3.8+. В более ранних версиях переменная `row` имела тип `OrderedDict`, который мы изучим чуть позже.

Приведенный ниже код:
```python
import csv

with open('products.csv', encoding='utf-8') as file:
    rows = csv.DictReader(file, delimiter=';', quotechar='"')
    expensive = sorted(rows, key=lambda item: int(item['price']), reverse=True)
    for record in expensive[:5]:
        print(record)
```

выводит 5 самых дорогих товаров:

```no-highlight
{'keywords': 'Складной стол, обеденный стол', 'price': '7499', 'product_name': 'ЭПЛАРО'}
{'keywords': 'Садовый стул', 'price': '2999', 'product_name': 'ЭПЛАРО'}
{'keywords': 'Садовый стол', 'price': '1999', 'product_name': 'ТЭРНО'}
{'keywords': 'Садовый стул, стул для дачи', 'price': '1699', 'product_name': 'ВЭДДО'}
{'keywords': 'Садовый табурет', 'price': '1699', 'product_name': 'ЭПЛАРО'}
```

При создании `DictReader` объекта значениями по умолчанию для аргументов `delimiter` и `quotechar` являются `','` (символ запятой) и `'"'` (символ двойной кавычки) соответственно.

Обратите внимание на то, что при использовании `DictReader` мы не избавляемся от первой строки, содержащей названия столбцов. Они хранятся в атрибуте `fieldnames` объекта `DictReader`. При этом к элементам строк мы обращаемся теперь не по индексам (`int(item[1])`), а по их названиям (`int(item['price'])`), что намного удобнее.

### Запись данных с помощью writer

Для записи данных в `csv` файл можно использовать специальный `writer` объект.

Приведенный ниже код:

```python
import csv

columns = ['first_name', 'second_name', 'class_number', 'class_letter']
data = [['Тимур', 'Гуев', 11, 'А'], ['Руслан', 'Чаниев', 9, 'Б'], ['Артур', 'Харисов', 10, 'В']]

with open('students.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(columns)                 # запись заголовков
    for row in data:                         # запись строк
        writer.writerow(row)
```

создает файл `students.csv` с содержимым:

```no-highlight
first_name,second_name,class_number,class_letter
Тимур,Гуев,11,А
Руслан,Чаниев,9,Б
Артур,Харисов,10,В
```

Обратите внимание на необязательный параметр `newline` функции `open()`, который имеет значение `''` (пустой строки). Он отвечает за переводы строк при чтении или записи в текстовый файл. По умолчанию имеет значение `None`, в этом случае все разделители строк преобразуются в `'\n'`. Если в файле оказывается лишний перевод строки, то следует использовать этот параметр в режиме `newline=''`, тогда `'\n'` будет преобразован в пустую строку.

При создании `writer` объекта мы так же можем его настраивать, задавая `delimiter` и многие другие параметры.

Приведенный ниже код:

```python
import csv

columns = ['first_name', 'second_name', 'class_number', 'class_letter']
data = [['Тимур', 'Гуев', 11, 'А'], ['Руслан', 'Чаниев', 9, 'Б'], ['Роман', 'Белых', 10, 'В']]

with open('students.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow(columns)
    for row in data:
        writer.writerow(row)
```

создает файл с содержимым:

```no-highlight
"first_name";"second_name";"class_number";"class_letter"
"Тимур";"Гуев";11;"А"
"Руслан";"Чаниев";9;"Б"
"Роман";"Белых";10;"В"
```

Значение аргумента `quoting=csv.QUOTE_NONNUMERIC` означает, что в кавычки будут браться все нечисловые значения. По умолчанию символом кавычки является `"`, если нужно поменять символ, то используйте уже знакомый нам именованный аргумент `quotechar`.

Для задания параметра `quoting` используются специальные константы из модуля `csv`:

- `QUOTE_ALL`: указывает объектам записи указывать все поля
- `QUOTE_MINIMAL`: указывает объектам записи заключать в кавычки только те поля, которые содержат специальные символы, такие как разделитель `delimiter`, кавычка `quotechar` или любой из символов в `lineterminator`
- `QUOTE_NONNUMERIC`: указывает объектам записи указывать все нечисловые поля
- `QUOTE_NONE`: указывает объектам записи никогда не заключать в кавычки поля

Помимо метода `writerow()` можно использовать и метод `writerows()`, чтобы записать сразу несколько строк. Единственным аргументом этого метода может быть коллекция коллекций. То есть, каждый элемент списка `rows` в нашем случае должен быть коллекцией. Если `rows` будет, например, списком чисел, программа завершится с ошибкой.

Приведенный ниже код:

```python
import csv

columns = ['first_name', 'second_name', 'class_number', 'class_letter']
data = [['Тимур', 'Гуев', 11, 'А'], ['Руслан', 'Чаниев', 9, 'Б'], ['Роман', 'Белых', 10, 'В']]

with open('students.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow(columns)
    writer.writerows(data)
```

создает файл `students.csv` с содержимым:

```no-highlight
"first_name";"second_name";"class_number";"class_letter"
"Тимур";"Гуев";11;"А"
"Руслан";"Чаниев";9;"Б"
"Роман";"Белых";10;"В"
```

### Запись данных с помощью DictWriter

Для записи данных в `csv` файл также можно использовать `DictWriter` объект, который позволяет записывать содержимое словаря в файл.

Приведенный ниже код:

```python
import csv

data = [{'first_name': 'Тимур', 'second_name': 'Гуев', 'class_number': 11, 'class_letter': 'А'},
        {'first_name': 'Руслан', 'second_name': 'Чаниев', 'class_number': 9, 'class_letter': 'Б'},
        {'first_name': 'Роман', 'second_name': 'Белых', 'class_number': 10, 'class_letter': 'В'}]

columns = ['first_name', 'second_name', 'class_number', 'class_letter']

with open('students.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=columns, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
    writer.writeheader()                 # запись заголовков
    for row in data:                     # запись строк
        writer.writerow(row)
```

создает файл `students.csv` с содержимым:

```no-highlight
"first_name";"second_name";"class_number";"class_letter"
"Тимур";"Гуев";11;"А"
"Руслан";"Чаниев";9;"Б"
"Роман";"Белых";10;"В"
```

Мы также можем использовать метод `writerows()` объекта `DictWriter` для записи сразу нескольких строк. Таким образом вместо строк кода:

```python
for row in data:
    writer.writerow(row)
```

можно написать:

```python
writer.writerows(data)
```

Обратите внимание на то, что ключи словарей, которые записываются в файл, должны совпадать с названиями полей, которые переданы в качестве аргумента `fieldnames`, иначе будет возникать ошибка `ValueError`.

## Примечания

**Примечание 1.** Спецификация формата `csv`:

- каждая строка файла — это одна строка таблицы
- разделителем (delimiter) значений колонок является символ запятой `,`. Однако на практике часто используются другие разделители, например: `;` или символ табуляции `\t` (формат TSV)
- значения, содержащие зарезервированные символы (двойная кавычка, запятая, точка с запятой, новая строка), обрамляются двойными кавычками `"`. Если в значении встречаются кавычки — они представляются в файле в виде двух кавычек подряд

**Примечание 2.** Подробнее о `csv` формате можно прочитать на [википедии](https://ru.wikipedia.org/wiki/CSV).

**Примечание 3.** Документация по модулю `csv` доступна по [ссылке](https://docs.python.org/3/library/csv.html) и [ссылке](https://docs-python.ru/standart-library/modul-csv-python/).

**Примечание 4.** Достаточно распространенная ошибка при чтении данных из `csv` файла — это передача в `csv.reader` (`csv.DictReader`) не файлового объекта, а текстовых данных, считанных из файла. Это не вызывает ошибки, но результат будет отличаться от ожидаемого.

**Примечание 5.** При создании `reader` объекта важно, чтобы файл был открыт в режиме чтения (`'r'`), аналогично при создании `writer` объекта — в режиме записи (`'w'`).

**Примечание 6.** Так как `reader` объект является итератором, мы можем преобразовать его в список или кортеж с помощью встроенных функций `list()` и `tuple()` соответственно, но не можем преобразовать в множество, т.к. его элементами могут быть только неизменяемые объекты, которыми списки не являются.