### twitter-excuse

Пишем рандомные отмазки в твиттер

"Отмазки" хранятся в Redis, который поднят на localhost'e в Docker

Для запуска на своей машине создайте файл .env рядом с файлом main.py;
запишите в него:

>TOKEN = "123456789-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

>TOKEN_KEY = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"

>CON_SEC = "aaaaaaaaaaaaaaaaaaaaaaaaa"

>CON_SEC_KEY = "qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq"

Так же необходимо создать папку **./logs/** и в ней файл **info.log**.

Вы можете самостоятельно перенастроить систему логирования - она тут
присутствует только для интереса и отладки.

Наполнение базы данных Redis "отмазками" или чем-либо еще зависит напрямую от вас.
При желании можно создать дополнительную переменную **replics** и уже из нее через **random.choice()** выбирать "желаемую" отмазку
