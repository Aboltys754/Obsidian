вы можете определить некоторые параметры как обязательные, некоторые - со значением по умолчанию, а некоторые - полностью необязательные:

```python
from fastapi import FastAPI 

app = FastAPI() 

@app.get("/items/{item_id}") 
async def read_user_item( 
	item_id: str, needy: str, skip: int = 0, limit: int | None = None 
			): 
	item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit} 
	return item
```

Параметры в Query() запросе

```python
max_length или min_length минимальная или максимальная длинна запроса

async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
```

```python
значение по умолчанию. default=None означает что параметр не обязателен

async def read_items(q: str | None = Query(default=None, max_length=50)):
```

```python
можно использовать регулярные выражения

async def read_items( q: Annotated[ str | None, Query(min_length=3, max_length=50, pattern="^fixedquery$") ] = None, ):
```

```python
"fixedquery" Может быть любая строка. Указанная по умолчанию если параметр не пришел. Так же указание параметра по умолчанию показывает что парраметр в запросе не обязателен

async def read_items(q: Annotated[str, Query(min_length=3)] = "fixedquery"):
```

```python
Если не указать какой либо параметр по умолчанию, то параметр станет обязательным

async def read_items(q: Annotated[str, Query(min_length=3)]):
```

```python
"..." означает что параметр обязателен без указания значения по умолчанию

async def read_items(q: Annotated[str, Query(min_length=3)] = ...):
```

```python
Так же что параметр можно указать через библиотеку pydantic
from pydantic import Required

async def read_items(q: Annotated[str, Query(min_length=3)] = Required):
```

```python
Если в запросе несколько раз встречается один и тот же параметр, то можно получить список параметра

http://localhost:8000/items/?q=foo&q=bar

async def read_items(q: Annotated[list[str] | None, Query()] = None):

{ "q": [ "foo", "bar" ] }
```

```python
Так же можно указать значения по умолчанию для списка

async def read_items(q: Annotated[list[str], Query()] = ["foo", "bar"]):
```

```python
можно указать название query-параметра, используя параметр `title`:

async def read_items( q: Annotated[str | None, Query(title="Query string", min_length=3)] = None ):
```

```python
можно добавить описание, используя параметр `description`:
async def read_items( 
			q: Annotated[ str | None, 
			Query( 
				title="Query string", 
				description="Query string for the items to search in the database that have a good match", 
				min_length=3, ), 
			] = None, ):

```

```python
можете объявить `псевдоним`, и этот псевдоним будет использоваться для поиска значения параметра запроса. Например если запрос может придти не валидный  'item-query'

http://127.0.0.1:8000/items/?item-query=foobaritems

async def read_items(q: Annotated[str | None, Query(alias="item-query")] = None):

```

```python
Предположим, вы больше не хотите использовать какой-либо параметр. Вы решили оставить его, потому что клиенты всё ещё им пользуются. Но вы хотите отобразить это в документации как устаревший функционал.
Тогда для `Query` укажите параметр `deprecated=True`:

async def read_items( 
	q: Annotated[ str | None, 
				Query( alias="item-query", 
				title="Query string", 
				description="Query string for the items to search in the database that have a good match", 
				min_length=3, 
				max_length=50, 
				pattern="^fixedquery$", 
				deprecated=True, ),
```

```python
Чтобы исключить query-параметр из генерируемой OpenAPI схемы (а также из системы автоматической генерации документации), укажите в `Query` параметр `include_in_schema=False`:

async def read_items( hidden_query: Annotated[str | None, 
					  Query(include_in_schema=False)] = None ):
```