### `**.get_cookies()**`

В коде ниже использован метод `.get_cookies()`**,** который получает список всех **cookie** на странице. Выполните код ниже у себя в терминале.

```python
from pprint import pprint
from selenium import webdriver

with webdriver.Chrome() as webdriver:
    webdriver.get('https://ya.ru/')
    cookies = webdriver.get_cookies()
    pprint(cookies)

>>>
[{'domain': '.ya.ru',
  'expiry': 1685518907,
  'httpOnly': False,
  'name': '_ym_d',
  'path': '/',
  'sameSite': 'None',
  'secure': True,
  'value': '1653982908'},
  ...
   {'domain': '.ya.ru',
  'expiry': 1656574906,
  'httpOnly': False,
  'name': 'yandex_gid',
  'path': '/',
  'sameSite': 'None',
  'secure': True,
  'value': '239'}]
```

Обратите внимание на то, что список **cookies** — это список **словарей,** т.е. каждая **cookie** представляет собой **словарь**!

### `**.get_cookie(name_cookie)**`

В отличие от первого метода, этот метод находит и возвращает **cookie** по его имени. Есть два способа определить имя. 

- Способ №1 - этот способ не очень надежен, т.к. с "живого" браузера данные в **cookies** могут отличаться в зависимости от открытой сессии. Но если ваш код не зависит от параметров сессии, то можно получить имена **cookie** именно в браузере;
    - ![](https://ucarecdn.com/da70ce48-6f33-4b4f-83da-24823222a1c8/)
- Способ №2 - мы можем в цикле **for/in** итерироваться по списку **cookie,** который мы получили с помощью метода `.**get_cookies()**` . Этим способом мы можем получить не только имя **cookie,** но и его значение.
    - ```python
        from selenium import webdriver
        
        with webdriver.Chrome() as webdriver:
            webdriver.get('https://ya.ru/')
            cookies = webdriver.get_cookies()
            for cookie in cookies:
                print(cookie['name']) # или cookie['value'] чтобы получить их значение
        >>>
        _ym_d, _ym_isad, _ym_uid, my, gdpr, _yasc, i, is_gdpr, yuidss
        yabs-frequency, is_gdpr_b, yandexuid, yp, mda, ymex, yandex_gid
        ```
        
    - Когда мы знаем имена всех **cookie** на странице, мы можем получить нужные нам данные по ключу. Мы помним, что `.get_cookies()` возвращает список словарей.  Если вы посмотрите на первый пример с кодом, вы увидите, что в cookie хранится время экспирации `'expiry': 1685518907` т.е., время истечения срока жизни **cookie**. Пример кода ниже поможет нам извлечь конкретное значение из cookie.
        - ```python
            from selenium import webdriver
            
            with webdriver.Chrome() as webdriver:
                webdriver.get('https://ya.ru/')
                print(webdriver.get_cookie('_ym_uid')['expiry'])
            
            >>>1685520499
            ```