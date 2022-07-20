# User Recommandation System

When you follow someone on Twitter, Facebook or Instagram, the website may recommend some
close friends of this user to you. This web service will implement a similar functionality based on the
Twitter dataset we collected.

## Getting started

These instructions will get you a copy of the project up and running on your local machine for development.

## Prerequisites

```
- Python 3.10.2
```

## Installation and setup

- Clone the repo

```
git clone https://github.com/Paccy10/pivot-user-recommandation-system.git
```

- Download python

```
https://www.python.org/downloads/
```

- Create the virtual environment

```
python -m venv venv
```

- Activate virtual environment

  - MacOS and Linux

  ```
  source venv/bin/activate
  ```

  - Windows

  ```
  .\venv\Scripts\activate
  ```

- Install dependencies

```
pip install -r requirements.txt
```

- Make a copy of the .env.sample file and rename it to .env and update the variables accordingly

- Apply migrations

```
python manage.py migrate
```

- When you make changes to the database models, run migrations as follows

  - Make new migrations

  ```
  python manage.py makemigrations
  ```

  - Run migrations

  ```
  python manage.py migrate
  ```

## Running

- Running app

```
python manage.py runserver
```
