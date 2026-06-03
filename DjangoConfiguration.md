```bash
mkdir myproject
cd myproject

py -m venv venv_name

venv_name\Scripts\activate


pip install django
pip install mysqlclient
pip install flask
pip install django-crispy-forms
pip install crispy-bootstrap5

django-admin startproject projectname
cd projectname

django-admin startapp appname
python manage.py runserver
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

```
# Django Project Setup Guide

This guide explains how to install Django, create a project, create an application, and run the development server.

---

# 1. Install Django

First install Django using pip.

## Command

```bash
pip install django
```

This command installs the Django framework in your Python environment.

---

# 2. Create a Folder for Django Projects

Create a directory where you want to store all your Django projects.

## Command

```bash
mkdir django_projects
```

---

# 3. Move Inside the Folder

Navigate into the folder you created.

## Command

```bash
cd django_projects
```

---

# 4. Create a New Django Project

Use the Django administrative command to create a new project.

## Command

```bash
django-admin startproject projectname
```

Example:

```bash
django-admin startproject myproject
```

This creates the following structure:

```
myproject/
│
├── manage.py
└── myproject/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
```

---

# 5. Go Inside the Project

Move into the project directory.

## Command

```bash
cd projectname
```

Example:

```bash
cd myproject
```

---

# 6. Create a New Django Application

A Django project can contain multiple applications.

## Command

```bash
django-admin startapp appname
```

Example:

```bash
django-admin startapp blog
```

Application structure:

```
blog/
│
├── migrations/
├── __init__.py
├── admin.py
├── apps.py
├── models.py
├── tests.py
└── views.py
```

---

# 7. Run the Django Development Server

Start the development server.

## Command

```bash
python manage.py runserver
```

Output:

```
Starting development server at http://127.0.0.1:8000/
```

Open the browser and visit:

```
http://127.0.0.1:8000/
```

---

# Summary of Commands

```bash
pip install django
mkdir django_projects
cd django_projects
django-admin startproject projectname
cd projectname
django-admin startapp appname
python manage.py runserver
```

---

# Requirements

- Python 3.x
- pip
- Django

---

# Author

Project created for learning Django framework.

# Module of project structure

## 1. __init__
It is empty module due to its special name ,django consider it has 1 python module

## 2.asgi.py
It acts like a webserver gateway interface while deploying the django project

## 3. settings.py
This file keep track the changes what is happening in entire django project , if any changes are made need to informing the setting.py<br>
Changes like:-<br>
Example<br>
1.Installation of external module and software<br>
2.Creation of new folder in a hierarcy<br>
3.Connecting the external database<br>


## asgi.py
It contains path of urls configurations for each html page and it contains functions call 

# Module of application folder

## migrations
 Its is a folder which contains the imformation changes made to database

## admin.py
Its is a module which contains the imformation of admin related functionality

## apps.py
it contains the configuration belongs to current working project

## models.py
It contains database related imformation

## test.py
This Module contains Testing related code of our project

## views.py
This module contains bussiness logic or python related code 

## manage.py
It is a entry level module to run django project and it contain main function to run django project
