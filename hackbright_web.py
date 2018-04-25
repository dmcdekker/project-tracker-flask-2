"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route('/')
def home():

    students = hackbright.get_students()

    projects = hackbright.get_projects()


    html = render_template("home.html",
                            students=students,
                            projects=projects)

    return html



@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)

    projects = hackbright.get_grades_by_github(github)

    # return "{acct} is the GitHub account for {first} {last}".format(
    #     acct=github, first=first, last=last)

    html = render_template("student_info.html",
    						first=first,
    						last=last,
    						github=github,
                            projects=projects)

    return html


@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")


@app.route("/student-add", methods=['POST'])
def student_add():
    """Add a student."""

    first = request.form.get("first_name")
    last = request.form.get("last_name")
    github = request.form.get("github")

    hackbright.make_new_student(first, last, github)

    return render_template("thank_you.html",
    						github=github)


@app.route("/add-form")
def student_add_form():
	""""""

	return render_template("student_add.html")

@app.route('/project')
def project_info():
    
    project_title = request.args.get('project_title')

    project_grades = hackbright.get_grades_by_title(project_title)

    project_info = hackbright.get_project_by_title(project_title)

    html = render_template("project_info.html",
                            project_info=project_info,
                            project_grades=project_grades)

    return html
    


if __name__ == "__main__":
	print "Hackbright-Web.py App"
	hackbright.connect_to_db(app)
	app.run(debug=True)