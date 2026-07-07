
# Final Project QA Automation

Дипломный проект по автоматизации тестирования веб-приложения **Task Management System**.

Проект включает UI-тесты (Playwright + Page Object Model), API-тесты (Requests), логирование, отчёты Allure и проверку качества кода через Pylint в GitHub Actions.

## Технологии

- Python 3.13
- Playwright — UI-автоматизация
- Requests — API-тесты
- Pytest — фреймворк для тестов
- Faker — генерация тестовых данных
- Allure Report — визуальные отчёты
- Logging — логирование
- Pylint — проверка качества кода
- Page Object Model — архитектура тестов
- GitHub Actions — CI/CD

## Установка

​```bash
git clone https://github.com/temkin1982/final_project_qa_automation-lab.git
cd final_project_qa_automation-lab

python -m venv .venv
.venv\Scripts\activate

pip install -r requirements.txt
playwright install
​```

## Запуск приложения (Docker)

Перед запуском тестов необходимо запустить тестируемое приложение:

​```bash
docker-compose up --build
​```

После запуска приложение доступно по адресам:

- Веб-интерфейс: http://localhost:3000
- API: http://localhost:8000
- Документация API (Swagger): http://localhost:8000/docs

## Запуск тестов

Все тесты (UI и API):

​```bash
pytest
​```

Только API-тесты:

​```bash
pytest tests/test_api_users.py tests/test_api_tasks.py
​```

## Запуск с Allure-отчётом

​```bash
pytest --alluredir=allure-results
allure serve allure-results
​```

Отчёт откроется в браузере. В разделе **Behaviors** тесты сгруппированы по областям (UI Tests, API Tests) и модулям. Каждый тест содержит пошаговое описание.

## Проверка качества кода

​```bash
pylint api pages core tests data conftest.py utils
​```

Проект настроен на оценку 10/10. Настройки Pylint находятся в файле `.pylintrc`.

## Структура проекта

​```
final_project_qa_automation-lab/
├── api/                    # API-клиенты
│   ├── http_client.py      # базовый клиент (авторизация, запросы)
│   ├── users_api.py        # методы для работы с пользователями
│   └── tasks_api.py        # методы для работы с задачами
├── core/
│   └── base_page.py        # базовый класс BasePage
├── pages/                  # Page Object классы (UI)
│   ├── login_page.py
│   ├── home_page.py
│   ├── dashboard_page.py
│   ├── create_board_page.py
│   ├── register_page.py
│   └── subscription_page.py
├── tests/                  # тесты (UI и API)
├── data/                   # тестовые данные
├── utils/
│   └── logger.py           # настройка логирования
├── conftest.py             # фикстуры Pytest
├── pytest.ini              # настройки Pytest
├── .pylintrc               # настройки Pylint
├── requirements.txt        # зависимости
└── .github/workflows/      # CI/CD (GitHub Actions с Pylint)
​```

## Тестовое покрытие

Проект содержит 70 автотестов:

- **UI-тесты (55):** авторизация, главная страница, панель управления, создание досок, регистрация, оформление подписки (промокоды, оплата картами)
- **API-тесты (15):** работа с пользователями (получение, обновление, удаление) и задачами (создание, поиск, удаление)

В тестах применяются техники тест-дизайна: эквивалентные классы, граничные значения, позитивные и негативные сценарии, параметризация.

## Логирование

API-запросы логируются в файл `test_logs.log` и в консоль. Каждый запрос фиксирует успешное выполнение (INFO) или ошибку (ERROR).

## CI/CD

При каждом push и pull request в GitHub автоматически запускается проверка кода через Pylint (GitHub Actions). Конфигурация находится в `.github/workflows/pylint.yml`.