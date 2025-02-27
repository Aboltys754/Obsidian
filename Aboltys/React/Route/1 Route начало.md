
Для установки Router набираем 
```js
npm i react-router-dom
```

импортируем  BrowserRouter в основную компоненту и обворачиваем начальный тег с которого начинается приложение

```js
import {BrowserRouter} from 'react-router-dom'

<React.StrictMode>
	<BrowserRouter>
		<App />
	</BrowserRouter>
</React.StrictMode>
```

В App  экспортируем Link, Routes и Route из react-router-dom

```js
import {Link, Routes, Route} from 'react-router-dom'
```

Далее в App создаем корневой элемент Routes а в нем елемент Route в котором указываем path это откуда у нас все адреса ссылок будут начинатся и element это корневая страница

```js
<Routes>
	<Route path="/" element={<Homepage />} />
</Routes>
```

Так же если в path указать * это будет значить путь который не нашелся. например если страницы нет то будет отбражатся какая то спецмально созданая страница NotFound

```js
<Route path="*" element={<NotFound />} />

если страница не найдется то выйдет компонента NotFound
export const NotFound = () => {
    return (
        <div>
            This page doesn't exist. Go <a href="/">Home</a>
        </div>
    );
};
```

Примерная страница App

```js
import { Route, Routes, Link } from "react-router-dom";  

import { About } from "./pages/AboutPage";
import { Blog } from "./pages/BlogPage";
import { Home } from "./pages/HomePage";
import { NotFound } from "./pages/NotFoundPage";  

function App() {
    return (
        <>
            <header>
                <Link to="/">Home</Link>
                <Link to="/blog">Blog</Link>
                <Link to="/about">About</Link>
            </header>
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/blog" element={<Blog />} />
                <Route path="/about" element={<About />} />
                <Route path="*" element={<NotFound />} />
            </Routes>
        </>
    );
}
export default App;
```