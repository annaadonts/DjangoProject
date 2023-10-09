# DjangoProject
This is how you can structure a Django project to integrate a Python script and visualize the results
# Install Django:
pip install Django

# Create a new Django project:
django-admin startproject myproject

# Create a new Django app:
python manage.py startapp myapp

# Make a 'urls.py' file in your app

# Include your app in the INSTALLED_APPS list in the settings.py file:
INSTALLED_APPS = [

    'myapp',
]

# Run the server:
python manage.py runserver
