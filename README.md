# Development

Install ![poetry](https://github.com/python-poetry/poetry)
```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
```
Install dependencies
```
poetry install
```

Initial database setup
```
python manage.py makemigrations
python manage.py migrate
```

Run server
```
python manage.py runserver 0.0.0.0:3000
```

![localhost:3000/](http://localhost:3000/)
