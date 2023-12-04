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
docker-compose exec payment_project python manage.py migrate
```

Создаем суперппользователя:

```bash
docker-compose exec payment_project python manage.py createsuperuser
```

##### Шаблон наполнения .env

```
SECRET_KEY = '**************************************************'
STRIPE_PUBLIC_KEY = 'pk_test_***********************************'
STRIPE_SECRET_KEY = 'sk_test_***********************************'
STRIPE_WEBHOOK_SECRET = '************'

## Автор

Афанасьев Илья
