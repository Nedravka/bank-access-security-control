# Пульт охраны банка
Это внутренний репозиторий для сотрудников банка. Если вы попали в
этот репозиторий случайно, то вы не сможете его запустить, т.к. у вас нет
доступа к БД, но можете свободно использовать код вёрстки или посмотреть как
реализованы запросы к БД.

Пульт охраны — это сайт, который можно подключить к удалённой базе данных с
визитками и карточками пропуска сотрудников нашего банка.
## Как установить
Достаточно скопировать репозиторий командой:

    git clone https://github.com/Nedravka/bank-access-security-control.git


Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:

    pip install -r requirements.txt

Сайт запускается командой:

    python manage.py runserver
    
Для полноценной работы необходимо в директории репозитория создать файл .env и прописать туда следующие параметры для подключения к БД:
    
    DB_ENGINE = 'postgres' или 'mysql' или 'oraclegis' и т.п
    PASSWORD = 'пароль БД'
    HOST = 'адрес хоста БД'
    NAME = 'название БД'
    USER = 'имя пользователя БД'
    PORT = 'порт БД'
    
А также рекомендуется добавить:

    SECRET_KEY = 'ваш код'
    ALLOWED_HOSTS = 'домен_1,домен_2,...,домен_n'
    
Опционально можно менять следующие параметры (дефолтно заданы):

    LANGUAGE_CODE = 'ru-ru'
    TIME_ZONE = 'Europe/Moscow'
    DEBUG = 'FaLse'
    
Или создать соответствующие переменные окружения в упомянутом формате другим способом, соответствующим вашей операционной системе.

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](http://dvmn.org).
## Links
Documentation: [https://docs.djangoproject.com/en/1.11/](https://docs.djangoproject.com/en/1.11/)
    
Git: [https://git-scm.com/docs/git](https://git-scm.com/docs/git)
    
Source Code: [https://github.com/Nedravka/bank-access-security-control](https://github.com/Nedravka/bank-access-security-control)
    