### Linux

Commands

- Install

  **`python3 -m pip install virtualenv`**

- Create Virtualenv In a Folder

  **`python3 -m pip virtualenv ENV_NAME`**

  **`virtualenv ENV_NAME`**

- Activation

  - Linux

    **`source ./myapp/bin/activate`**

  - Windows

    **`./myapp/Scripts/activate`**

- Django

  1. Install django

     **`pip install django`**

  1. Create Django Main Application

     **`django-admin startproject PROJECT_NAME`**

  1. Run django server

     **`python manage.py runserver`**

  1. Collect Static Files

     **`python manage.py collectstatic`**

  1. Create app

     **`python manage.py startapp APP_NAME`**

  1. Make Migration

     - **`python manage.py makemigrations`**
     - **`python manage.py makemigrations APP_NAME`**

  1. Migrate

     **`python manage.py migrate`**

     - Sync DB
       - python manage.py migrate

  1. Create Super User

     **`python manage.py createsuperuser`**

# CHECK COMMMIT be8b067f886b4d4eac535c5c9079d568e4eeba61 FOR CASUAL AUTH
