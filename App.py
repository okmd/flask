from flask import Flask, render_template, url_for, request
from Database import Database
import sqlite3
import datetime

app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def index():
	db = Database()
	if request=='POST':
		emp_id = request.form['emp_id']
		emp_name = request.form['emp_name']
		emp_position = request.form['emp_position']
		emp_doj = "08-07-2019"
		db.insert(emp_id, emp_name,emp_position, emp_doj)
	else:
		emps = db.select_all()
		return render_template('index.html',employees=emps)

@app.route('/delete/<int:emp_id>', methods=['GET', 'POST'])
def delete():
	db = Database()
	if request=='POST':
		pass
	else:
		emps = db.select_all()
		return render_template('index.html',employees=emps)

if __name__ == '__main__':
	app.run()