Код на основе уроков тестирования из плейлиста:
https://www.youtube.com/playlist?list=PLB2iiSfKWtvykq9s0plSVI_Du60i0iphU

Также стоит посмотреть:
https://www.youtube.com/playlist?list=PLeLN0qH0-mCVdHgdjlnKTl4jKuJgCK-4b

## Список команд

- `python -m venv venv` - создание среды
- `source venv/bin/activate` - её активация
- `pip freeze > requirements.txt` - запись списока зависимостей
- `pip install -r requirements.txt` - установка зависимостей
- `pip install pytest requests pydantic jsonschema`
- `pytest tests` - запуск тестов
  ctrl+shift+p add gitignore python
- `pytest -s -v tests/test_something.py` - запуск тестов расширенный

### Сомнительные команды

- `python -m venv --upgrade venv` - апгрейд версии Python в среде (ломает, т.к нужно ещё пакеты обновить)
- `pip install upgrade pytest requests pydantic jsonschema` -апгрейд пакетов

## Заметки

`jsonschema` vs `pydantic`

Плюсы:

- В `pydantic` компактное и простое описание схемы (без лишних "")
- В `pydantic` можно реализовать валидацию полей в том же класс что и описание схемы
- Утилита для `pydantic`: https://jsontopydantic.com

Пример описания `jsonschema` в файле `schemas/post.py`

Пример описания `pydantic` в файле `pydantic_schemas/post.py`
