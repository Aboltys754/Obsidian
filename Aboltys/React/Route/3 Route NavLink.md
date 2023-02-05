Для выделения активной ссылки в меню React-Router предлагает отдельный компонент NavLink, у которого особые возможности работы с атрибутами className и style. Кроме того, есть возможность создать собственный компонент, скрыв в нем всю стилизацию активного состояния ссылки

Меняем в Layout тег Link На NavLink
```js
import { NavLink, Outlet } from "react-router-dom";  

export const Layout = () => {
    return (
        <>
            <header>
                <NavLink to="/">Home</NavLink>
                <NavLink to="/blog">Blog</NavLink>
                <NavLink to="/about">About</NavLink>
            </header>
            <Outlet />
            <footer>2021</footer>
        </>
    );
};
```

и в css прописываем селектор active

```css
.active {
  color: red;
  cursor: default;
}
```

и выделеная ссылка будет менять цвет на красный. все дело в том что NavLink автаматически прописывает класс active той ссылке на которую нажали
![[Pasted image 20230205103840.png]]

Если Мы хотим сами создать свой className то можно ввести проверку активной ссылки в NavLink
```js
import { NavLink, Outlet } from "react-router-dom"; 

export const Layout = () => {
    const setActive = ({ isActive }) => (isActive ? "active-link" : "");
    return (
        <>
            <header>
                <NavLink to="/" className={setActive}>
                    Home
                </NavLink>
                <NavLink to="/blog" className={setActive}>
                    Blog
                </NavLink>
                <NavLink to="/about" className={setActive}>
                    About
                </NavLink>
            </header>
            <Outlet />
            <footer>2021</footer>
        </>
    );
};
```
параметр {isActive}  указывает какая ссылка в данный момент активна

Можно вообще создать свой полностью компонент который будет отображать все действия с активной ссылкой. Для этого создадим свой компонент CustomLink

```js
import { Link, useMatch } from "react-router-dom";  

export const CustomLink = ({ children, to, ...props }) => {
    const match = useMatch(to);
    console.log(match);
    return (
        <Link
            to={to}
            {...props}
            style={{
                color: match ? "green" : "blue",
            }}
        >
            {children}
        </Link>
    );
};
```

Он будет принимать параметр {to} путь ссылки {children} то что надо будет отобразить  и можно еще какие нибудь параметры {...props}.
Что бы определить активность ссылки будем использовать хук useMatch он может принимать строку. в данном случае передаем ему путь.  и если ссылка активна то в ответ получим объект если нет null. и в зависимости от то го что получаем задействуем стили

```js
import { Outlet } from "react-router-dom";
import { CustomLink } from "./CustomLink";  

export const Layout = () => {
    return (
        <>
            <header>
                <CustomLink to="/">Home</CustomLink>
                <CustomLink to="/blog">Blog</CustomLink>
                <CustomLink to="/about">About</CustomLink>
            </header>
            <Outlet />
            <footer>2021</footer>
        </>
    );
};
```
Далее маняем NavLink на наш кастомный CustomLink
