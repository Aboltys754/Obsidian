файл для экспорта имеет название handler.js
Такой способ для ES6:

Если экспортировать одну функцию

```js
let i = 0;

function handler(req, res) {
	i++
	res.end(i)
}

export.default handler
```

Если несколько

```js
let i = 0;

function handler1(req, res) {
	i++
	res.end(i)
}

function handler2(req, res) {
	i++
	res.end(i)
}

export {handler1, handler2};
```

Соответственно импортировать нужно так:

Если экспортировать одну функцию

```js
import handler1 from './handler.js'
```

Для нескольких
```js
import {handler1, handler2} from './handler.js'
```



Такой способ для commonJS

```js
let i = 0;

function handler(req, res) {
	i++
	res.end(i)
}
```

чтобы отдельный файл был виден в другом файле в конце надо прописать

```js
let i = 0;

function handler(req, res) {
	i++
	res.end(i)
}
module.exports = handler
```

при таком способе будет экспортироваться одна функция
и что бы ее экспортировать нужно прописать
```js
const handler = require('./hendler')
```


Если в исходном файле несколько функция то можно их экспортировать как объект
для этого нужно экспортировать по другому
```js
let i = 0;

function handler1(req, res) {
	i++
	res.end(i)
}

function handler2(req, res) {
	i++
	res.end(i)
}
exports.hendler1 = handler
exports.hendler2 = handler
```
