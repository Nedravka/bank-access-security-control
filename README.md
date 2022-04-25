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

Скрипт запускается командой:

    manage.py runserver

Доступен для просмотра по адресу:

    http://127.0.0.1:8000/

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](http://dvmn.org).
## Links
Documentation: [https://docs.djangoproject.com/en/1.11/](https://docs.djangoproject.com/en/1.11/)
    
Git: [https://git-scm.com/docs/git](https://git-scm.com/docs/git)
    
Source Code: [https://github.com/Nedravka/bank-access-security-control](https://github.com/Nedravka/bank-access-security-control)
    