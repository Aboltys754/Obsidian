
INSERT

```python
from sqlalchemy import Table, Column, Integer, String  
from sqlalchemy import MetaData, ForeignKey  
from sqlalchemy import create_engine  
from sqlalchemy import insert  
  
SQL_POSTGRES_URL = "postgresql://postgres:postgres@localhost/sql_alchemy"  
engine = create_engine(SQL_POSTGRES_URL)  
  
metadata_obj = MetaData()  
  
user_table = Table(  
    "user_account",  
    metadata_obj,  
    Column("user_id", Integer, primary_key=True),  
    Column("name", String(30)),  
    Column("fullname", String)  
)  
  
address_table = Table(  
    "address",  
    metadata_obj,  
    Column("address_id", Integer, primary_key=True),  
    Column("user_id", ForeignKey("user_account.user_id"), nullable=False),  
    Column("email_address", String, nullable=False),  
)  

создаем строку для SQL
stmt = insert(user_table).values(name="spongebob", fullname="Spongebob Squarepants")  

Подключаемся к базе и передаем туда строку. После делаем коммит
with engine.connect() as conn:  
    result = conn.execute(stmt)  
    conn.commit()  

Отправляем все в базу
metadata_obj.create_all(engine)
```

Можно так же напрямую добавлять без переменных

```python
with engine.connect() as conn:
     result = conn.execute(
         insert(user_table),
         [
             {"name": "sandy", "fullname": "Sandy Cheeks"},
             {"name": "patrick", "fullname": "Patrick Star"},
         ],
     )
     conn.commit()
```

Можно вернуть последнее вставленное значение returning()

```python
insert_stmt = insert(address_table).returning(
    address_table.c.id, address_table.c.email_address
)
print(insert_stmt)

INSERT INTO address (id, user_id, email_address) 
VALUES (:id, :user_id, :email_address) 
RETURNING address.id, address.email_address
```

Также можно использовать from.select()

```python
 select_stmt = select(user_table.c.id, user_table.c.name + "@aol.com")
 insert_stmt = insert(address_table).from_select(
     ["user_id", "email_address"], select_stmt
 )
 print(insert_stmt.returning(address_table.c.id, address_table.c.email_address))
```

SELECT

