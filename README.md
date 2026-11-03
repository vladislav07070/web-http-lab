
# web-http-lab

## Как запустить проект локально

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com
   cd web-http-lab
   ```

2. Создайте и активируйте виртуальное окружение:
   ```bash
   python -m venv .venv
   source .venv/Scripts/activate  # Для Git Bash
   ```

3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

4. Запустите сервер:
   ```bash
   uvicorn main:app --reload
   ```

Проверить работу можно по адресам `/hello` и `/docs`.
