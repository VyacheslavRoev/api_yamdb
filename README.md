# api_yamdb

### Описание
Проект YaMDb собирает отзывы пользователей на различные произведения.

### Алгоритм регистрации пользователей:
```
1. Пользователь отправляет POST-запрос на добавление нового пользователя с параметрами email и username на эндпоинт /api/v1/auth/signup/.
2. YaMDB отправляет письмо с кодом подтверждения (confirmation_code) на адрес email.
3. Пользователь отправляет POST-запрос с параметрами username и confirmation_code на эндпоинт /api/v1/auth/token/, в ответе на запрос ему приходит token (JWT-токен).
4. При желании пользователь отправляет PATCH-запрос на эндпоинт /api/v1/users/me/ и заполняет поля в своём профайле (описание полей — в документации).
```

### Пользовательские роли:
```
1. Аноним — может просматривать описания произведений, читать отзывы и комментарии.
2. Аутентифицированный пользователь (user) — может, как и Аноним, читать всё, дополнительно он может публиковать отзывы и ставить оценку произведениям (фильмам/книгам/песенкам), может комментировать чужие отзывы; может редактировать и удалять свои отзывы и комментарии. Эта роль присваивается по умолчанию каждому новому пользователю.
3. Модератор (moderator) — те же права, что и у Аутентифицированного пользователя плюс право удалять любые отзывы и комментарии.
4. Администратор (admin) — полные права на управление всем контентом проекта. Может создавать и удалять произведения, категории и жанры. Может назначать роли пользователям.
5. Суперюзер Django — обладет правами администратора (admin)
```

### Технологии:
Python 3.9, Django 2.2.16, DRF, JWT

## Проект написан в операционной системе Windows
### Как запустить проект(все команды выполняются в командной оболочке bach):

Клонировать репозиторий и перейти в него в командной строке.

Cоздать и активировать виртуальное окружение с учетом версии Python:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

## Примеры запросов:
### Регистрация нового пользователя
```
Получить код подтверждения на переданный email.

Использовать имя 'me' в качестве username запрещено.

Поля email и username должны быть уникальными.
```
```
POST    /api/v1/auth/signup/
```
```
{
  "email": "string",
  "username": "string"
}
```

Ответ:
```
{
  "email": "string",
  "username": "string"
}
```

### Получение JWT-токена
```
POST    /api/v1/auth/token/
```
```
{
  "username": "string",
  "confirmation_code": "string"
}
```

Ответ:
```
{
  "token": "string"
}
```

### Получение списка всех категорий
```
GET    /api/v1/categories/
```

Ответ:
```
[
  {
    "count": 0,
    "next": "string",
    "previous": "string",
    "results": [
      {
        "name": "string",
        "slug": "string"
      }
    ]
  }
]
```

### Добавление новой категории (Права доступа: Администратор)
```
POST    /api/v1/categories/
```
```
{
  "name": "string",
  "slug": "string"
}
```

Ответ:
```
{
  "name": "string",
  "slug": "string"
}
```

### Добавление произведения
```
Права доступа: Администратор.

Нельзя добавлять произведения, которые еще не вышли (год выпуска не может быть больше текущего).

При добавлении нового произведения требуется указать уже существующие категорию и жанр.
```
```
POST    /api/v1/titles/
```
```
{
  "name": "string",
  "year": 0,
  "description": "string",
  "genre": [
    "string"
  ],
  "category": "string"
}
```

Ответ:
```
{
  "id": 0,
  "name": "string",
  "year": 0,
  "rating": 0,
  "description": "string",
  "genre": [
    {
      "name": "string",
      "slug": "string"
    }
  ],
  "category": {
    "name": "string",
    "slug": "string"
  }
}
```
### Получение информации о произведении
```
GET    /api/v1/titles/{titles_id}/
```

Ответ:
```
{
  "id": 0,
  "name": "string",
  "year": 0,
  "rating": 0,
  "description": "string",
  "genre": [
    {
      "name": "string",
      "slug": "string"
    }
  ],
  "category": {
    "name": "string",
    "slug": "string"
  }
}
```

### Полуение отзыва по id
```
GET    /api/v1/titles/{title_id}/reviews/{review_id}/
```

Ответ:
```
{
  "id": 0,
  "text": "string",
  "author": "string",
  "score": 1,
  "pub_date": "2019-08-24T14:15:22Z"
}
```

### Частичное обновление отзыва по id
```
Права доступа: Автор отзыва, модератор или администратор.
```
```
PATCH   /api/v1/titles/{title_id}/reviews/{review_id}/
```
```
{
  "text": "string",
  "score": 1
}
```

Ответ:
```
{
  "id": 0,
  "text": "string",
  "author": "string",
  "score": 1,
  "pub_date": "2019-08-24T14:15:22Z"
}
```

### Получение комментария к отзыву
```
GET    /api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/
```

Ответ:
```
{
  "id": 0,
  "text": "string",
  "author": "string",
  "pub_date": "2019-08-24T14:15:22Z"
}
```
### Получение списка всех пользователей
```
Права доступа: Администратор
```
```
GET    /api/v1/users/
```

Ответ:
```
[
  {
    "count": 0,
    "next": "string",
    "previous": "string",
    "results": [
      {
        "username": "string",
        "email": "user@example.com",
        "first_name": "string",
        "last_name": "string",
        "bio": "string",
        "role": "user"
      }
    ]
  }
]
```
### Изменение данных своей учетной записи
```
Права доступа: Любой авторизованный пользователь

Поля email и username должны быть уникальными.
```
```
PATCH    /api/v1/users/me/
```
```
{
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string"
}
```

Ответ:
```
{
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string",
  "role": "user"
}
```

### Подробная документация к API доступна после запуска проекта
http://127.0.0.1:8000/redoc/

### Над проектом работали:
- ul [Цветков Никита](https://github.com/NikitaTsvetkov1990): управление пользователями (Auth и Users): система регистрации и аутентификации, права доступа, работа с токеном, система подтверждения через e-mail.
+ ul [Причко Надежда](https://github.com/NadyaMerlion): категории (Categories), жанры (Genres) и произведения (Titles): модели, представления и эндпойнты для них.
+ ul [Роев Вячеслав](https://github.com/VyacheslavRoev): отзывы (Review) и комментариями (Comments): модели, представления, эндпойнты, права доступа для запросов. Рейтинги произведений.