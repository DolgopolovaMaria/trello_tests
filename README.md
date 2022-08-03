# Автотесты для Trello
Для локального запуска нужно добавить в проект файл <code>config.py</code> со своими ключом и токеном для Trello:
```python
TOKEN = 'my token'
KEY = 'my key'
```
Чтобы получить ключ и токен, нужно залогиниться в <a target="_blank" href="https://trello.com/">Trello</a> и перейти <a target="_blank" href="https://trello.com/app-key">сюда</a>.

Установка зависимостей с помощью pip:
```shell
pip install virtualenv
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```

Запуск всех тестов:
```shell
pytest
```

Запуск тестов для досок/списков/карточек (<code>board</code>/<code>list</code>/<code>card</code>):
```shell
pytest -m board
```
Запуск позитивных/негативных (<code>positive</code>/<code>negative</code>) тестов:
```shell
pytest -m positive
```

