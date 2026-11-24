# Notes API (`web-http-lab`)

Учебный REST API сервис для управления заметками на базе FastAPI.

## Как запустить проект локально

1. Клонируйте репозиторий и перейдите в папку проекта:
   ```bash
   git clone https://github.com
   cd web-http-lab
   ```

2. Создайте и активируйте виртуальное окружение:
   ```bash
   python -m venv .venv
   # Для Windows (PowerShell):
   .venv\Scripts\Activate.ps1
   # Для Git Bash / Linux / macOS:
   source .venv/Scripts/activate
   ```

3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

4. Запустите сервер:
   ```bash
   uvicorn main:app --reload
   ```

После запуска интерактивная документация Swagger UI доступна по адресу: **http://127.0.0.1:8000/docs**

---

## Список Endpoints

* `GET /` — главная страница (приветственное сообщение)
* `GET /hello` — приветствие от Notes API
* `GET /health` — проверка работоспособности сервиса
* `GET /notes` — получение списка всех заметок
* `POST /notes` — создание новой заметки
* `GET /notes/{note_id}` — получение конкретной заметки по `id`

---

## Примеры Request / Response

### 1. Создание заметки (`POST /notes`)

**Request:**
```json
{
  "title": "Купить продукты",
  "content": "Молоко, хлеб, яйца"
}
```

**Response (`201 Created`):**
```json
{
  "id": 1,
  "title": "Купить продукты",
  "content": "Молоко, хлеб, яйца"
}
```

### 2. Получение списка заметок (`GET /notes`)

**Response (`200 OK`):**
```json
[
  {
    "id": 1,
    "title": "Купить продукты",
    "content": "Молоко, хлеб, яйца"
  }
]
```

### 3. Получение заметки по ID (`GET /notes/1`)

**Response (`200 OK`):**
```json
{
  "id": 1,
  "title": "Купить продукты",
  "content": "Молоко, хлеб, яйца"
}
```

**Если заметка не найдена (`GET /notes/999` — `404 Not Found`):**
```json
{
  "detail": "Note not found"
}
```

---

## Ограничения

* **Хранение в памяти (in-memory):** все заметки хранятся в списке в оперативной памяти сервера. После перезапуска приложения все созданные данные исчезают.
