# Тестовое задание в юнит гео в avito

## Описание задания
Цель задания – разработать приложение имплементацию in-memory Redis кеша. Подробности [тут](https://github.com/avito-tech/geo-backend-trainee-assignment/blob/main/README.md).

### Необходимый функционал

* Клиент и сервер REST API
* Key-value хранилище строк, списков, словарей
* Возможность установить TTL на каждый ключ
* Реализовать операторы: GET, SET, DEL, KEYS
* Реализовать покрытие несколькими тестами функционала

## Особенности реализации сервера
Приложение разработано под python версии 3.8+.  
(**Почему?** Потому что соотношение мои знания языка/время разработки на этом языке максимально)

В качестве web-фреймворка использовался flask.  
Для валидации запросов используеися библиотека marshmallow

Реализаиця сервера находится в папке serdis-server

## Описание api
Api подробно описан в [файле](https://github.com/Zeryoshka/avito-geo/blob/master/api.md) `api.md`

## Тестирование
Для тестирования использовался модуль `pytest`, все тесты находятся в папке `tests`, для оценки покрытия кода тестами исопльзовался `pytest-coverage`.

Для запуска тестов необходимо выполнить следующие команды:
```bash
pip install -r test-requirements.txt
pytest --cov=serdis_server -v  
```

Покрытие тестов на последнем замере: 92%


