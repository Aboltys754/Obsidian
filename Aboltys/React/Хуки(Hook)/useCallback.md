 https://reactjs.org/docs/hooks-reference.html#usecallback


```js
const onRemoveProduct useCallback(() => dispatch(removeProduct(productId)), [зависимость]) 
```

когда меняются зависимости пересаздается ссылка и произойдет перерендер. если ни чего не написать в зависимости то ссылка создастся один раз и до конца жизненного цикла

```js
const memoizedCallback = useCallback(
  () => {
    doSomething(a, b);
  },
  [a, b],
);
```

useCallback используется тогда когда этот Callback прокидываются в какой то компонент