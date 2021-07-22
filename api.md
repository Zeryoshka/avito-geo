# Опсиание Api

## PING
Проверяет подключение и возвращает "PONG"

Пример запроса:
```json
GET /ping
```

Если  сервер доступен, то возвращает "PONG"

```json
HTTP 200 Successful
"PONG"
```


## SET
Создание пары ключ значение. Возможно задать ttl

Пример запроса:
```json
POST /set
{
    "KEY": "name",
    "VALUE": "Sergey",
    "TTL": 10
}
```
|Поле            |Тип                     |Описание                                                                                 |
|:---------------|:-----------------------|:----------------------------------------------------------------------------------------|
|KEY             |Строка                  |Ключ состоящий из английских букв, цифр и символов подчеркивания, не начинающийся с цифры|
|VALUE           |Строка                  |Значение, сопоставляемое ключу                                                           |
|TTL             |Натуральное число       |Время жизни пары в секундах                                                              |

Все поля кроме TTL обязательны

* В случае если запрос составлен некорректно, сервер вернет ошибку `HTTP 400 Bad Request`
* В случае если невозможно установить новое значение для ключа, сервер врнет ошибку `HTTP 400 Bad Request`
* В сулчае если запрос составлен корректно и значение можно установить, сервер вернет `HTTP 201 Created`
```json
HTTP 201 Created
{
    "is_created": true,
    "message": "OK"
}
```

## GET
Чтение пары ключ значение

Пример запроса:
```json
POST /get
{
    "KEY": "name",
    "VALUE": "Sergey",
    "TTL": 10
}
```
|Поле            |Тип                     |Описание                                                                                 |
|:---------------|:-----------------------|:----------------------------------------------------------------------------------------|
|KEY             |Строка                  |Ключ состоящий из английских букв, цифр и символов подчеркивания, не начинающийся с цифры|

Все поля обязательны

* В случае если запрос составлен некорректно, сервер вернет ошибку `HTTP 400 Bad Request`
* В случае если невозможно получить текущее значение для ключа, сервер врнет ошибку `HTTP 400 Bad Request`
* В сулчае если запрос составлен корректно и значение можно установить, сервер вернет `HTTP 200 Created`
```json
HTTP 200 Successful
{
    "is_created": true,
    "message": "OK"
}
```

