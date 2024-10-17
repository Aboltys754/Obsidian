
Перед тем как начать работу с библиотекой [Requests](https://requests.readthedocs.io/en/latest/), убедитесь, что она установлена в вашей системе. Если же нет, её можно установить с помощью команды:
```cmake
pip3 install requests
```
Сразу после установки `requests` можно полноценно использовать.
Импорт библиотеки `requests` производится следующим образом:
```haskell
import requests
```
#### Простой GET-запрос

Для начала давайте сделаем простой GET-запрос к сайту. Это как когда вы вбиваете URL в браузере и жмёте Enter. Только теперь всё будет в коде:

```dart
import requests

response = requests.get('https://www.example.com')
print(response.text)
```