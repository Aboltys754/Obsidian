Сначала инициализируйте два репозитория:
```bash
git init A
git init B
```
![](https://ucarecdn.com/cb549d8b-04c4-406a-98ec-d5280aff2564/)

Добавьте удаленный адрес в репозиторий A:
```bash
cd A
git remote add origin *address*
```

![](https://ucarecdn.com/85faa82d-aa84-4c9f-a67b-dabe711c4062/)

Следующий шаг - перенести все изменения из центрального репозитория в локальный репозиторий.

```bash
git pull origin master
```

![](https://ucarecdn.com/31df568b-3dc4-4589-b11b-b9450beb8517/)

Выполните тот же процесс, чтобы добавить источник в репозиторий B.

```bash
git remote add origin *address*
```

![](https://ucarecdn.com/c4db99bd-bf5d-4250-9952-486855c60669/)

Команда `pull` выполняется снова, чтобы извлечь все содержимое из удаленного репозитория и переместить его в локальный репозиторий.

```bash
git pull origin master
```

![](https://ucarecdn.com/d5164129-bd6c-4522-8dcc-6a5978bb29db/)

Оба этих репозитория представляют собой два разных репозитория двух разных разработчиков.

Давайте вернемся к репозиторию A.

```
cd ../A
```

![](https://ucarecdn.com/df42994b-36e8-4934-9a15-8cc0315d78ed/)

В репозитории A открывается файл readme для внесения различных изменений.

```bash
vi README.md
```

Внесите необходимые изменения в файл, а затем сохраните его. Затем выполните команду `git status`, чтобы увидеть отраженные изменения.

```
git status
```

![](https://ucarecdn.com/5198f57a-1ab1-463d-bd71-9073b40d3c74/)

Следующий шаг - добавить эти изменения и зафиксировать их.

```
git add.
git commit -m *commit message*
```

![](https://ucarecdn.com/38b9cafa-cc3c-42b4-aa1e-031f9497edf9/)

После завершения фиксации измененный файл отправляется в удаленный репозиторий.

```
git push origin master
```

Теперь вернитесь в репозиторий B.

```
cd B
```

![](https://ucarecdn.com/bfa645bf-d872-46f7-923c-bd21a9783699/)

Откройте файл readme:

```
vi README.md
```

![](https://ucarecdn.com/ff2f274f-4754-45ed-ae79-e588cde65d95/)

Внесите изменения в файл, сохраните его и закройте. После этого добавьте измененный файл и зафиксируйте его.

```
git add.
git commit -m *commit message*
```

![](https://ucarecdn.com/37040379-8d20-483d-b7fa-e083ef67843a/)

Следующий шаг - отправить файл в удаленный репозиторий.

```
git push
```

![](https://ucarecdn.com/b840313a-a348-48c0-8d18-cb0bc2972e08/)

Отображается сообщение об ошибке, означающее, что обновления отклонены.

Далее нам нужно выполнить:

```
git -- rebase origin master
```

![](https://ucarecdn.com/2cd476bb-028b-4fa0-a7ed-36b44e51f3a8/)

В настоящее время существуют видимые конфликты, которые необходимо разрешить вручную. Если вы хотите пропустить этот коммит, вы можете ввести `git rebase --skip`, или если вы хотите прервать эту перебазировку, вы можете ввести `git rebase --abort`.

После управления этим конфликтом вручную мы откроем инструмент слияния.

```
git mergetool
```

![](https://ucarecdn.com/b6fcfc49-552f-4352-8c94-1233f0fee441/)

После того, как мы введем эту команду, все файлы будут обработаны.

![](https://ucarecdn.com/dd5b861b-0af9-42ae-993d-5300cc997a35/)

Это все процессы и изменения, выполненные в файле. Вы можете увидеть там три разных файла, и все, что было добавлено или удалено. После прокрутки вы можете проверить, где именно произошел конфликт.

![](https://ucarecdn.com/76e020b6-8093-47fc-bc81-b4a40bf39f80/)

Затем вы можете решить, хотите ли вы продолжить работу с этим конкретным файлом или нет. В данном случае мы продолжим удалять эту строку.

![](https://ucarecdn.com/46c66e13-73da-4a93-9844-ee7316d2c7fe/)

Ручные модификации позволили нам разрешить конфликты файлов. Сохраните файл и закройте окончательный файл.

![](https://ucarecdn.com/65afa3eb-60a4-4181-9c54-4d0e67021225/)

Далее мы запустим:

```
git rebase --continue
```

![](https://ucarecdn.com/02fe479b-6b1e-44fa-97d2-9473f74f82ef/)

Теперь, когда конфликт разрешен, мы должны иметь возможность отправить файл в удаленный репозиторий.

![](https://ucarecdn.com/8d0700f4-6933-4307-b3a3-db05bd7408bc/)

Теперь вы можете проверить коммиты в вашем удаленном репозитории.

![](https://ucarecdn.com/6411dec7-b8ae-40aa-8884-517339d8cbee/)