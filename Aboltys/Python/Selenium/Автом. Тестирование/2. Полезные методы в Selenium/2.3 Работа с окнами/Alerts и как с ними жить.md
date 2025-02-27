 **Alert** является модальным окном: это означает, что пользователь не может взаимодействовать дальше с интерфейсом, пока не закроет alert. Для этого нужно сначала переключиться на окно с alert, а затем принять его с помощью команды **accept()**
```python
alert = browser.switch_to.alert
alert_text = alert.text
alert.accept()
```
Другой вариант модального окна, который предлагает пользователю выбор согласиться с сообщением или отказаться от него, называется **confirm**. Для переключения на окно confirm используется та же команда, что и в случае с alert
```python
confirm = browser.switch_to.alert 
confirm.accept() # Принять
confirm.dismiss() # Отказ
```
Третий вариант модального окна — **prompt** — имеет дополнительное поле для ввода текста. Чтобы ввести текст, используйте метод **send_keys()**
```python
prompt = browser.switch_to.alert 
prompt.send_keys("My answer") 
prompt.accept()
```
