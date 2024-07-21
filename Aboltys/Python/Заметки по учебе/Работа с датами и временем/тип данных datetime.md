1. [[#Тип данных datetime]]
2. Методы `combine(), date(), time()`
3. Методы `now(), utcnow(), today()`
4. Метод `timestamp()`
5. Форматирование даты-времени
6. Преобразование строки в дату-время

## Тип данных datetime

Типы данных `date` и `time` позволяют работать по отдельности с датами и временами. Однако на практике чаще требуется работать одновременно и с датой, и со временем. Для таких целей используется тип данных `datetime` из одноименного модуля `datetime`.
```python
from datetime import datetime
```
При создании новой даты-времени (тип `datetime`) нужно указать год, месяц, день, часы, минуты, секунды и микросекунды. При этом год, месяц и день являются **обязательными**, а часы, минуты, секунды и микросекунды **необязательными**.
```python
from datetime import datetime 
my_datetime = datetime(1992, 10, 6, 9, 40, 23, 51204) # создаем полную дату-время 
only_date = datetime(2021, 12, 31) # создаем дату-время с нулевой временной информацией 
print(my_datetime) 
print(only_date) 
print(type(my_datetime))
>>> 1992-10-06 09:40:23.051204 
>>> 2021-12-31 00:00:00 
>>> <class 'datetime.datetime'>
```
Конструктор типа `datetime` сначала принимает год, месяц, день, часы, минуты, секунды, а уже потом микросекунды. Мы также можем использовать именованные аргументы, нарушая указанный порядок `datetime(day=6, month=10, year=1992, second=23, minute=40, microsecond=51204, hour=9)`.

Получить доступ к ним можно с помощью атрибутов:
- `year` — год
- `month` — месяц
- `day` — день
- `hour` — час
- `minute` — минуты
- `second` — секунды
- `microsecond` — микросекунды

```python
from datetime import datetime 
my_datetime = datetime(1992, 10, 6, 9, 40, 23, 51204) 
print('Год =', my_datetime.year) 
print('Месяц =', my_datetime.month) 
print('День =', my_datetime.day) 
print('Часы =', my_datetime.hour) 
print('Минуты =', my_datetime.minute) 
print('Секунды =', my_datetime.second) 
print('Микросекунды =', my_datetime.microsecond)
```