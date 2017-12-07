# Ticket Management Application

Here we will provide more information about the ticket management application that we wrote
for the purpose of demonstrating upgrading from Django 1.8 to 1.11.

The sourcecode of the django app is located in the [app](../app/) folder.

## Setup

### Pre-Requesits

The application requires Python 3.4+ ([Python 2 is EOL in 2020](https://pythonclock.org/)) and
is best used with a virtual environment. The requirements are available in [app/requirements.txt](app/requirements.txt).

```bash
virtualenv -p python3 venv
source venv/bin/activate
pip install -r app/requirements.txt
```

### Setup

As with most Django apps, we have to apply migrations and create a superuser.

```bash
cd app
python manage.py migrate
python manage.py createsuperuser
```

### Running

Finally, we have to run the server

```bash
python manage.py runserver
```

## Features

This simple application has the following features:

* Registration
* Login
* Create a new ticket
* My tickets
* Edit tickets
* Write comments on tickets
* Django Admin

The ORM looks as follows:

ToDo

