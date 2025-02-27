Когда вам нужно работать с высокоуровневыми файловыми операциями, такими как копирование содержимого файла, создание новой копии файла и ее архивирование, вам подойдет модуль shutil в Python.  

```python
# скопировать файл в новый файл только в текущем каталоге.
import os 
import shutil 
print('BEFORE:', os.listdir('.')) 
shutil.copyfile('file_copy.py', 'file_copy.py.copy')
print('AFTER:', os.listdir('.'))
```

```python
# скопировать файл в другой каталог
import os 
import shutil 
os.mkdir('journaldev') 
print('BEFORE:', os.listdir('journaldev')) 
shutil.copy('file_copy.py', 'journaldev') 
print('AFTER:', os.listdir('journaldev'))  
```
Эта функция отличается от функции copyfile(), поскольку последняя принимает имя файла в качестве параметра, тогда как функция copy() принимает имя каталога в качестве входных данных.  
Наконец, разрешения файла также клонируются при копировании файла с обеими функциями, но метаданные не копируются, что означает, что новый созданный файл будет иметь время только что созданного вместо времени исходного файла.  

```python
# Если вам нужно сделать точный клон файла вместе с разрешениями и метаданными файла  

import os 
import shutil 
import time 

def file_metadata(file_name): 
	# получает статистическую информацию файла или дескриптора файла
	stat_info = os.stat(file_name) 
	print(' Mode :', oct(stat_info.st_mode)) 
	print(' Created :', time.ctime(stat_info.st_ctime)) 
	print(' Accessed:', time.ctime(stat_info.st_atime)) 
	print(' Modified:', time.ctime(stat_info.st_mtime))
	os.mkdir('journaldev') 
	print('SOURCE FILE:') 
	file_metadata('file_copy.py') 
	shutil.copy2('file_copy.py', 'journaldev') 
	print('DESTINATION FILE:') 
	file_metadata('journaldev/file_copy.py')  
```

```python
# полностью рекурсивно реплицировать дерево каталогов  

import pprint 
import shutil 
import os 
shutil.copytree('../shutil', './journaldev') 
print('\nAFTER:') 
pprint.pprint(os.listdir('./journaldev'))  
```


```python
# удаление всего каталога  

import pprint 
import shutil 
import os 
print('BEFORE:') 
pprint.pprint(os.listdir('.')) 
shutil.rmtree('journaldev') 
print('\nAFTER:') 
pprint.pprint(os.listdir('.'))  
```
```python
# для поиска файла на вашем компьютере, который присутствует в PATH 

import shutil 
print(shutil.which('bsondump')) 
print(shutil.which('no-such-program'))  
```


```python
# получить информацию о том, сколько данных присутствует в нашей файловой системе 

import shutil 
total_b, used_b, free_b = shutil.disk_usage('.') 
gb = 10 ** 9 
print('Total: {:6.2f} GB'.format(total_b / gb)) 
print('Used : {:6.2f} GB'.format(used_b / gb)) 
print('Free : {:6.2f} GB'.format(free_b / gb))  
```
