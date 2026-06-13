
# Final project qA automation

Дипломный проект по автоматизации тестирования сайта Task Management System.

## Технологии

- Python 3.13
- Playwright
- Pytest
- Allure Report
- Page Object Model

## Установка

git clone https://github.com/temkin1982/final_project_qa_automation-lab.git
cd final_project_qa_automation-lab

python -m venv .venv
.venv\Scripts\activate

pip install -r requirements.txt
playwright install

## Запуск тестов

pytest

## Запуск с Allure отчетом

pytest --alluredir=allure-results
allure serve allure-results

## Структура проекта

pages - Page Object классы
tests - тесты
data - тестовые данные
conftest.py - фикстуры
pytest.ini - настройки pytest