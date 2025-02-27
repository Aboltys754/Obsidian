
https://russianblogs.com/article/93331330430/
https://github.com/koajs/static

установка библиотеки
```js
	npm install koa-static
```

подключение библиотеки 
```js
const KoaStatic = require('koa-static');
```

Примерный код

```js
const Koa = require('koa');
const KoaStatic = require('koa-static');
const app = new Koa();  

app.use(KoaStatic('./src/html'));  

app.listen(3000);
```

В этот путь './src/html' помещают файлы сайта которые библиотека отдаст


```js
const Koa = require('koa');
const KoaStatic = require('koa-static');
const app = new Koa();  

app.use(async (ctx, next) => {
    if (ctx.method === 'GET') {
        await next();
        return;
    }
    console.log(ctx.method)
    console.log(ctx.request.url)
});  

app.use(KoaStatic('./src/html'));  

app.listen(3000);
```
