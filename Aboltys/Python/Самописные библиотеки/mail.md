Нужна доработка. Не разобрался как отдельно сделать тему письма, поле от кого и поле кому


```python
def _send_email(self, mail_message: str) -> None:
        """send_email отправляет письмо о проблеме 
        Args:
            message (str): Получает Строку которую отправит в сообщении
        """
        try:
            smtp_object = smtplib.SMTP('mail.sps-holding.ru', 25)
            smtp_object.login('Почта отправителя', 'Логин от почты отправителя')
            smtp_object.sendmail('From: supportva@krasnoe-beloe.ru', 'To: supportva@krasnoe-beloe.ru', f'Subject: {mail_message} {self.name_systime}')
        except Exception as error:
            print(error)
        finally:
            smtp_object.quit()
```


```python
import smtplib  

# данные почтового сервиса

user = "foo@mail.ru"
passwd = "**********"
server = "smtp.mail.ru"

port = 25  

# тема письма
subject = "Тестовое письмо от Python."

# кому
to = "bar@mail.ru"

# кодировка письма
charset = 'Content-Type: text/plain; charset=utf-8'
mime = 'MIME-Version: 1.0'

# текст письма
text = "Отправкой почты управляет Python!"

  

# формируем тело письма
body = "\r\n".join((f"From: {user}", f"To: {to}",
       f"Subject: {subject}", mime, charset, "", text))  

try:
    # подключаемся к почтовому сервису
    smtp = smtplib.SMTP(server, port)
    smtp.starttls()
    smtp.ehlo()
    
    # логинимся на почтовом сервере
    smtp.login(user, passwd)

    # пробуем послать письмо
    smtp.sendmail(user, to, body.encode('utf-8'))

except smtplib.SMTPException as err:
    print('Что - то пошло не так...')
    raise err
finally:
    smtp.quit()
```