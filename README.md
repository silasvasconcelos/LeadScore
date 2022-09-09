# LeadScore

## Development settings

### Dependencies

- [Python 3.10](https://www.python.org/)
  > Tip: Recommend install the [PyEnv](https://github.com/pyenv/pyenv) to manager python verions.
- [Poetry](https://python-poetry.org/)

### Running

Clone this repository, copy `.env.example` file to `.env` and changed values, after run:


```shell
# installing dependencies
poetry install

# running migrations
poetry run python manage.py migrate

# creating a user
poetry run python manage.py migrate

# running the project
poetry run python manage.py runserver
```

### API Documentation
- reDoc: http://localhost:8000/ - Recommended for public readers
- Swagger: http://localhost:8000/swagger - Recommended for developers (use JWT and Basic authentications)