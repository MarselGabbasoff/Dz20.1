1. Откройте .env и замените значения переменных на свои собственные
cp .env.example .env
2. Проект использует Poetry для управления зависимостями. Убедитесь, что Poetry установлен, затем выполните следующую команду, чтобы установить все зависимости:
poetry shell
poetry install
3. Чтобы начать миграцию, используйте следующую команду:
python3 manage.py migrate
4. Загрузка тестовых фикстур для базы данных:
python3 manage.py load_fixtures
5. Для запуска сервера используйте следующую команду:
python3 manage.py runserver
6. Сервер будет доступен по адресу http://127.0.0.1:8000
