[**AJAX**](https://ru.wikipedia.org/wiki/AJAX) (**Asynchronous Javascript and XML**) - позволяет обновлять данные на сайте без перезагрузки страницы. Пример: вы работаете на сайте, изменяете информацию в текстовых полях, нажимаете на кнопки, обмениваетесь данными с сервером, при этом страница ни разу не обновилась, а данные на странице изменялись многократно. Такое поведение сайта обеспечивает технология **AJAX**. Так происходит, потому что **AJAX** подгружает не всю страницу целиком, а только ее часть. На **AJAX** построено огромное количество сайтов в интернете, вы встречали их неоднократно, просто не знали, что эта технология так называется. 

Вызовы **AJAX** в основном выполняются для **API**, который возвращает объект **JSON**, который может быть легко обработан библиотекой `requests`.

Если перед вами есть кнопка, при нажатии на которую происходит загрузка данных, или это происходит при скроллинге страницы, то перед вами **AJAX**. 

Второй и более точный способ распознать AJAX - это заглянуть в инструменты разработчика и обнаружить в заголовках запроса ключ  `'x-requested-with': 'XMLHttpRequest'`.

`'x-requested-with': 'XMLHttpRequest'` - нестандартный заголовок, при запросах из JavaScript без перезагрузки страницы,  полезен для имитации **AJAX.**

Пример AJAX без серверного заголовка `'x-requested-with': 'XMLHttpRequest`, на чистом JS, на нашем [сайте](https://parsinger.ru/4.7/1/index.html) тренажёре.

![](https://ucarecdn.com/6ea07383-72d7-40c1-8643-d24611a2a167/)

Это [сайт](https://bitality.cc/) для обмена криптовалют. Это не реклама, и я не призываю пользоваться этим сайтом, пользователь в чате попросил помочь ему достать заветный **JSON** с нужными данными.  Давайте посмотрим на эти данные в **JSON**-формате, там лежит курс обмена выбранных валют. При желании можно написать бота, который будет присылать вам текущий курс обмена интересующей вас криптовалюты.

![](https://ucarecdn.com/b6530d43-134b-4c72-8bcc-657c53d69313/)

Если вы скопируете [ссылку](https://bitality.cc/Home/GetSum?GiveName=Ethereum&GetName=Bitcoin&Sum=4.1895414&Direction=0), которая находится в левой части на скриншоте выше, вы получите ошибку "**Страница bitality.cc не найдена**". Так происходит потому, что мы совершаем прямой запрос к серверу, где лежат данные, но мы не передаем ключ '`x-requested-with': 'XMLHttpRequest'`.

Давайте напишем скрипт и передадим с запросом ключ `requested-with': 'XMLHttpRequest'` и стандартный юзер-агент.

**!КОД НИЖЕ МОЖЕТ НЕ РАБОТАТЬ ИЗ-ЗА ПЕРИОДИЧЕСКОГО ВКЛЮЧЕНИЯ CLOUDFLARE НА ЭТОМ САЙТЕ. ЭТОТ САЙТ НАЙДЕН В ПРОСТОРАХ ИНТЕРНЕТА И ИСПОЛЬЗУЕТСЯ ИСКЛЮЧЕТЕЛЬНО В КАЧЕСТВЕ ПРИМЕРА!**

```python
import requests
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
}

url = "https://bitality.cc/Home/GetSum?GiveName=Ethereum&GetName=Bitcoin&Sum=4.1895414&Direction=0"
response = requests.get(url=url, headers=headers).json()
print(response)

>>> {'giveSum': '4.1895414', 'getSum': '0.25619551'}
```

После запуска кода мы видим, что все отработало как мы и ждали, в консоли напечатался тот же самый **JSON** с данными, пусть немного с другими, т.к. курс постоянно колеблется. 

**Почему AJAX делает парсинг сложнее?**

Как вы уже знаете, AJAX позволяет веб-страницам динамически загружать данные без перезагрузки страницы. Это означает, что при первоначальной загрузке страницы некоторые данные могут отсутствовать. Они загружаются позже, когда происходит AJAX-запрос. Именно поэтому традиционные методы парсинга могут не сработать