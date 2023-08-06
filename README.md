# test_pvsmvd
Реализовать RESTful-сервис на Python с использованием FastAPI, SQLAlchemy, Alembic

Для реализации необходимо использовать следующие сущности: Author, Book, Genre.

1.Author содержит поля: Ф.И.О., дата рождения, жанр (у одного автора может быть одна или несколько написанных книг);

2.Book содержит поля: название, автор/авторы, количество страниц, опубликована или нет (у одной книги может быть несколько авторов);

3.Genre содержит поле: название (может быть только один жанру книги).

Реализовать CRUD-методы: GET_BY_ID, GET_ALL, POST, PATCH, DELETE.

Необходима реализация Docker-файла для запуска приложения