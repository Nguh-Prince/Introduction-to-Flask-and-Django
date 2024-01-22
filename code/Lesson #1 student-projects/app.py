import sqlite3

from flask import Flask, render_template, request

app = Flask(__name__)

from create_db import get_path_to_sqlite_database

path_to_db = get_path_to_sqlite_database(file_path=__file__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        # TODO send the list of students to the template and display a select 
        # instead of the input text
        return render_template("index.html")
    elif request.method == 'POST':
        student_name = request.form['name']
        project_name = request.form['project-name']
        project_description = request.form['project-description']
        
        with sqlite3.connect(path_to_db) as connection:
            # save the student to the database
            cursor = connection.cursor()
            insert_into_student_table_query = "INSERT INTO Students (name) VALUES(?)"        
            cursor.execute(insert_into_student_table_query, (student_name, ))

            connection.commit()
    
            select_last_student_query = "SELECT id FROM Students ORDER BY id DESC LIMIT 1"
            result = cursor.execute(select_last_student_query).fetchone()

            latest_student_id = result[0]

            inset_into_projects_table_query = "INSERT INTO Projects (student, name, description) VALUES (?,?,?)"

            cursor.execute(inset_into_projects_table_query, (latest_student_id, project_name, project_description))
            connection.commit()
        
        return "<p>Project saved successfully. Go back to <a href="/">index page</a></p>"

@app.route('/projects')
def projects():
    with sqlite3.connect(path_to_db) as connection:
        cursor = connection.cursor()

        result = cursor.execute(
            """
                SELECT p.id, p.name, p.description, s.name as student, s.id as student_id 
                FROM Projects as p LEFT JOIN Students AS s ON p.student=s.id 
            """
        ).fetchall()

        result_dictionary = [
            { 
                "project": {
                    "name": f[1],
                    "id": f[0],
                    "description": f[2]
                },
                "student": {
                    "name": f[3],
                    "id": f[4]
                }
            } for f in result
        ]
        return render_template("projects.html", projects=result_dictionary)