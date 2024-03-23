
```python
import time  

def logger(message: str, file: str = "test", level: str = "test") -> None:
    """Получает три строки. Путь, уровень ошибки и сообщение. И в зависимости от уровня записывает их в разные файлы лога"""  

    data = time.strftime("%d.%m.%Y.%H:%M:%S")
    with open(f"log\\{file}.log", "a", encoding="utf-8", ) as log:
        log.write(f"{data}, {level}, {message}\n")
    print(message)
```