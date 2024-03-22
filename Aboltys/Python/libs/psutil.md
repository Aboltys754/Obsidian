
https://pypi.org/project/psutil/

Выводит список имен и pid процессов. Проверяя если имя равно chrome
``` python
process_names = [[proc.name(), proc.pid] for proc in psutil.process_iter() if proc.name() == "chrome.exe"]
```
