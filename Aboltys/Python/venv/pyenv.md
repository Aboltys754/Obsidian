https://habr.com/ru/articles/599441/

```
curl https://pyenv.run | bash
```

Если выходит ошибка надо обновить пакеты
```bash
udo apt update; sudo apt install build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev curl \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
```


```python
pyenv install 3.10.4

pyenv install -l

pyenv global 3.10.4
```

изменив версию на нужную можно создавать окружение 

```python 
python3 -m venv venv
```
