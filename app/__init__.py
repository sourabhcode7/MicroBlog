from flask import Flask
# Flask is a Python framework used to build web applications. 
# We import the Flask class so that we can create our application.

app = Flask(__name__)
# Here: Flask(__name__) creates a new Flask application.
# app stores that application.
# In simple words: We are creating our web application and giving it the name app.

app.config.from_object('config')

from app import views

#Why do we import views at the end?
#This is the most important concept: Circular Import.

#Imagine we have two files:

#File 1: app/__init__.py
#from flask import Flaskapp = Flask(__name__)from app import views

#File 2: app/views.py
#from app import app@app.route('/')def home():    return "Hello, World!"

# Notice something?
# - __init__.py imports views.
# - views.py imports app from __init__.py.
# So both files depend on each other!

# This is called a circular import.

# How do we solve it?

# We first create the Flask application:
# app = Flask(__name__)

# Then, after creating the application, we import views:
# from app import views

# Now, when views.py imports app, the application has already been created.

# That's why we put the import statement at the end so it avoids circular import error