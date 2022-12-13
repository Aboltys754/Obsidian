https://ru.react.js.org/docs/hooks-reference.html#usestate

Хук для изменения состояния компонента.
вот пример написания хука useState
```
const[state, setState] = useSate(initialState);
```

В useState( "указывается начальное состояние" ) то что получит компонент когда он создастся.
это может быть приметив., объект, массив и т.д. Так же это может быть функция которая вычислит начальное состояние

```js
const [state, setState] = useState(() => {
  const initialState = someExpensiveComputation(props);
  return initialState;
});
```

state это значение в данный момент. при создании state и useState имеют одно и тоже значение

setState это метод с помощью которого меняется состояние

```js
const [count, setCount] = useState(initialCount);
  return (
    <>
      <button onClick={() => setCount(count + 1)}>+</button>
      <button onClick={() => setCount(count - 1)}>-</button>
    </>
  );
```

При изменении состояния происходит рендеринг компонента

