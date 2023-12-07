# Simple social media app

How to run server:

1. clone this repo
2. set your db in `.env` file
3. enter backend dir with `cd backend`
4. install requirements: `pip install -r requirements.txt`
5. enter django dir `cd social_media`
6. migrate to db `python manage.py migrate`
7. create superuser with `python manage.py createsuperuser`
8. run server `python manage.py runserver`

How to run bot:

1. run server
2. `cd bot` from root dir
3. run `pip install -r requirements.txt`
4. run `python bot.py`
