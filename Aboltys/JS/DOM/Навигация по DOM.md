## [Сверху: documentElement и body](https://learn.javascript.ru/dom-navigation#sverhu-documentelement-i-body)

Самые верхние элементы дерева доступны как свойства объекта `document`:
`<html>` = `document.documentElement`

Самый верхний узел документа: `document.documentElement`. В DOM он соответствует тегу `<html>`.
`<body>` = `document.body`

Другой часто используемый DOM-узел – узел тега `<body>`: `document.body`.
`<head>` = `document.head`


-   **Дочерние узлы (или дети)** – элементы, которые являются непосредственными детьми узла. Другими словами, элементы, которые лежат непосредственно внутри данного. Например, `<head>` и `<body>` являются детьми элемента `<html>`.
-   **Потомки** – все элементы, которые лежат внутри данного, включая детей, их детей и т.д.
- _Соседи_ – это узлы, у которых один и тот же родитель.

**Свойства `firstChild` и `lastChild` обеспечивают быстрый доступ к первому и последнему дочернему элементу.**

Они, по сути, являются всего лишь сокращениями. Если у тега есть дочерние узлы, условие ниже всегда верно:

`elem.childNodes[0] === elem.firstChild elem.childNodes[elem.childNodes.length - 1] === elem.lastChild`

Для проверки наличия дочерних узлов существует также специальная функция `elem.hasChildNodes()`.

Родитель доступен через `parentNode`
Следующий узел того же родителя (следующий сосед) – в свойстве `nextSibling` 
А предыдущий – в `previousSibling`.

Навигация только по элементам

![[Pasted image 20230323114316.png]]

-   `children` – коллекция детей, которые являются элементами.
-   `firstElementChild`, `lastElementChild` – первый и последний дочерний элемент.
-   `previousElementSibling`, `nextElementSibling` – соседи-элементы.
-   `parentElement` – родитель-элемент.