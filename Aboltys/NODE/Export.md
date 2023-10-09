файл для экспорта имеет название handler.js


```
let i = 0;

function handler(req, res) {
	i++
	res.end(i)
}
```

чтобы отдельный файл был виден в другом файле в конце надо прописать

```
let i = 0;

function handler(req, res) {
	i++
	res.end(i)
}
module.exports = handler
```

при таком способе будет экспортироваться одна функция
и что бы ее экспортировать нужно прописать
```
const handler = require('./hendler')
```


Если в исходном файле несколько функция то можно их экспортировать как объект
для этого нужно экспортировать по другому
```
let i = 0;

function handler1(req, res) {
	i++
	res.end(i)
}

function handler2(req, res) {
	i++
	res.end(i)
}
exports.hendler = handler
```