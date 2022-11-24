https://stackoverflow.com/questions/30068298/git-fatal-could-not-read-from-remote-repository-please-make-sure-you-have-th


**Шаг 1: создайте две пары ключей ssh:**

```
ssh-keygen -t rsa -C "your_email@youremail.com"
```

**Шаг 2: здесь будет создано два ключа ssh:**

```
~/.ssh/id_rsa_account1
~/.ssh/id_rsa_account2
```

**Шаг 3: нужно зайти в agent
````
eval `ssh-agent -s`
````

**Шаг 4: теперь нам нужно добавить эти ключи:**

```
ssh-add ~/.ssh/id_rsa_account2
ssh-add ~/.ssh/id_rsa_account1
```

-   Вы можете просмотреть список добавленных ключей, используя эту команду: `ssh-add -l`
-   Вы можете удалить старые кэшированные ключи с помощью этой команды: `ssh-add -D`

**Шаг 5: измените конфигурацию ssh**

```
cd ~/.ssh/
touch config
```
`subl -a config` или `code config`или `nano config`

**Шаг 6: добавьте это в файл конфигурации:**

```
#Github account1
Host github.com-account1
    HostName github.com
    User account1
    IdentityFile ~/.ssh/id_rsa_account1

#Github account2
Host github.com-account2
    HostName github.com
    User account2
    IdentityFile ~/.ssh/id_rsa_account2
```

**Шаг 7 обновите свой `.git/config`файл:**

_Шаг-7.1: перейдите к проекту account1 и обновите узел:_

```
[remote "origin"]
        url = git@github.com-account1:account1/gfs.git
```

Если вас пригласил какой-либо другой пользователь в их репозиторий git. Затем вам нужно обновить хост следующим образом:

```
[remote "origin"]
            url = git@github.com-account1:invitedByUserName/gfs.git
```

_Шаг-7.2: перейдите к проекту account2 и обновите узел:_

```
[remote "origin"]
        url = git@github.com-account2:account2/gfs.git
```

**Шаг 8: обновите имя пользователя и адрес электронной почты для каждого репозитория отдельно, если требуется, это не корректирующий шаг:**

Перейдите к проекту account1 и запустите эти:

```
git config user.name "account1"
git config user.email "account1@domain.com" 
```

Перейдите к проекту account2 и запустите эти:

```
git config user.name "account2"
git config user.email "acccount2@doamin.com" 
```