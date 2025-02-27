Наиболее распространенные основные объекты метаданных базы данных в SQLAlchemy известны как [`MetaData`](https://docs.sqlalchemy.org/en/20/core/metadata.html#sqlalchemy.schema.MetaData "sqlalchemy.schema.MetaData"), [`Table`](https://docs.sqlalchemy.org/en/20/core/metadata.html#sqlalchemy.schema.Table "sqlalchemy.schema.Table")и [`Column`](https://docs.sqlalchemy.org/en/20/core/metadata.html#sqlalchemy.schema.Column "sqlalchemy.schema.Column").

Какой бы подход ни использовался, мы всегда начинаем с коллекции, в которой мы будем размещать наши таблицы, называемые объектом [`MetaData`](https://docs.sqlalchemy.org/en/20/core/metadata.html#sqlalchemy.schema.MetaData "sqlalchemy.schema.MetaData") . Этот объект, по сути, представляет собой [фасад](https://docs.sqlalchemy.org/en/20/glossary.html#term-facade) словаря Python, в котором хранится ряд [`Table`](https://docs.sqlalchemy.org/en/20/core/metadata.html#sqlalchemy.schema.Table "sqlalchemy.schema.Table")объектов, связанных с их строковыми именами. Хотя ORM предоставляет несколько вариантов получения этой коллекции, у нас всегда есть возможность просто создать ее напрямую, что выглядит так:

CORE

```python
>>> from sqlalchemy import MetaData
>>> metadata_obj = MetaData()
```

Создание таблицы

```python
>>> from sqlalchemy import Table, Column, Integer, String
>>> user_table = Table(
...     "user_account",
...     metadata_obj,
...     Column("id", Integer, primary_key=True),
...     Column("name", String(30)),
...     Column("fullname", String),
... )
```

Компоненты таблицы 
```python
>>> user_table.c.name
Column('name', String(length=30), table=<user_account>)

>>> user_table.c.keys()
['id', 'name', 'fullname']
```

Для внесения созданных таблиц используется  metadata_obj.create_all(engine)

```python
from sqlalchemy import Table, Column, Integer, String  
from sqlalchemy import MetaData, ForeignKey  
from sqlalchemy import create_engine  
  
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
  
metadata_obj.create_all(engine)
```

ORM

```python
>>> from typing import List
>>> from typing import Optional
>>> from sqlalchemy.orm import Mapped
>>> from sqlalchemy.orm import mapped_column
>>> from sqlalchemy.orm import relationship
>>> from sqlalchemy import create_engine 
>>> from sqlalchemy.orm import DeclarativeBase
>>
	SQL_POSTGRES_URL = "postgresql://postgres:postgres@localhost/sql_alchemy"  
	engine = create_engine(SQL_POSTGRES_URL) 

	class Base(DeclarativeBase):
	     pass

>>> class User(Base):
...     __tablename__ = "user_account"
...
...     id: Mapped[int] = mapped_column(primary_key=True)
...     name: Mapped[str] = mapped_column(String(30))
...     fullname: Mapped[Optional[str]]
...
...     addresses: Mapped[List["Address"]] = relationship(back_populates="user")
...
...     def __repr__(self) -> str:
...         return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

>>> class Address(Base):
...     __tablename__ = "address"
...
...     id: Mapped[int] = mapped_column(primary_key=True)
...     email_address: Mapped[str]
...     user_id = mapped_column(ForeignKey("user_account.id"))
...
...     user: Mapped[User] = relationship(back_populates="addresses")
...
...     def __repr__(self) -> str:
...         return f"Address(id={self.id!r}, email_address={self.email_address!r})"
```

Можно без указания типов

```python
class User(Base):
    __tablename__ = "user_account"

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(30), nullable=False)
    fullname = mapped_column(String)

    addresses = relationship("Address", back_populates="user")
```

Для отправки в базу используют 
```python
Base.metadata.create_all(engine)
```


отражение таблицы

```python
some_table = Table("some_table", metadata_obj, autoload_with=engine)

```

В качестве примера отражения мы создадим новый [`Table`](https://docs.sqlalchemy.org/en/20/core/metadata.html#sqlalchemy.schema.Table "sqlalchemy.schema.Table") объект, который будет представлять собой `some_table`объект, который мы создали вручную в предыдущих разделах этого документа. Опять же, есть несколько разновидностей того, как это выполняется, однако самый простой — создать объект [`Table`](https://docs.sqlalchemy.org/en/20/core/metadata.html#sqlalchemy.schema.Table "sqlalchemy.schema.Table"), учитывая имя таблицы и [`MetaData`](https://docs.sqlalchemy.org/en/20/core/metadata.html#sqlalchemy.schema.MetaData "sqlalchemy.schema.MetaData")коллекцию, к которой он будет принадлежать, а затем вместо указания отдельных лиц [`Column`](https://docs.sqlalchemy.org/en/20/core/metadata.html#sqlalchemy.schema.Column "sqlalchemy.schema.Column")и [`Constraint`](https://docs.sqlalchemy.org/en/20/core/constraints.html#sqlalchemy.schema.Constraint "sqlalchemy.schema.Constraint")объектов передать ему цель [`Engine`](https://docs.sqlalchemy.org/en/20/core/connections.html#sqlalchemy.engine.Engine "sqlalchemy.engine.Engine") с помощью [`Table.autoload_with`](https://docs.sqlalchemy.org/en/20/core/metadata.html#sqlalchemy.schema.Table.params.autoload_with "sqlalchemy.schema.Table")параметр:

```python
>>> some_table
Table('some_table', MetaData(),
    Column('x', INTEGER(), table=<some_table>),
    Column('y', INTEGER(), table=<some_table>),
    schema=None)
```

В конце процесса `some_table`объект теперь содержит информацию об [`Column`](https://docs.sqlalchemy.org/en/20/core/metadata.html#sqlalchemy.schema.Column "sqlalchemy.schema.Column")объектах, присутствующих в таблице, и его можно использовать точно так же, как объект, [`Table`](https://docs.sqlalchemy.org/en/20/core/metadata.html#sqlalchemy.schema.Table "sqlalchemy.schema.Table")который мы объявили явно: