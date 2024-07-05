https://docs.python.org/3/library/fractions.html

```d
В Python нельзя совершать арифметические операции (`+`, `-`, `*`, `/`) между типами  Decimal и Fraction.
```

`Fraction` - это числовой тип данных , который представляет из себя [обыкновенную дробь](https://ru.wikipedia.org/wiki/%D0%94%D1%80%D0%BE%D0%B1%D1%8C_(%D0%BC%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B0)#.D0.9E.D0.B1.D1.8B.D0.BA.D0.BD.D0.BE.D0.B2.D0.B5.D0.BD.D0.BD.D1.8B.D0.B5_.D0.B4.D1.80.D0.BE.D0.B1.D0.B8), с заданными числителем и знаменателем;

Для работы с рациональными числами в Python используется тип данных `Fraction`. Тип данных `Fraction` как и `Decimal` реализован программно, поэтому он в разы медленнее встроенных числовых типов данных `int` и `float`. Тип данных `Fraction` неизменяемый. Операции над данными этого типа приводят к созданию новых объектов, при этом старые не меняются.
```python
from fractions import Fraction
```
Создать `Fraction` число можно несколькими способами:

- из целых чисел, передав значения числителя и знаменателя дроби,
- из строки на основании десятичного представления;
- из строки на основании обыкновенной дроби;
- из числа с плавающей точкой (не рекомендуется).
```python
from fractions import Fraction 
num1 = Fraction(3, 4) # 3 - числитель, 4 - знаменатель 
num2 = Fraction('0.55') 
num3 = Fraction('1/9') 
print(num1, num2, num3, sep='\n')

>>>3/4 
>>>11/20 
>>>1/9
```
Нужно быть очень внимательным при создании `Fraction` чисел из чисел с плавающей точкой (`float`), потому что `float` числа округляются внутри до ближайшего возможного, а `Fraction` об этом ничего не знает, поэтому копирует содержимое `float`.

Обратите внимание на то, что при создании рационального числа `Fraction`, автоматически происходит сокращение числителя и знаменателя дроби.
```python
from fractions import Fraction 
num1 = Fraction(5, 10) 
num2 = Fraction('75/100') 
num3 = Fraction('0.25') 
print(num1, num2, num3, sep='\n')

>>> 1/2 
>>> 3/4 
>>> 1/4
```
Также стоит обратить внимание на вывод дробей, являющихся целыми числами.
```python
from fractions import Fraction 
num1 = Fraction(5, 1) # 5/1 = 5 
num2 = Fraction(23, 23) # 23/23 = 1 
print(num1, num2, sep='\n')
>>> 5 
>>> 1
```
### Сравнение Fraction чисел
`Fraction` числа можно сравнивать между собой точно так же, как и любые другие числа. Доступны 66 основных операторов сравнения:

- `>`: больше;
- `<`: меньше;
- `>=`: больше либо равно;
- `<=`: меньше либо равно;
- `==`:  в точности равно;
- `!=`: не равно.
```python
from fractions import Fraction 
num1 = Fraction(1, 2) # 1/2 
num2 = Fraction(15, 30) # 15/30=1/2 
num3 = Fraction(3, 5) # 3/5 
num4 = Fraction(5, 3) # 5/3 
num5 = 1 
num6 = 0.8 

print(num1 == num2) 
print(num1 != num4) 
print(num2 > num3) 
print(num4 <= num1) 
print(num1 < num5) 
print(num6 > num4)
```
### Арифметические операции над Fraction числами

Тип данных `Fraction` отлично интегрирован в язык Python. С `Fraction` числами работают все привычные операции: сложение, вычитание, умножение, деление, возведение в степень.
```python
from fractions import Fraction 
num1 = Fraction('1/10') 
num2 = Fraction('2/3') 
print(num1 + num2) 
print(num1 - num2) 
print(num1 * num2) 
print(num1 / num2)
```
Мы также можем совершать арифметические операции над `Fraction` и целыми числами (миксовать `Fraction` и `int`), но не рекомендуется смешивать их с `float`.
```python
from fractions import Fraction 
num = Fraction('3/8') 
print(num + 1) 
print(num - 1) 
print(num * 2) 
print(num ** 4)
```
### Математические функции

`Fraction` числа можно передавать как аргументы функций, ожидающих `float`. Тогда они будут преобразованы во `float`. К примеру, модуль `math`, оперирующий `float` числами, может работать и с `Fraction` числами.
```python
from fractions import 
Fraction from math import * 
num1 = Fraction('1.44') 
num2 = Fraction('0.523') 
print(sqrt(num1)) 
print(sin(num2)) 
print(log(num1 + num2))
>>> 1.2 
>>> 0.4994813555186418 
>>> 0.6744739152943241
```
Важно понимать, что результатом работы функций модуля `math` являются `float` числа, а не `Fraction`.

### Свойства numerator и denominator
Для получения числителя и знаменателя `Fraction` числа используются свойства `numerator` и `denominator`.
```python
from fractions import Fraction 
num = Fraction('5/16') 
print('Числитель дроби равен:', num.numerator) 
print('Знаменатель дроби равен:', num.denominator)

>>> Числитель дроби равен: 5 
>>> Знаменатель дроби равен: 16
```

В Python 3.8 появился метод `as_integer_ratio()`, который возвращает кортеж, состоящий из числителя и знаменателя данного `Fraction` числа.
```python
from fractions import Fraction 
num = Fraction('-5/16') 
print(num.as_integer_ratio())
```
### Метод limit_denominator()

Метод `limit_denominator()` возвращает самую близкую к данному числу рациональную дробь, чей знаменатель не превосходит переданного аргумента.

```python
from fractions import Fraction 
import math 
print('PI =', math.pi) 
num = Fraction(str(math.pi)) 
print('No limit =', num) 
for d in [1, 5, 50, 90, 100, 500, 1000000]:
	limited = num.limit_denominator(d) 
	print(limited)
>>>PI = 3.141592653589793 
>>>No limit = 3141592653589793/1000000000000000 
>>>3 
>>>16/5 
>>>22/7 
>>>267/85 
>>>311/99 
>>>355/113 
>>>3126535/995207
```
Метод `limit_denominator()` позволяет получить очень точные рациональные приближения иррациональных чисел, что очень удобно во многих математических задачах.
