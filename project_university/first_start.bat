@echo off

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

pause