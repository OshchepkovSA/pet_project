# Книга рецептов на django с использованием Docker, база данных SQLite


## Использование Docker

### Сборка образов и запуск контейнеров

В корне репозитория выполните команду:

```bash
docker-compose up --build
```

При первом запуске данный процесс может занять несколько минут.

### Остановка контейнеров

Для остановки контейнеров выполните команду:

```bash
docker-compose stop
```
### Инициализация проекта

#### Применение миграций:

```bash
docker-compose exec web python manage.py migrate
```

#### Создание суперпользователя

```bash
docker-compose exec web python manage.py createsuperuser
```

#### Добавление фикстур

```bash
docker-compose exec web python manage.py loaddata book_recipes/fixtures/initial_data.json
```

Проект доступен по адресу http://0.0.0.0:8000
