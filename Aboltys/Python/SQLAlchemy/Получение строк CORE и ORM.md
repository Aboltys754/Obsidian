```python
 with engine.connect() as conn:
     result = conn.execute(text("SELECT x, y FROM some_table"))
     for row in result:
         print(f"x: {row.x}  y: {row.y}")

```

```SQl
BEGIN (implicit)
SELECT x, y FROM some_table
[...] ()

x: 1  y: 1
x: 2  y: 4
x: 6  y: 8
x: 9  y: 10

ROLLBACK
```


- **Назначение кортежа** . Это наиболее идиоматический стиль Python, который заключается в назначении переменных каждой строке позиционно по мере их получения:
- 
```python
result = conn.execute(text("select x, y from some_table")) 
	for x, y in result:
		...
``` 

- **Целочисленный индекс** . Кортежи представляют собой последовательности Python, поэтому доступен также обычный целочисленный доступ:
  
```python
result = conn.execute(text("select x, y from some_table"))   
   for row in result:
	   x = row[0]
```

- **Имя атрибута** . Поскольку это кортежи с именами Python, кортежи имеют имена динамических атрибутов, соответствующие именам каждого столбца. Эти имена обычно являются именами, которые оператор SQL присваивает столбцам в каждой строке. Хотя они обычно довольно предсказуемы и могут управляться с помощью меток, в менее определенных случаях они могут зависеть от поведения, специфичного для базы данных:
- 
```python
result = conn.execute(text("select x, y from some_table"))    
    for row in result:
        y = row.y    
        # illustrate use with Python f-strings
        print(f"Row: {row.x} {y}")
``` 

- **Доступ к сопоставлению** . Чтобы получать строки в виде объектов **сопоставления** Python , которые по сути являются доступной только для чтения версией интерфейса Python для общего `dict` объекта, их [`Result`](https://docs.sqlalchemy.org/en/20/core/connections.html#sqlalchemy.engine.Result "sqlalchemy.engine.Result")можно **преобразовать** в [`MappingResult`](https://docs.sqlalchemy.org/en/20/core/connections.html#sqlalchemy.engine.MappingResult "sqlalchemy.engine.MappingResult")объект с помощью [`Result.mappings()`](https://docs.sqlalchemy.org/en/20/core/connections.html#sqlalchemy.engine.Result.mappings "sqlalchemy.engine.Result.mappings")модификатора; это объект результата, который возвращает [`RowMapping`](https://docs.sqlalchemy.org/en/20/core/connections.html#sqlalchemy.engine.RowMapping "sqlalchemy.engine.RowMapping")объекты, подобные словарю, а не [`Row`](https://docs.sqlalchemy.org/en/20/core/connections.html#sqlalchemy.engine.Row "sqlalchemy.engine.Row")объекты:

```python
result = conn.execute(text("select x, y from some_table"))
   for dict_row in result.mappings():
		x = dict_row["x"]
        y = dict_row["y"]
```

```python
>>> with engine.connect() as conn:
...     result = conn.execute(text("SELECT x, y FROM some_table WHERE y > :y"), {"y": 2})
...     for row in result:
...         print(f"x: {row.x}  y: {row.y}")

BEGIN (implicit)
SELECT x, y FROM some_table WHERE y > ?
[...] (2,)

x: 2  y: 4
x: 6  y: 8
x: 9  y: 10

ROLLBACK
```

Выполнение с помощью  ORM

```python
>>> from sqlalchemy.orm import Session

>>> stmt = text("SELECT x, y FROM some_table WHERE y > :y ORDER BY x, y")
>>> with Session(engine) as session:
...     result = session.execute(stmt, {"y": 6})
...     for row in result:
...         print(f"x: {row.x}  y: {row.y}")

BEGIN (implicit)
SELECT x, y FROM some_table WHERE y > ? ORDER BY x, y
[...] (6,)

x: 6  y: 8
x: 9  y: 10
x: 11  y: 12
x: 13  y: 14

ROLLBACK
```

```python
>>> with Session(engine) as session:
...     result = session.execute(
...         text("UPDATE some_table SET y=:y WHERE x=:x"),
...         [{"x": 9, "y": 11}, {"x": 13, "y": 15}],
...     )
...     session.commit()

BEGIN (implicit)
UPDATE some_table SET y=? WHERE x=?
[...] [(11, 9), (15, 13)]
COMMIT
```