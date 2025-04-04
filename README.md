# Пульт охраны банка

**Пульт охраны банка** - этот проект представляет собой веб-приложение на Django, 
которое помогает охраннику следить за посетителями хранилища. 
Перед входом в хранилище установлен пропускной пункт, а все посещения фиксируются в базе данных. 
Пульт управления позволяет охраннику видеть, кто находится внутри, сколько времени они там провели и другую полезную информацию.

## Описание
Проект решает задачу мониторинга посетителей хранилища. 

**Основные функции:**
* Отображение списка активных посетителей (кто сейчас в хранилище).
* Показ времени входа и длительности пребывания.
* Возможность отмечать выход посетителей.
* Хранение истории посещений в базе данных.

Приложение создано с использованием Django ORM для работы с базой данных и предоставляет удобный интерфейс.

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](dvmn.org).

## Требования
* Python 3.8+
* Django 4.0+
* SQLite

## Установка
Для запуска проекта локально выполните следующие шаги:
1. Склонируйте репозиторий:
```bash
git clone https://github.com/1ns0mn1a7/django-orm-watching-storage.git
```
2. Перейдите в директорию проекта:
```bash
cd django-orm-watching-storage
```
3. Создайте виртуальное окружение и активируйте его:

*Для Mac OS/Linux:*
```bash
python -m venv venv
source venv/bin/activate
```
*Для Windows:*
```bash
python -m venv venv
source venv\Scripts\activate
```
4. Установите зависимости:
```bash
pip install -r requirements.txt
```
5. Настройте базу данных в .env
```python
DEBUG=True
ALLOWED_HOSTS=example.com,yourexample.com
DB_HOST=your-host
DB_PORT=your-port
DB_NAME=your-name
DB_USER=your-user
DB_PASSWORD=your-password
```
6. Примените миграции:
```bash
python manage.py migrate
```

## Использование
1. Запустите сервер:
```bash
python manage.py runserver
```
2. Откройте браузер и перейдите по адресу:
```http://127.0.0.1:8000/```
3. Основные функции пульта управления:

* Просмотр списка посетителей, находящихся в хранилище.
* Время входа посетителя в хранилище.
* Отметка выхода посетителя.
* Просмотр истории посещений.

## Лицензия
Проект лицензирован [MIT License](https://opensource.org/license/MIT). Полный текст лицензии доступен в файле LICENSE.
