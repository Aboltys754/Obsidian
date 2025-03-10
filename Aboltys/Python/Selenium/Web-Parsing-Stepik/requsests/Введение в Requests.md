[[#Параметры запроса и передача данных]]
[[#Аутентификация и безопасность]]
[[#Сессии и сохранение состояния]]
[[#Обработка исключений]]
[[#Работа с файлами и мультимедиа]]
[[#Потоковая передача данных]]
[[#Преимущества]]
[[#Недостатки]]
[[#Передача данных в формате JSON]]
[[#Работа с куками]]
[[#Следование редиректам]]


Библиотека [requests](https://requests.readthedocs.io/en/master/)

Библиотека Requests в Python значительно упрощает процесс формирования HTTP-запросов. Трудно представить разработку парсера без использования этой библиотеки или её аналогов.

HTTP-запросы являются фундаментом Всемирной паутины. Каждый раз, когда вы открываете веб-страницу, ваш браузер отправляет на сервер множество запросов. В ответ сервер предоставляет все необходимые данные для отображения страницы. Только после этого ваш браузер может корректно отобразить веб-сайт для вашего просмотра.

С помощью запросов к HTML или API сайтов можно извлекать разнообразные данные: от информации о погоде и итогов спортивных состязаний до рейтингов фильмов, твитов, результатов поисковых систем, изображений и многого другого.

В этом разделе курса мы рассмотрим наиболее полезные методы библиотеки Requests. Научимся формировать запросы для различных сценариев, которые часто возникают при создании парсера. В частности, мы обсудим:

- Формирование запросов с использованием различных HTTP-методов;
- Редактирование заголовков запросов, параметров User-Agent, прокси и т. д.;
- Анализ данных запросов и ответов;
- Настройку запросов так, чтобы минимизировать риски возникновения нежелательных ситуаций.

**Requests** — это не просто библиотека для отправки HTTP-запросов. Это целый инструментарий, который позволяет разрабатывать сложные и функциональные парсеры, обеспечивая при этом высокий уровень безопасности и удобство работы. С его помощью можно не только извлекать, но и отправлять, анализировать и обрабатывать данные, делая вашу работу с интернет-ресурсами максимально эффективной.

### Параметры запроса и передача данных

Когда дело доходит до передачи данных на сервер или запроса конкретной информации, **Requests** позволяет делать это легко и непринуждённо. С помощью параметров URL или тела запроса можно передавать данные в виде ключ-значение, что открывает широкие возможности для интерактивной работы с веб-ресурсами.

```csharp
# Указываем параметры запроса в виде словаря
params = {'key1': 'value1', 'key2': 'value2'}
response = requests.get('https://www.example.com', params=params)
```

### Аутентификация и безопасность

Важным аспектом при работе с HTTP-запросами является безопасность. **Requests** предлагает механизмы для аутентификации, которые защищают ваши запросы и данные. Это может быть базовая аутентификация с использованием логина и пароля или, например, более сложные механизмы с использованием токенов и ключей.

```csharp
from requests.auth import HTTPBasicAuth

# Указываем логин и пароль
response = requests.get('https://www.example.com', auth=HTTPBasicAuth('user', 'pass'))
```

### Сессии и сохранение состояния

Иногда требуется не просто отправить одиночный запрос, а выполнить целую последовательность действий. В таких случаях на помощь приходят сессии, которые позволяют сохранять между запросами определенное состояние — куки, заголовки и так далее. Это экономит время и упрощает код, особенно при написании сложных парсеров.

```csharp
# Создаем сессию
with requests.Session() as s:
    s.get('https://www.example.com/login')
    response = s.get('https://www.example.com/data')
```

### Обработка исключений

Сетевая работа всегда подвержена различным ошибкам и исключениям. **Requests** предоставляет удобные средства для обработки этих моментов. От таймаутов и отсутствия сети до ошибок на стороне сервера — зная, как с этим работать, вы сможете создать устойчивые и надёжные парсеры.

```python
try:
    response = requests.get('https://www.example.com', timeout=1)
except requests.Timeout:
    print("Слишком долгое ожидание!")
except requests.RequestException as e:
    print(f"Произошла ошибка: {e}")
```

### Работа с файлами и мультимедиа

Не менее интересной является возможность работы с файлами. Загрузка изображений, аудио, видео или даже больших данных для анализа — всё это можно сделать с помощью **Requests**. Это открывает двери для широкого спектра задач, начиная от автоматизации рабочих процессов и заканчивая сбором данных для научных исследований.

```csharp
# Открываем файл и отправляем его на сервер
with open('file.txt', 'rb') as f:
    files = {'file': f}
    response = requests.post('https://www.example.com/upload', files=files)
```

### Потоковая передача данных

Для больших объемов данных или работы в реальном времени **Requests** предлагает потоковую передачу. Это особенно актуально для тех, кто работает с большими файлами или стриминговыми сервисами. Потоковая передача обеспечивает эффективное использование ресурсов и быстрый отклик.

```python
# Загрузка файла с сервера по частям
with requests.get('https://www.example.com/file', stream=True) as r:
    with open('file.txt', 'wb') as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)
```

По мере глубокого погружения в работу с библиотекой Requests, становится ясно, что у неё есть свои преимущества и недостатки.

### Преимущества:

- **Простота и интуитивность**: Первое, что бросается в глаза при работе с Requests, — это чистота и понятность кода. Не требуется большого количества строк кода для выполнения даже сложных HTTP-запросов.
    
- **Функциональность**: Requests поддерживает множество методов HTTP, работу с куками, сессиями, заголовками и так далее. Эта библиотека предлагает решения для большинства задач, связанных с веб-скрапингом и API.
    
- **Безопасность и аутентификация**: Библиотека предоставляет встроенные механизмы для различных типов аутентификации, что делает ваш код не только короче, но и безопаснее.
    
- **Хорошая документация и сообщество**: Большое количество ресурсов, примеров и активное сообщество делают процесс изучения и работы с Requests намного проще.
    
- **Переиспользуемость кода**: Благодаря высокому уровню абстракции, код, написанный с использованием Requests, легко переиспользовать в других проектах.
    

### Недостатки:

- **Не всегда подходит для асинхронного программирования**: Хотя существуют асинхронные форки и адаптации, сама по себе библиотека не предназначена для асинхронных операций (_aiohttp мы будет разбирать в модуле Асинхронный парсинг_). .
    
- **Зависимости**: Для некоторых специфичных задач, например, работы с WebSockets или определёнными типами аутентификации, может потребоваться установка дополнительных библиотек.
    
- **Потребление ресурсов**: При работе с большими объёмами данных или множеством одновременных соединений, Requests может быть менее эффективным по сравнению с некоторыми альтернативными решениями.
    
- **Недостаток некоторых продвинутых функций**: В то время как для большинства задач функционала Requests будет более чем достаточно, в некоторых случаях может потребоваться использование более специализированных библиотек.
    

### Передача данных в формате JSON

Работая с современными веб-сервисами, часто приходится сталкиваться с форматом данных JSON. Благодаря Requests, работа с JSON становится удивительно простой:

```python
# Отправляем данные в формате словаря dict

data = {'name': 'John', 'age': 30}
response = requests.post('https://www.example.com/api', json=data)
```

### Работа с куками

Куки — ещё один важный аспект, с которым вы столкнётесь, работая с HTTP-запросами. Requests делает работу с куками простой и интуитивной:

```csharp
# Использование куки в сессии
with requests.Session() as s:
    s.get('https://www.example.com/login')
    cookies = dict(cookies_are='working')
    response = s.get('https://www.example.com/data', cookies=cookies)
```

### Следование редиректам

Когда сервер перенаправляет ваш запрос на другой URL, Requests может автоматически следовать этим редиректам, что упрощает жизнь:

```ini
# Автоматическое следование редиректам
response = requests.get('https://www.example.com/redirect', allow_redirects=True)
```