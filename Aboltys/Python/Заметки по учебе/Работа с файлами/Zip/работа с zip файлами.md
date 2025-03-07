[[#Архивирование данных]]
[[#Формат zip]]
[[#Работа с zip файлами в Python]]
-  [[#Модуль zipfile]]
- [[#Метод printdir()]]
- [[#Метод infolist()]]
- [[#Метод namelist()]]
- [[#Метод getinfo()]]
[[#Работа с конкретными файлами из архива]]
[[#Запись в zip архив]]
[[#Извлечение содержимого zip-файла в каталог]]
[[#Примечания]]


https://habr.com/ru/companies/vk/articles/490790/
https://docs.python.org/3/library/zipfile.html#command-line-interface

## Архивирование данных

**Сжатие информации** – это процесс преобразования информации, хранящейся в файле, при котором уменьшается избыточность в ее представлении и, соответственно, требуется меньший объем памяти для хранения.

Сжатие информации в файлах производится за счет устранения избыточности различными способами, например, за счет упрощения кодов, исключения из них постоянных битов или представления повторяющихся символов или повторяющейся последовательности символов в виде коэффициента повторения и соответствующих символов.

**Архивация файлов** — упаковка нескольких файлов в один файл или поток — архив. Не следует путать архивацию со сжатием, которое далеко не всегда применяется при создании архива.

**Архивный файл** – это специальным образом организованный файл, содержащий в себе один или несколько файлов в сжатом или несжатом виде и служебную информацию об именах файлов, дате и времени их создания или модификации, размерах и т.д.

Целью архивации (упаковки) файлов обычно являются обеспечение более компактного размещения информации на диске, сокращение времени и соответственно стоимости передачи информации по каналам связи в компьютерных сетях. Кроме того, упаковка в один архивный файл группы файлов существенно упрощает их перенос с одного компьютера на другой и сокращает время копирования файлов на диски.

**Степень сжатия файлов** характеризуется коэффициентом K, определяемым как отношение объема сжатого файла Vc​ к объему исходного файла Vo​_,_ выраженным в процентах:

![[Pasted image 20240922112243.png]]

Степень сжатия зависит от используемой программы, метода сжатия и типа исходного файла. Наиболее хорошо сжимаются файлы графических образов, текстовые файлы и файлы данных, для которых степень сжатия может достигать 5−40%, меньше сжимаются файлы исполняемых программ и загрузочных модулей 60−90%. Почти не сжимаются архивные файлы.

**Архивация (упаковка)** – помещение (загрузка) исходных файлов в архивный файл в сжатом или несжатом виде.

**Разархивация (распаковка)** – процесс восстановления файлов из архива точно в таком виде, какой они имели до загрузки в архив. При распаковке файлы извлекаются из архива и помещаются на диск или в оперативную память;

Программы, осуществляющие упаковку и распаковку файлов, называются программами – **архиваторами**

## Формат zip
В реальной жизни применяется большое количество различных форматов архивов: `zip, 7z, rar` и многие другие. В нашем уроке мы остановимся на `zip` архивах.

`zip` — это формат сжатия без потерь: после распаковки данные будут такими же, как перед сжатием. Алгоритм ищет избыточности в исходных данных и эффективнее представляет информацию.

Формат сжатия без потерь отличается от сжатия с потерями, который используется в таких форматах, как JPEG и MP3: при сжатии выбрасывается часть информации, которая менее заметна для человеческого глаза или уха.

Формат `zip` обладает следующими преимуществами:

- является полностью открытым
- является очень популярным (большинство архивов в Internet – это архивы `zip`)
- является очень быстрым

## Работа с zip файлами в Python

В Python для работы с `zip` архивами используется встроенный модуль `zipfile`. Основное преимущество данного модуля заключается в том, что он позволяет работать с архивом, как с обычной папкой, содержащей файлы и другие каталоги.

### Модуль zipfile
Для того чтобы начать работать с `zip` архивами в Python, нам потребуется импортировать модуль `zipfile`, в частности нам потребуется создать объект `ZipFile`.
```python
from zipfile import ZipFile
```
Объекты `ZipFile` похожи на файловые объекты, возвращаемые функцией `open()`.

### Метод printdir()
В начале работы мы создаем объект типа `ZipFile`, передавая ему имя архива (архив лежит в той же папке, что и программа).
Метод `printdir()` выводит таблицу с информацией о содержимом архива: полные названия файлов с указанием даты изменения и размера в байтах.

```python
from zipfile import ZipFile

with ZipFile('test.zip') as zip_file:
    zip_file.printdir()
```

выводит:

```no-highlight
File Name                                             Modified             Size
test/                                          2021-11-27 12:47:10            0
test/Картинки/                                 2021-11-27 12:49:02            0
test/Картинки/1.jpg                            2021-09-02 12:30:20        90156
test/Картинки/avatar.png                       2021-08-20 09:38:44        19053
test/Картинки/certificate.png                  2021-10-23 09:46:36        43699
test/Картинки/py.png                           2021-07-28 17:55:56        33522
test/Картинки/World_Time_Zones_Map.png         2021-11-08 07:30:06      2324421
test/Картинки/Снимок экрана.png                2021-10-01 20:47:02        10878
test/Неравенства.djvu                          2021-08-19 08:39:06      5283010
test/Программы/                                2021-11-27 12:48:20            0
test/Программы/image_util.py                   2021-11-18 12:42:22         4955
test/Программы/sort.py                         2021-11-14 19:31:02           61
test/Разные файлы/                             2021-11-27 12:48:10            0
test/Разные файлы/astros.json                  2021-11-08 09:29:58          505
```

При создании объекта `ZipFile` мы также можем передать необязательный аргумент `mode`, который задает режим работы (по аналогии с обычными файлами):

- `r` — файл будет открыт для чтения
- `w` — если файл существует, то он будет уничтожен и вместо него будет создан новый файл
- `a` — существующий файл будет открыт в режиме добавления в конец

По умолчанию параметр `mode` имеет значение `mode='r'`, то есть архив открывается для чтения.

### Метод infolist()

Метод `infolist()` позволяет получить информацию о файлах из архива в виде списка специальных объектов (тип `ZipInfo`), которые содержат дополнительную информацию о каждом файле:

```python
from zipfile import ZipFile  

with ZipFile('a.zip') as zip_file:
    info = zip_file.infolist()
    print(info[6].file_size)                # размер начального файла в байтах
    print(info[6].compress_size)            # размер сжатого файла в байтах
    print(info[6].filename)                 # имя файла
    print(info[6].date_time)                # дата изменения файла
    print(info[6].is_dir())                 # Является каталогом(True) или нет(False)
    print(info[6].compress_type)            # метод сжатия файла 0 файл не сжат, 8 файл                                               сжат
    print(info[6].comment)                  # Комментарий для отдельного члена архива                                                 как bytes объекта.
    print(info[6].create_version)           # Число обозначающее версию PKZIP, которая                                                создала архив ZIP.
    print(info[6].create_system)            # Код операционной системы, которая создала                                               ZIP архив.
    print(info[6].extra)                    # Содержит некоторые комментарии по                                                       внутренней структуре данных, содержащихся                                               в этом байтовом объекте.
    print(info[6].extract_version)          # Число обозначающее версию PKZIP, которая                                                необходима для распаковки архива.
    print(info[6].reserved)                 # Должно быть равно нулю.
    print(info[6].volume)                   # Возвращает номер тома заголовка файла.
```
Помимо указанных атрибутов (свойств)  доступны и другие, о которых можно почитать в официальной документации.

### Метод namelist()
Метод `namelist()` возвращает список названий файлов и директорий, содержащихся в архиве.
```python
from zipfile import ZipFile 
with ZipFile('test.zip') as zip_file: 
	info = zip_file.namelist() 
	print(*info, sep='\n')
```
### Метод getinfo()
В отличие от метода `infolist()`, который позволяет получить информацию о всех файлах из архива в виде списка специальных объектов (тип `ZipInfo`), метод `getinfo()` позволяет получить информацию о конкретном файле по его имени в архиве.

```python
from zipfile import ZipFile

with ZipFile('test.zip') as zip_file:
    info = zip_file.namelist()                # получаем названия всех файлов архива
    last_file = zip_file.getinfo(info[-4])    # получаем информацию об отдельном файле
    print(last_file.file_size)
    print(last_file.compress_size)
    print(last_file.filename)
    print(last_file.date_time)
```
выводит:
```no-highlight
4955
1641
test/Программы/image_util.py
(2021, 11, 18, 12, 42, 22)
```
## Работа с конкретными файлами из архива

Структуру архива мы получили, «вытащим» теперь и конкретный файл.

```python
from zipfile import ZipFile

with ZipFile('test.zip') as zip_file:
    with zip_file.open('test/Разные файлы/astros.json') as file:
        print(file.read())
```
выводит:
```no-highlight
b'{"number": 10, "people": [{"craft": "ISS", "name": "Mark Vande Hei"}, {"craft": "ISS", "name": "Pyotr Dubrov"}, {"craft": "ISS", "name": "Thomas Pesquet"}, {"craft": "ISS", "name": "Megan McArthur"}, {"craft": "ISS", "name": "Shane Kimbrough"}, {"craft": "ISS", "name": "Akihiko Hoshide"}, {"craft": "ISS", "name": "Anton Shkaplerov"}, {"craft": "Shenzhou 13", "name": "Zhai Zhigang"}, {"craft": "Shenzhou 13", "name": "Wang Yaping"}, {"craft": "Shenzhou 13", "name": "Ye Guangfu"}], "message": "success"}'
```

Обратите внимание на символ `b` перед выводом. Это бинарная строка. Метод `file.read()` возвращает сырые байты (тип `bytes`). Для того чтобы преобразовать их в строку (тип `str`), нужно использовать метод `decode()`, указав нужную кодировку (файл `astros.json` имеет кодировку UTF-8).

Метод `ZipFile.open()` открывает файл именно в бинарном виде, не в текстовом.

```python
from zipfile import ZipFile

with ZipFile('test.zip') as zip_file:
    with zip_file.open('test/Разные файлы/astros.json') as file:
        print(file.read().decode('utf-8'))
```
выводит:
```no-highlight
{"number": 10, "people": [{"craft": "ISS", "name": "Mark Vande Hei"}, {"craft": "ISS", "name": "Pyotr Dubrov"}, {"craft": "ISS", "name": "Thomas Pesquet"}, {"craft": "ISS", "name": "Megan McArthur"}, {"craft": "ISS", "name": "Shane Kimbrough"}, {"craft": "ISS", "name": "Akihiko Hoshide"}, {"craft": "ISS", "name": "Anton Shkaplerov"}, {"craft": "Shenzhou 13", "name": "Zhai Zhigang"}, {"craft": "Shenzhou 13", "name": "Wang Yaping"}, {"craft": "Shenzhou 13", "name": "Ye Guangfu"}], "message": "success"}
```
Обратите внимание на отсутствие символа `b`.

Прочитать подробнее про тип данных `bytes` можно в официальной [документации](https://docs.python.org/3/library/stdtypes.html#bytes-objects).

## Запись в zip архив

По аналогии с чтением файлов из архива их можно туда и записывать, для этого необходимо создать объект `ZipFile` в режимах `mode='w'` или `mode='a'`.
Для записи файла в архив используется метод `write()`, который принимает имя существующего файла.
```python
from zipfile import ZipFile

with ZipFile('archive.zip', mode='w') as zip_file:
    zip_file.write('program.py')
    zip_file.write('lse.jpeg')
    print(zip_file.namelist())
```

cоздает в папке с программой архив с именем `archive.zip` и записывает в него содержимое файлов `program.py` и `lse.jpeg`, которые так же находятся в папке с программой, а затем выводит список всех файлов данного архива:

```no-highlight
['program.py', 'lse.jpeg']
```

Если файлы для записи в архив не будут найдены, то возникнет ошибка (исключение) `FileNotFoundError`.

Метод `write()` может принимать еще один строковый аргумент, задающий новое имя файла в архиве.
```python
from zipfile import ZipFile

with ZipFile('archive.zip', mode='w') as zip_file:
    zip_file.write('program.py', 'new_program.py')  # первый аргумент - это имя файла
    zip_file.write('lse.jpeg', 'lse1.jpeg')         # второй аргумент - это имя файла в архиве
    print(zip_file.namelist())                      
```

cоздает в папке с программой архив с именем `archive.zip` и записывает в него содержимое файлов `program.py` и `lse.jpeg`, которые так же находятся в папке с программой, а затем выводит список всех файлов данного архива:

```no-highlight
['new_program.py', 'lse1.jpeg']
```

Для добавления файлов в уже существующий архив необходимо создать объект `ZipFile` в режиме `mode='a'`.
```python
from zipfile import ZipFile

with ZipFile('test.zip', mode='a') as zip_file:
    zip_file.write('program.py', 'test/program.py')
    zip_file.write('lse.jpeg')
    print(*zip_file.namelist(), sep='\n')
```
добавляет два новых файла `program.py` и `lse.jpeg` в уже существующий архив `test.zip` и выводит:
```no-highlight
test/
test/Картинки/
test/Картинки/1.jpg
test/Картинки/avatar.png
test/Картинки/certificate.png
test/Картинки/py.png
test/Картинки/World_Time_Zones_Map.png
test/Картинки/Снимок экрана.png
test/Неравенства.djvu
test/Программы/
test/Программы/image_util.py
test/Программы/sort.py
test/Разные файлы/
test/Разные файлы/astros.json
test/program.py
lse.jpeg
```
Обратите внимание на то, что файл `program.py` добавлен в папку `test`, в то время как файл `lse.jpeg` добавлен в корень архива.

## Извлечение содержимого zip-файла в каталог

Для извлечения данных из архива в каталог используются методы `extract()` и `extractall()`.

Если требуется извлечь отдельные файлы, то используется метод `extract()`, он принимает два аргумента: название файла и путь, по которому требуется извлечь файл. Если путь не указывать, то файл будет извлечен в папку, где находится файл с программой.
```python
from zipfile import ZipFile

with ZipFile('test.zip') as zip_file:
    zip_file.extract('test/Картинки/avatar.png')
    zip_file.extract('test/Программы/image_util.py')
    zip_file.extract('lse.jpeg')
```
извлекает файлы из обновленного архива `test.zip`.

Если требуется извлечь все содержимое архива, то используется метод `extractall()`, он принимает в качестве аргумента путь, по которому требуется извлечь все файлы. Если путь не указывать, то файл будет извлечен в папку, где находится файл с программой.
```python
from zipfile import ZipFile

with ZipFile('test.zip') as zip_file:
    zip_file.extractall()
```
извлекает все содержимое файла `test.zip` в папку, где находится файл с программой, при этом структура каталогов архива сохраняется.

## Примечания

1.** При создании объекта `ZipFile` мы также можем передать еще два необязательных аргумента:

- `compression`, который определяет метод сжатия, который должен использоваться при записи в архив. Он принимает одно из значений: `ZIP_STORED, ZIP_DEFLATED, ZIP_BZIP2, ZIP_LZMA`. По умолчанию используется значение `compression=ZIP_STORED`
    
- `allowZip64`, который позволяет разрешить использование расширений `zip64`, которые дают возможность создавать архивы размером больше 4 гигабайт. По умолчанию равен `allowZip64=True`
    

**2.** Для того чтобы проверить является ли некоторый файл `zip` архивом, используется функция `zipfile.is_zipfile()`, которая принимает на вход путь к файлу (или сам файловый объект) и возвращает значение `True`, если указанный файл является `zip` архивом, или `False` в противном случае.