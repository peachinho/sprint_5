# Sprint_5
Для заполенения README, а так же в рамках помощи и подсказок при выполнении проекта был использован ИИ


Автотесты UI для сервиса объявлений
`https://qa-desk.education-services.ru/`. Проект покрывает регистрацию,
авторизацию, выход из аккаунта и создание объявлений авторизованным и
неавторизованным пользователем.

## Стек

- Python 3
- pytest
- Selenium WebDriver
- Google Chrome

## Структура

- `tests/` — тестовые модули, разделённые по функциональности;
- `conftest.py` — драйвер и все pytest-фикстуры;
- `locators.py` — локаторы элементов интерфейса;
- `pages.py` — действия со страницами и явные ожидания;
- `data.py` — URL, тестовые константы и генераторы уникальных данных.

## Установка и запуск

На компьютере должен быть установлен Google Chrome.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
```

По умолчанию тесты запускаются в headless-режиме. Чтобы видеть окно Chrome:

```bash
HEADLESS=false pytest
```

