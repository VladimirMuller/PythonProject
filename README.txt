1. Initialization for new project
        python3 -m venv venv

2. Activate enviroment for running
>.venv\Scripts\activate.bat
 
3. Initialization for new project
        (.vent)> pip install django
        (.vent)> django-admin startproject myApp

        (.vent)> pip install djangorestframework
        (.vent)> pip install markdown     
        (.vent)> pip install django-filter  
        (.vent)> pip install django-cors-headers

        Add 'rest framework' in \myApp\myApp\settings.py
        INSTALLED_APPS = [
            ...
            'rest_framework'
        ]

4. Select path
cd myApp

5. Run server on localhost:
(.vent) > python3 manage.py runserver
http://127.0.0.1:8000/


6. Initialization API for new project
        (.vent) > python3 manage.py startapp api     

7. Model modifications
        (.vent) > python3 manage.py makemigrations
        (.vent) > python3 manage.py migrate

        # Unapply old migrations:
        # python3 manage.py migrate api zero  
        # Remove the .pyc files under /migrations/_pycache_/ that you have unapplied.
        # Remove the .py files under migrations/ that you have unapplied.


8. REST API endpoints:
GET  http://127.0.0.1:8000/api/orders                - It gets all orders
GET  http://127.0.0.1:8000/api/waypoints             - It gets all waypoints
GET  http://127.0.0.1:8000/api/orders/5/waypoints    - It gets waypoints for order with id=5
POST http://127.0.0.1:8000/api/orders/create         - Create new order and waypoints
{
    "number": 10,
    "customer_name": "John",
    "date": "2025-03-05",
    "waypoints": [
        {
            "address": "Adresa 1",
            "type_address": "DE"
        },
        {
            "id": 6,
            "address": "Addresa 2",
            "type_address": "PI",
            "order": 5
        }
    ]
}



9. Other notes for debugging:

from django.db import connection
print(connection.queries)

from django.contrib.auth.models import User


10. VUE frontend in new Terminal
cd vue_frontend
npm run dev   

npm run build


  git init && git add -A && git commit -m "initial commit"
  