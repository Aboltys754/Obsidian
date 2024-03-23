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