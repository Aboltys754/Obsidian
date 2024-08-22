Рассмотрим ветвление на примере.

Создайте "тестовый" репозиторий в локальной системе.

```
mkdir git_test
```

Перейдите в тестовый репозиторий.

```
cd git_test
```

 Создайте новый экземпляр git для проекта.

```
git init
```

![](https://ucarecdn.com/1a92136b-6bac-4ccf-a664-b9673793dc09/)

Создайте текстовый файл с именем `info.txt` в папке `git_test`. Напишите что-нибудь и сохраните это.

```
touch info.txt
notepad info.txt
```

![](https://ucarecdn.com/97bd6beb-9635-44cd-ae51-897d7bd9c1d0/)

Проверьте состояние репозитория.

```
git status
```

![](https://ucarecdn.com/a8eeb1b3-d36d-4aca-95cd-47e88ab29e7e/)

Добавьте файл, который вы создали для выполнения коммита. 

```
git add .
```

Внесите эти изменения в историю репозитория с помощью короткого сообщения.

```
git commit -m "commiting a text file"
```

![](https://ucarecdn.com/57f2c816-1dd8-400d-8e3c-7b00709fb4e7/)

Внесите все необходимые изменения в файл и сохраните.

![](https://ucarecdn.com/3149cbbd-4c85-47ad-86ff-00d1967bcbfd/)

Теперь, когда вы внесли изменения в файл, вы можете сравнить различия с момента вашего последнего коммита.

![](https://ucarecdn.com/aa05879e-2bff-49d3-a1df-45745791bf99/)

Добавьте имя пользователя на GitHub в конфигурацию Git.

```
git config --global user.username Olesya100
```

![](https://ucarecdn.com/f752e293-83ed-4a73-a2ec-d81f2d14598c/)

Создайте удаленный репозиторий на GitHub.

![](https://ucarecdn.com/94bf5cbc-e6aa-4a3b-92db-16f8d0929197/)

Подключите локальный репозиторий к вашему удаленному репозиторию.

```
git remote add origin https://github.com/Olesya100/git_test.git
```

Отправьте файл в удаленный репозиторий.

```
git push origin master
```

![](https://ucarecdn.com/4e8bebce-9517-403b-8fd5-99389c079c83/)

Обновите страницу своего репозитория на GitHub. Вы получите свой локальный файл в удаленном репозитории GitHub.

![](https://ucarecdn.com/2aac4cee-b26b-49c7-aef9-be90cbe087e3/)

Создайте еще три текстовых файла в локальном репозитории - `info1.txt`, `info2.txt`, `info3.txt`.

![](https://ucarecdn.com/8f450691-6871-47d2-b556-a5152d4b9b05/)

Создайте ветвь `first_branch` и объедините ее с основной (master) ветвью.

```
git branch first_branch
```

 Приведенная выше команда создает ветвь.

```
git checkout first_branch
```

![](https://ucarecdn.com/f29c1207-04c2-4127-bb7b-b0543621b5d2/)

Приведенная выше команда переключается на новую ветвь из главной ветви.

Создадим и добавим `info3.txt` к `first_branch`.

```
git add info3.txt
```

![](https://ucarecdn.com/dfebdca4-a055-48d6-82a1-b49325404bd4/)

Создайте ветвь `first_branch` и объедините ее с основной (master) ветвью.

```
git commit -m "make some changes to first brach"
```

![](https://ucarecdn.com/770a6175-dc9d-4b7d-ac1b-10635f142595/)

Приведенная выше команда выполняет фиксацию в `first_branch`.

![](https://ucarecdn.com/7535dd79-090a-4d60-a559-2ffdb62e26e8/)

Приведенная выше команда показывает, что новая ветвь имеет доступ ко всем файлам.

```
git branch first_branch
```

![](https://ucarecdn.com/b010b276-b421-4a75-93fe-732bf2a659af/)

Приведенная команда показывает, что у главной ветви нет файла `info3.txt`.

Объединим `first_branch` с главной ветвью. Теперь главная ветвь содержит файл `info3.txt`.

![](https://ucarecdn.com/5e8c8a7a-b1f6-45b2-a513-6bb26ee3d085/)