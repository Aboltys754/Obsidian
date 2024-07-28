
1. [[#Тип данных timedelta]]
2. [[Тип данных timedelta#Атрибуты days, seconds, microseconds и метод total_seconds()]]
3. [[#Сравнение временных интервалов]]
4. [[#Операции над временными интервалами timedelta]]
5. Операции над `datetime` и `date`


## Тип данных timedelta
Тип данных `timedelta` представляет собой временной интервал (разница между двумя объектами `datetime` или `date`) и используется для удобного выполнения различных манипуляций над типами `datetime` или `date`.

При создании объекта `timedelta` можно указать следующие аргументы:
- недели (`weeks`)
- дни (`days`)
- часы (`hours`)
- минуты (`minutes`)
- секунды (`seconds`)
- миллисекунды (`milliseconds`)
- микросекунды (`microseconds`)

Мы можем выбрать любые их сочетания для задания временного интервала, при этом все аргументы являются необязательными и по умолчанию равны `0`.
```python
from datetime import timedelta
delta = timedelta(days=7, hours=20, minutes=7, seconds=17)
print(delta) # 7 days, 20:07:17
print(type(delta)) # <class 'datetime.timedelta'>
```
Аргументы могут быть целыми числами или числами с плавающей запятой, а также могут быть как положительными, так и **отрицательными**. Используйте именованные аргументы, вместо позиционных, чтобы избежать ошибок.

Тип `timedelta` внутренне хранит только сочетание `days, seconds, microseconds`, а остальные переданные в конструктор аргументы конвертируются в эти единицы:

- `milliseconds` преобразуется в 10001000 `microseconds`
- `minutes` преобразуется в 60 `seconds`
- `hours` преобразуется в 3600 `seconds`
- `weeks` преобразуется в 7 `days`
```python
from datetime import timedelta

delta1 = timedelta(days=50, seconds=27, microseconds=10, milliseconds=29000, minutes=5, hours=8, weeks=2)
delta2 = timedelta(weeks=1, hours=23, minutes=61)
delta3 = timedelta(hours=25)
delta4 = timedelta(minutes=300)

print(delta1, delta2, delta3, delta4, sep='\n')
>>> 64 days, 8:05:56.000010
>>> 8 days, 0:01:00
>>> 1 day, 1:00:00
>>> 5:00:00
```
Обратите внимание на то, что если во временном интервале (`timedelta`) значение `days` равно нулю, то оно не выводится.
Также временной интервал (`timedelta`) может быть отрицательным.
Приведенный ниже код:

```python
from datetime import timedelta

delta1 = timedelta(minutes=-40)
delta2 = timedelta(seconds=-10, weeks=-2)

print(delta1) # -1 day, 23:20:00
print(delta2) # -15 days, 23:59:50
```
## Атрибуты days, seconds, microseconds и метод total_seconds()
Как уже было сказано, тип `timedelta` внутренне хранит только сочетание `days, seconds, microseconds`, которые можно получить с помощью одноименных атрибутов.
```python
from datetime import timedelta

delta = timedelta(days=50, seconds=27, microseconds=10, milliseconds=29000, minutes=5, hours=8, weeks=2)

print('Количество дней =', delta.days) # Количество дней = 64
print('Количество секунд =', delta.seconds) # Количество секунд = 29156
print('Количество микросекунд =', delta.microseconds) # Количество микросекунд = 10
print('Общее количество секунд =', delta.total_seconds()) # Общее количество секунд = 5558756.00001
```

Метод `total_seconds()` возвращает общее количество секунд, содержащееся во временном интервале`timedelta`.

Обратите внимание на то, что у типа `timedelta` нет атрибутов `hours` и `minutes`, позволяющих получить количество часов и минут соответственно. Достать часы и минуты можно так:
```python
from datetime import timedelta

def hours_minutes(td):
    return td.seconds // 3600, (td.seconds // 60) % 60

delta = timedelta(days=7, seconds=125, minutes=10, hours=8, weeks=2)
hours, minutes = hours_minutes(delta)

print(delta) # 21 days, 8:12:05
print(hours) # 8
print(minutes) # 12
```
## Сравнение временных интервалов

Временные интервалы (тип `timedelta`) можно сравнивать (`==, !=, <, >, <=, >=`), как и любые другие типы данных.
```python
from datetime import timedelta

delta1 = timedelta(weeks=1)
delta2 = timedelta(hours=24*7)
delta3 = timedelta(minutes=24*7*59)

print(delta1 == delta2) # True
print(delta1 != delta3) # True
print(delta1 < delta3) # False
```
Операторы сравнения `==` или `!=` всегда возвращают значение `bool`, независимо от типа сравниваемого объекта.
```python
from datetime import timedelta

delta1 = timedelta(seconds=57)
delta2 = timedelta(hours=25, seconds=2)

print(delta1 != 57) # True
print(delta2 == '5') # False
```
Для всех других операторов сравнения, таких как `<, >, <=, >=`, когда объект `timedelta` сравнивается с объектом другого типа, возникает ошибка (исключение) `TypeError`.

```python
from datetime import timedelta

delta1 = timedelta(seconds=57)
delta2 = timedelta(hours=25, seconds=2)

print(delta2 > delta1)     # тут все ок
print(delta2 > 5)
```
приводит к возникновению ошибки:
```no-highlight
TypeError: '>' not supported between instances of 'datetime.timedelta' and 'int'
```

## Операции над временными интервалами timedelta
