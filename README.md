# Список команд

- `python -m venv venv` - создание среды
- `source venv/bin/activate` - её активация
- `pip freeze > requirements.txt` - запись списока зависимостей
- `pip install -r requirements.txt` - установка зависимостей
- `pip install pytest requests pydantic jsonschema`
- `pytest tests` - запуск тестов
  ctrl+shift+p add gitignore python
- `pytest -s -v tests/test_something.py` - запуск тестов расширенный

Описание параметров:
-s capture, показывает print с тестов
-v verbose, подробное отображение
-k expression, отсев тестов по меткам
--duration=3 отметка тестов выполняющихся дольше указанного времени
-vv подробное описание по времени

## Сомнительные команды

- `python -m venv --upgrade venv` - апгрейд версии Python в среде (ломает, т.к нужно ещё пакеты обновить)
- `pip install upgrade pytest requests pydantic jsonschema` -апгрейд пакетов

## Заметки

### `jsonschema` vs `pydantic`

Плюсы:

- В `pydantic` компактное и простое описание схемы (без лишних "")
- В `pydantic` можно реализовать валидацию полей в том же класс что и описание схемы
- Утилита для `pydantic`: <https://jsontopydantic.com>

Пример описания `jsonschema` в файле `schemas/post.py`

Пример описания `pydantic` в файле `pydantic_schemas/post.py`

### fixture

Выполняются перед тестом (Например, подключение к базе данных)

Можно передавать функции

`scope`:

- `function` - (по умолчанию) повторное выполнение `fixture` при повторном вызове,
- `session` - выполнение `fixture` единожды и затем использование кэшированного результата в рамках всего теста
- Замысел - повышение производительности/скорости исполнения тестов за счёт исключения повторяющихся действий

`autouse`:

- `True` - `fixture` будет исполняться для каждого теста без дополнительного указания

### parametrise

Проверка одинаковых функций с разными входными данными

Выглядит удобно, но реализуется странно

- `@pytest.mark.parametrize`

### custom mark

Кастомные метки задаются в pytest.ini
Добавляются к тестам через декораторы
На тесте может стоять несколько меток

- `@pytest.mark.production`
- `@pytest.mark.development`

Запуск тестов с метками:

- `pytest -s -v -k development tests`

Запуск всех, кроме тестов с метками

- `pytest -s -v -k "not development"  tests`

Skip теста по причинам в комментарие

- `@pytest.mark.skip("Комментарий")`

## Источники

Код на основе уроков тестирования из плейлиста:
<https://www.youtube.com/playlist?list=PLB2iiSfKWtvykq9s0plSVI_Du60i0iphU>
