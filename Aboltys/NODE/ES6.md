
Для того что бы работали скрипты ES6 в NODE у файлы должно быть разрешение mjs
index.mjs

Либо в package.json должно быть прописано что мы используем ES6

для создания package.json можно использовать команду 
```
npm init -y
```

создастся такой файл
```
{
  "name": "02",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC"
}
```

Нужно добавить строчку  "type": "module",

```
{
  "name": "02",
  "version": "1.0.0",
  "description": "",
  "type": "module",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC"
}
```