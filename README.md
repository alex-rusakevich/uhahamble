Uhahamble Bot
===

![Python version](https://badgen.net/badge/python/v3.12/blue)
![Python version](https://badgen.net/badge/redis/v7/red)

Бот с русскими анекдотами, собирающий лучшее с Рунета

## Разработчику

Требования для запуска:

* Python **3.12** и новее
* Poetry
* Redis (если установлен `NO_CACHE=1` в .env)

Токен должен быть установлен в .env как `BOT_TOKEN`

Установка зависимостей:

```sh
poetry install
```

Запуск:

```sh
poetry run inv dev
```
