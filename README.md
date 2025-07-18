# CRM System

Добро пожаловать в CRM систему — мощное и удобное веб-приложение для управления услугами, рекламными кампаниями, лидами, клиентами и контрактами.

---

## Описание

CRM система разработана на Django 5.2 и предназначена для автоматизации бизнес-процессов в отделах продаж и маркетинга. Она позволяет:

- Управлять каталогом услуг (Products)
- Вести рекламные кампании (Ads)
- Обрабатывать и отслеживать лиды (Leads)
- Управлять клиентской базой (Customers)
- Работать с контрактами (Contracts)
- Управлять пользователями и правами доступа

---

## Технологии

- Python 3.11+
- Django 5.2.4
- PostgreSQL (в качестве базы данных)
- Bootstrap 5 (для фронтенда)
- Font Awesome (иконки)
- HTML5, CSS3, JavaScript

---

## Установка и запуск

1. Клонируйте репозиторий:

```

git clone https://github.com/martinankru325/CRM-system.git
cd CRM-system

```

2. Создайте и активируйте виртуальное окружение:

```

python -m venv venv
source venv/bin/activate  \# Linux/macOS
venv\Scripts\activate     \# Windows

```

3. Установите зависимости:

```

pip install -r requirements.txt

```

4. Настройте базу данных PostgreSQL:

- Создайте базу данных `crm_db`
- Создайте пользователя `crm_user` с паролем
- Обновите настройки в `CRM-system/settings.py`, если необходимо

5. Выполните миграции:

```

python manage.py migrate

```

6. Создайте суперпользователя:

```

python manage.py createsuperuser

```

7. Запустите сервер разработки:

```

python manage.py runserver

```

8. Откройте в браузере: [http://localhost:8000/](http://localhost:8000/)

---

## Основные URL

- `/users/login/` — страница входа
- `/users/logout/` — выход из системы (через POST)
- `/` — главная страница с общей статистикой (доступна после входа)
- `/products/` — управление услугами
- `/ads/` — управление рекламными кампаниями
- `/leads/` — управление лидами
- `/customers/` — управление клиентами
- `/contracts/` — управление контрактами
- `/admin/` — административная панель Django

---

## Особенности

- Аутентификация и авторизация с использованием стандартных Django Views
- Защита от CSRF и безопасный выход из системы через POST-запрос
- Использование Bootstrap 5 и Font Awesome для удобного и современного интерфейса
- Гранулярные права доступа к разделам с проверкой в шаблонах
- Локализация на русский язык и часовой пояс Europe/Moscow

---

## Рекомендации

- Для продакшена используйте `DEBUG = False` и настройте `ALLOWED_HOSTS`
- Храните секретные ключи и пароли в переменных окружения
- Настройте HTTPS и другие меры безопасности при деплое

---

## Контакты и поддержка

Если у вас возникли вопросы или предложения, пожалуйста, создайте issue в репозитории или свяжитесь по электронной почте: martinankru927@gmail.com

---

Спасибо за использование CRM системы!


