# IoT Server

This project uses Django and Channels for IoT-related communication.

## Configuration

`SECRET_KEY` and `DEBUG` settings are loaded from environment variables. For development you may create a `.env` file or export them in your shell before starting the server.

Example `.env` file:

```
SECRET_KEY=change-me
DEBUG=True
```

Load the environment variables with [`django-environ`](https://github.com/joke2k/django-environ) or similar, or simply `export` them in your shell:

```bash
export SECRET_KEY=change-me
export DEBUG=True
python manage.py runserver
```

Ensure `SECRET_KEY` is set to a secure value and `DEBUG` is `False` in production.
