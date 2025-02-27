выносим в отдельный элемент то что должно отрисовыватся всегда
Outlet это компонента в которой будет отрисовыватся все остально а вся остальная страница будет оставатся такая же без перезагрузки

```js
import { Link, Outlet } from "react-router-dom";
export const Layout = () => {
    return (
        <>
            <header>
                <Link to="/">Home</Link>
                <Link to="/blog">Blog</Link>
                <Link to="/about">About</Link>
            </header>
            <Outlet />
            <footer>2021</footer>
        </>
    );
};
```

далее импортируем эту страницу в App  и создаем еще одну обертку с path="/" и с сылкой на элемент который создали. В элементе Home path="/" меняем на index как бы говоря что это начальная страница.  В остальных путях можно убрать /  а можно оставить

```js
import { Route, Routes } from "react-router-dom";

import { About } from "./pages/AboutPage";
import { Blog } from "./pages/BlogPage";
import { Home } from "./pages/HomePage";
import { NotFound } from "./pages/NotFoundPage";
import { Layout } from "./components/Layout";  

function App() {
    return (
        <>
            <Routes>
                <Route path="/" element={<Layout />}>
                    <Route index element={<Home />} />
                    <Route path="blog" element={<Blog />} />
                    <Route path="about" element={<About />} />
                    <Route path="*" element={<NotFound />} />
                </Route>
            </Routes>
        </>
    );
}
export default App;
```