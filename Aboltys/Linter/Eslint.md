[http://31.129.109.120/%D0%9B%D0%B8%D0%BD%D1%82%D0%B5%D1%80](http://31.129.109.120/%D0%9B%D0%B8%D0%BD%D1%82%D0%B5%D1%80)

# Линтер

### Установка

1. установить пакет `eslint`
2. создать файл конфигурации командой

```
bash
npm init @eslint/config
```

3. установить конфигурацию для ESlint. Например, [конфигурация airbnb](https://www.npmjs.com/package/eslint-config-airbnb-base) устанавливается так:

```

npx install-peerdeps --dev eslint-config-airbnb-base
```

Затем в конфигурационном файле .eslinrc.js надо указать эту конфигу:

```

module.exports = {
	...
    "extends": "airbnb-base",
	...
}
```

### Использование

В файле package.json:

```
json
{
	...
  "scripts": {
    "lint": "eslint .",
    "lint:fix": "eslint . --fix"
  },
  	...
}
```

Запускается линтер командой

```

//для конкретного файла
npx eslint directory/file_name

//для проверки всего проекта (надо прописать запуск скрипта в pakcage.json)
npm run lint
```

Для корректной работы линтера нужен конфигурационный файл (.eslintrc.js). Примерно такой:

```

module.exports = {
  env: {
    node: true,
  },

  extends: [
    'airbnb',
  ],

  parserOptions: {
    ecmaVersion: 12,
    sourceType: 'module',
  },

  rules: {
    'no-underscore-dangle': 'off',
    'no-use-before-define': 'off',
    'no-param-reassign': 'off',
  },

  ignorePatterns: ['*.test.js'],
};
```

[Подробнее про eslint](https://eslint.org/docs/)

### [eslint with TypeScript](http://31.129.109.120/eslint%20with%20TypeScript)

[Подробнее про eslintrc](https://eslint.org/docs/latest/user-guide/configuring/configuration-files)

[eslint и tslint](https://khalilstemmler.com/blogs/typescript/eslint-for-typescript/)