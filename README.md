# Simple django app

Simple Django application made with [Django](https://docs.djangoproject.com/en/3.2/) and [Django REST framework](https://www.django-rest-framework.org/)

## Installation
1. Download the simple-django-app
2. Create and activate virtual environment  
   ```python -m virualenv venv```  
   ```source ./venv/bin/activate```
3. Install the required libraries  
  ```pip install -r requirements.txt```

## Usage 
For using simple-django-app enter  
```gunicorn simpleapp.wsgi```  or  ```python manage.py runserver 8000```  

## The CRUD application made with Django:  
  
```https://localhost:8000/blog/~```  
  
**CRUD** means performing Create, Retrieve, Update and Delete operations on a table in a database.  


**Create** – create or add new posts in a table in the database.  
**Retrieve** – read, retrieve, search or view posts as a list(List View) or retrieve a post in detail (Detail View)  
**Update** – update or edit existing posts in a table in the database  
**Delete** – delete, deactivate, or remove existing posts in a table in the database  

## The REST application made with Django Rest Framework:  
  
```https://localhost:8000/drf_blog/api/~```  

**REST** is a protocol for creating, listing, changing and deleting data on your server over HTTP.  
The **Django REST framework (DRF)** is a toolkit built on top of the Django web framework that reduces the amount of code you need to write to create **REST** interfaces.  
