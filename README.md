# payment_project

## Описание

Приложение для онлайн-покупок с использовнием Stripe API

### Технологии

Python 3.9 Django 2.2 Stripe API Docker

## Запуск проекта в dev-режиме

- Установите и активируйте виртуальное окружение
- Установите зависимости из файла requirements.txt

```bash
pip install -r requirements.txt
``` 

- В папке с файлом manage.py выполните команду:

```bash
python3 manage.py runserver
```

## Запуск проекта в Docker

Клонируем репозиторий и переходим в него в командной строке:

```bash
git clone https://github.com/afanasev-ilia/payment_project
```

```bash
cd payment_project
```

Запускаем docker-compose:

```bash
docker-compose up -d --build
```

Выполняем миграции:

```bash
docker-compose exec web python manage.py migrate
```

Создаем суперппользователя:

```bash
docker-compose exec web python manage.py createsuperuser
```

Собираем статику проекта:

```bash
docker-compose exec web python manage.py collectstatic --no-input
```

##### Шаблон наполнения .env

```
DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql
DB_NAME=postgres # имя базы данных
POSTGRES_USER=postgres # логин для подключения к базе данных
POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой)
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД 
```

## Автор

Афанасьев Илья
