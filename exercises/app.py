from databases import *
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return render_template(
        "home.html")
@app.route('/student/<int:ID>')
def home1(ID):
	return render_template(
		"student.html",
		num=ID)
	display_student(student_id)

app.run(debug=True)
