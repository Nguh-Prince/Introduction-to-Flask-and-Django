import sqlite3 # For sqlite database connection

from flask import Flask # used to create the app

# used to render HTML files to the browser
from flask import render_template

# used to access request information like form data, cookies, etc.
from flask import request

from create_db import get_path_to_sqlite_database

app = Flask(__name__) # create a Flask app

# gets the absolute path to this app's database, 
# the db.sqlite file created after running the create_db.py 
# script
path_to_db = get_path_to_sqlite_database(file_path=__file__)

@app.route('/', methods=["GET", "POST"])
def index():
    #TODO
    # add functionality to add a new project and student
    # to the database 
    return render_template("index.html")

@app.rout('/projects')
def projects():
    #TODO
    # get list of projects from the database
    # return a dictionary of those projects to the browser
    # replace simple json output with an HTML page, containing 
    # a table of the projects
    # add styles and JavaScript to this page 
    return "Display list of projects to this page"