
```
хук который меняет состояние
const[state, setState] = useState();

useEffect отслежывает состояние state и при его изменении запускает функцию
useEffect(() => {}, [state]);
```

--Если поместить несколько state и тогда useEffect будет срабатывать на изменение любого из них.

```
const[state, setState] = useState();
const[state2, setState2] = useState();

useEffect(() => {
	console.log(1)
}, [state, state2]);
```

--Если в функции в return указа функцию то она будет выполняться при разрушении компонента
```
const[state, setState] = useState();

useEffect(() => {
	console.log("привет")
	return console.log("Пока")
}, [state]);
```
--Если не указать ни чего то функция сработает один раз при создании компонента

```
useEffect(() => {
	console.log("привет")
}, []);
```