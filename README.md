# Storefront
A store App developed using Django, RESTFul API, JWT.
SQLite has been used as database.
_Training Material_

# Installation
- Clone the repository to your working folder
```bash
$ git clone git@github.com:MuhammadAlgshy/Storefront.git
```
- Install requirments 
```bash
$pip install -r requirments.txt
```
- Setting Configuration
```bash
# Set the Django security key (storefront/settings --> SECRET_KEY)
SECRET_KEY = 'django-insecure-_YOURSECURITYCODE_'
```
```bash
# Set your database settings (storefront/settings --> DATABASES)
# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'Storefront.sqlite',
    }
}
```
- Database Migration
```bash
# Go to you working directory on terminal/cmd
$ cd _workingdirectory_
```
```bash
# Make database migration 
$Python manage.py makemigrations
# Migrate Database
$Python manage.py migrate
```
- Create Admin user
```bash
$ python manage.py createsuperuser
```
- Run Server
```bash
# Run django server
$python manage.py runserver
```
- Login to admin area, open Browser and go to: http://127.0.0.1:8000/admin/
- Check the list of available APIs, open Browser and go to: http://127.0.0.1:8000/store/

Enjoy the experiance.

