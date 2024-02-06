
Postgres:

установка библиотеки для общения с postgres

```python
pip install psycopg2
```

Настройка в settings
```python
DATABASES = {  
    "default": {  
        "ENGINE": "django.db.backends.postgresql",  
        'NAME': '<dbname>',  
        'USER': 'postgres',  
        'PASSWORD': '<password>',  
        'HOST': 'localhost',  
        'PORT': 5432,  
    }  
}
```