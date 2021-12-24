# test_spa

Таблица в формате Single Page Application.

Используемые технологии: Django, Bootstrap4, PostgreSQL

Файл .env должен лежать в корневой папке. В себе он содержит следующие данные:

* DB_ENGINE – используемая база данных 
* DB_NAME – имя 
* БД POSTGRES_USER – имя пользователя 
* POSTGRES_PASSWORD – пароль 
* DB_HOST=db 
* DB_PORT – порт 
* БД SECRET_KEY – секретный ключ Django 
* DEBUG – включен ли режим дебага в Django 
* ALLOWED_HOSTS – разрешённые хосты


Склонировать репозиторий: `git clone https://github.com/dayterr/test_spa.git`

Установить виртуальное окружение: `python3 -m venv venv`

Установить нужные библиотеки: `pip3 install -r requirements.txt`

Заполнить базу данных: `django-admin loaddata fixtures.json`

Запустить проект: `python3 spa/manage.py runserver`

Автор: Мария Дайтер – https://github.com/dayterr
