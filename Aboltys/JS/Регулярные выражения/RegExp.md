https://learn.javascript.ru/regexp-introduction  ссылка на статью по регулярке

есть 2 метода создания регулярных выражения:
	1.. Длинный 
	regexp = new RegExp("шаблон", "флаги");
	позволяет создавать динамические выражения
	`let regexp = new RegExp(`<${tag}>`); // то же, что /<h2>/ при ответе "h2" на prompt выше`