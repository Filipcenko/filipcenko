# Task Manager

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone <URL вашего репозитория>
   cd task_manager
   ```

2. Создайте и активируйте виртуальное окружение:
   ```bash
   python -m venv venv
   source venv/bin/activate  # для Linux и macOS
   venv\Scripts\activate  # для Windows
   ```

3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

4. Примените миграции базы данных:
   ```bash
   python manage.py migrate
   ```

5. Создайте суперпользователя:
   ```bash
   python manage.py createsuperuser
   ```

6. Запустите сервер разработки:
   ```bash
   python manage.py runserver
   ```

7. Откройте браузер и перейдите по адресу `http://127.0.0.1:8000` для доступа к проекту.

## API Эндпоинты

- **Получение JWT токена:**
  - Метод: POST
  - URL: `http://127.0.0.1:8000/api/token/`
  - Тело запроса:
    ```json
    {
        "username": "<username>",
        "password": "<password>"
    }
    ```

- **Обновление JWT токена:**
  - Метод: POST
  - URL: `http://127.0.0.1:8000/api/token/refresh/`
  - Тело запроса:
    ```json
    {
        "refresh": "<refresh_token>"
    }
    ```

- **Список задач:**
  - Метод: GET
  - URL: `http://127.0.0.1:8000/api/tasks/`
  - Заголовок запроса: `Authorization: Bearer <access_token>`

