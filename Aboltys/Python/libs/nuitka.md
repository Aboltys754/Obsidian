https://nuitka.net/user-documentation/user-manual.html

иконка 
```python
python -m nuitka --onefile --windows-icon-from-ico=your-icon.png program.py
python -m nuitka --onefile --windows-icon-from-ico=your-icon.ico program.py
python -m nuitka --onefile --windows-icon-template-exe=your-icon.ico program.py
```
Окно консоли
```python
--disable-console
--enable-consoleproduct
```
имя продукта
```python
--product-name=foo
```
версия
```python
--windows-product-version=1.0.5.0
```
один файл
```python
--onefile
```