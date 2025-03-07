Логическое выражение после ключевого слова `WHERE` может включать операторы  **`BETWEEN`** и **`IN`**. Приоритет  у этих операторов такой же как у операторов сравнения, то есть они выполняются раньше, чем `**NOT**`, `**AND**,` `**OR**`.

Оператор `BETWEEN` позволяет отобрать данные, относящиеся к некоторому интервалу, включая его границы.

**Пример**

Выбрать названия и количества тех книг, количество которых от 5 до 14 включительно.

_Запрос:_
```sql
SELECT title, amount 
FROM book
WHERE amount BETWEEN 5 AND 14;
```

_Результат:_
```sql
+---------------+--------+
| title         | amount |
+---------------+--------+
| Белая гвардия | 5      |
| Идиот         | 10     |
+---------------+--------+
```

Этот запрос можно реализовать по-другому, результат будет точно такой же.

```sql
SELECT title, amount 
FROM book
WHERE amount >= 5 AND amount <=14;
```

Оператор  `IN`  позволяет выбрать данные, соответствующие значениям из списка.

**Пример**

Выбрать названия и цены книг, написанных Булгаковым или Достоевским.

_Запрос:_

```sql
SELECT title, price 
FROM book
WHERE author IN ('Булгаков М.А.', 'Достоевский Ф.М.');
```

_Результат:_
```sql
+--------------------+--------+
| title              | price  |
+--------------------+--------+
| Мастер и Маргарита | 670.99 |
| Белая гвардия      | 540.50 |
| Идиот              | 460.00 |
| Братья Карамазовы  | 799.01 |
+--------------------+--------+
```

Этот запрос можно реализовать по-другому, результат будет точно такой же.

```sql
SELECT title, price 
FROM book
WHERE author = 'Булгаков М.А.' OR author = 'Достоевский Ф.М.';
```
