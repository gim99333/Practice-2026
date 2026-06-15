#Развертывание django-проекта на локальном ресурсе
*Выполняется после копирования из репозитория папки case3*

1. Установка Django:
`pip install django`

2. Создание проекта ##greetings_project##
``django-admin startproject greetings_project``

3. Создание приложения greetings в проекте:
`cd greetings_project`
`python manage.py startapp greetings`

4. Миграция БД:
`python manage.py makemigrations`
`python manage.py migrate`

5. Создание суперюзера БД _(задать имя, пароль и т.д. при вводе)_:
`python manage.py createsuperuser`

6. Запуск http-сервера django:
`python manage.py runserver` 

Откройте в браузере главную страницу: <http://127.0.0.1:8000/>