```python
В данном примере body параметр является не обязательным

from fastapi import FastAPI 
from pydantic import BaseModel 

app = FastAPI() 

class Item(BaseModel): 
	name: str 
	description: str | None = None 
	price: float 
	tax: float | None = None 
	
@app.put("/items/{item_id}") 
async def update_item( 
		item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)], 
		q: str | None = None, 
		item: Item | None = None, ): 
	results = {"item_id": item_id} 
	if q: results.update({"q": q}) 
	if item: results.update({"item": item}) 
	return results
```

Можно определить как одно тело запроса, так и несколько

```python
from fastapi import FastAPI 
from pydantic import BaseModel 

app = FastAPI() 

class Item(BaseModel): 
	name: str 
	description: str | None = None 
	price: float 
	tax: float | None = None 
	
class User(BaseModel): 
	username: str 
	full_name: str | None = None 
	
@app.put("/items/{item_id}") 
async def update_item(
		item_id: int, 
		item: Item, 
		user: User): 
	results = {"item_id": item_id, "item": item, "user": user} 
	return results
```
```python
Обратите внимание, что хотя параметр `item` был объявлен таким же способом, как и раньше, теперь предпологается, что он находится внутри тела с ключом `item`.



{ 
	 "item": { 
		 "name": "Foo", 
		 "description": "The pretender", 
		 "price": 42.0, 
		 "tax": 3.2 }, 
	 "user": { 
		 "username": "dave", 
		 "full_name": "Dave Grohl" 
		 } 
}
```

```python
Можно указать Body(embed=True) для того что бы получить JSON с ключом `item`
@app.put("/items/{item_id}") 
async def update_item(
		item_id: int, 
		item: Annotated[Item, Body(embed=True)]): 
	results = {"item_id": item_id, "item": item} 
	return results
```

```python
И тогда будет ожидать JSON
{ 
	 "item": { 
		 "name": "Foo", 
		 "description": "The pretender", 
		 "price": 42.0, 
		 "tax": 3.2 
	 }
}

а не такой 

{ 
	 "name": "Foo", 
	 "description": "The pretender", 
	 "price": 42.0, 
	 "tax": 3.2 
}
```


```python

from fastapi import Body, FastAPI from pydantic import BaseModel, Field app = FastAPI() class Item(BaseModel): name: str description: str | None = Field( default=None, title="The description of the item", max_length=300 ) price: float = Field(gt=0, description="The price must be greater than zero") tax: float | None = None @app.put("/items/{item_id}") async def update_item(item_id: int, item: Item = Body(embed=True)): results = {"item_id": item_id, "item": item} return results
```