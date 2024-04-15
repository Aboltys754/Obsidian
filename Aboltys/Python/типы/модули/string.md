Встроенный модуль `string` раньше использовался для расширения стандартных возможностей (функционала) строкового типа данных `str`. На текущий момент все функции из модуля `string` переехали в методы строкового типа данных `str`, однако в модуле `string` остались удобные константные строки, которые можно использовать при решении задач.

```python
import string 
print(string.ascii_letters) 
print(string.ascii_uppercase) 
print(string.ascii_lowercase) 
print(string.digits) 
print(string.hexdigits) 
print(string.octdigits) 
print(string.punctuation) 
print(string.printable)

>>> abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 
>>> ABCDEFGHIJKLMNOPQRSTUVWXYZ 
>>> abcdefghijklmnopqrstuvwxyz 
>>> 0123456789 
>>> 0123456789abcdefABCDEF 
>>> 01234567 
>>> !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ 
>>> 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ \t\n\r\x0b\x0c
```