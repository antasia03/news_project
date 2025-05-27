# News Project

Пет-проект новостного сайта на Django.  
Позволяет публиковать, редактировать и удалять новости, управлять ими через админку и тестировать email-уведомления в консоли.

## Технологии

- **Python 3.10+**
- **Django**
- **SQLite** (по умолчанию)
- **HTML, CSS**
- **Django Admin**
- **Email (вывод в консоль для тестирования)**


## Быстрый старт

1. **Клонируйте репозиторий:**
git clone https://github.com/antasia03/news_project.git
cd news_project

2. **Создайте и активируйте виртуальное окружение:**
python -m venv venv
source venv/bin/activate # Linux/Mac
venv\Scripts\activate # Windows

3. **Установите зависимости:**
pip install -r requirements.txt

4. **Примените миграции:**
python manage.py migrate

5. **Создайте суперпользователя для доступа к админке:**
python manage.py createsuperuser

6. **Запустите сервер:**
python manage.py runserver

7. **Откройте сайт в браузере:**
http://127.0.0.1:8000/

## Админка

Доступ к админке:  
http://127.0.0.1:8000/admin/

Войдите под логином и паролем суперпользователя.

**В админке можно:**
- Управлять новостями (добавлять, редактировать, удалять)
- Управлять пользователями и правами

## Email-уведомления

Для локальной разработки email-уведомления выводятся в консоль (терминал).  
Настройка в `settings.py`:
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

**Все письма можно увидеть в консоли при запуске сервера.**

Для реальной отправки писем настройте SMTP в файле `settings.py`.


