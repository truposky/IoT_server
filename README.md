# IoT Server

This project uses Django and Channels for IoT-related communication.

## Configuration

`SECRET_KEY` and `DEBUG` settings are loaded from environment variables. You can manage these variables with [`python-decouple`](https://github.com/henriquebastos/python-decouple) using a `.env` file or export them in your shell.

Example `.env` file:

```
SECRET_KEY=change-me
DEBUG=True
```

Install **python-decouple** and create a `.env` file, or simply `export` the variables in your shell:

```bash
export SECRET_KEY=change-me
export DEBUG=True
python manage.py runserver
```

Ensure `SECRET_KEY` is set to a secure value and `DEBUG` is `False` in production.
