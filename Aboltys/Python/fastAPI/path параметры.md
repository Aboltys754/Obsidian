
При создании _операций пути_ можно столкнуться с ситуацией, когда путь является фиксированным.

Например, `/users/me`. Предположим, что это путь для получения данных о текущем пользователе.

У вас также может быть путь `/users/{user_id}`, чтобы получить данные о конкретном пользователе по его ID.

Поскольку _операции пути_ выполняются в порядке их объявления, необходимо, чтобы путь для `/users/me` был объявлен раньше, чем путь для `/users/{user_id}`:

```python
from fastapi import FastAPI 

app = FastAPI() 

@app.get("/users/me") 
async def read_user_me(): 
	return {"user_id": "the current user"} 
	
@app.get("/users/{user_id}") 
async def read_user(user_id: str): 
	return {"user_id": user_id}
```

Иначе путь для `/users/{user_id}` также будет соответствовать `/users/me`, "подразумевая", что он получает параметр `user_id` со значением `"me"`.

Аналогично, вы не можете переопределить операцию с путем:

```python
from fastapi import FastAPI 

app = FastAPI() 

@app.get("/users") 
async def read_users(): 
	return ["Rick", "Morty"] 
	
@app.get("/users") 
async def read_users2(): 
	return ["Bean", "Elfo"]
```

Первый будет выполняться всегда, так как путь совпадает первым.


Импортируйте `Enum` и создайте подкласс, который наследуется от `str` и `Enum`.

Мы наследуемся от `str`, чтобы документация API могла понять, что значения должны быть типа `string` и отображалась правильно.

Затем создайте атрибуты класса с фиксированными допустимыми значениями:

```python
from enum import Enum 
from fastapi import FastAPI 

class ModelName(str, Enum): 
	alexnet = "alexnet" 
	resnet = "resnet" 
	lenet = "lenet" 
	
app = FastAPI() 

@app.get("/models/{model_name}") 
async def get_model(model_name: ModelName): 
	if model_name is ModelName.alexnet: 
		return {"model_name": model_name, "message": "Deep Learning FTW!"} 
	if model_name.value == "lenet": 
		return {"model_name": model_name, "message": "LeCNN all the images"} 
	return {"model_name": model_name, "message": "Have some residuals"}
```