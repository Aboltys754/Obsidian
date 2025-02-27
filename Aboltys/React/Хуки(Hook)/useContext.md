https://webtricks-master.ru/react-hooks/uchim-usecontext-na-primerah/


Context в React это способность передачи данных через дерево компонентов, минуя прокидывание данных через пропсы от одного компонента к другому.

Для создания контекста достаточно воспользоваться методом React.createContext, он имеет единственный параметр, в который можно передать дефолтное значение или объект для получения дочерних компонентов через контекст.

```js
const context = React.createContext('value');
```

Пример (App.js):

```js
import React, { useState } from "react";
import { Context } from "./Context.js";

import ComponentA from "./ComponentA";
import ComponentB from "./ComponentB";

export default function App() {
  const [context, setContext] = useState("default context value");
  return (
    <Context.Provider value={[context, setContext]}>
      <ComponentA />
      <ComponentB />
    </Context.Provider>
  );
}
```

Пример (Context.js):

```js

import React from "react";
export const Context = React.createContext();
```

Пример (ComponentA.js):

```js

import React, { useContext } from "react";
import { Context } from "./Context";

export default function ComponentA() {
  const [context, setContext] = useContext(Context);
  return (
    <div>
      ComponentA:
      <button onClick={() => setContext("New Value")}>
        Change Context Value
      </button>
    </div>
  );
}
```

Пример (ComponentB.js):

```js

import React, { useContext } from "react";
import { Context } from "./Context";

export default function ComponentB() {
  const [context, setContext] = useContext(Context);
  return <div>ComponentB: {context}</div>;
}
```


В Context.js создается сам контекст, а в App.js импортируются два компонента и контекст, которым они оборачиваются, c передачей в value начального состояния (context) и функции для его изменения (setContext).

Два дочерних компонента импортируют в себя контекст, используя хук useContext  и посредством деструктуризации вытаскивается значение и функция для ее изменения.

При нажатии на кнопку в компоненте ComponentA происходит изменение значения контекста, благодаря useContext в компоненте ComponentB происходит его моментальное перерендеривание и, как результат в нем отображается значение контекста.