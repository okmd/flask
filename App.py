from flask import Flask, render_template, url_for, request, redirect
from Database import Database
import sqlite3
import datetime

app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def index():
	db = Database()
	if request.method=='POST':
		emp_id = request.form['emp_id']
		emp_name = request.form['emp_name']
		emp_position = request.form['emp_position']
		emp_doj = request.form['emp_doj']
		db.insert(emp_id, emp_name,emp_position, emp_doj)
		return redirect('/')
	else:
		emps = db.select_all()
		return render_template('index.html',employees=emps)

@app.route('/update/<int:emp_id>', methods=['GET', 'POST'])
def update(emp_id):
	db = Database()
	if request.method=='POST':
		emp_name = request.form['emp_name']
		emp_position = request.form['emp_position']
		emp_doj = request.form['emp_doj']
		db.update(emp_id, emp_name,emp_position, emp_doj)
		return redirect('/')
	else:
		emps = db.select_one(emp_id)
		return render_template('update.html',emp=emps)

@app.route('/delete/<int:emp_id>', methods=['GET', 'POST'])
def delete(emp_id):
	db = Database()
	db.delete(emp_id)
	return redirect('/')


if __name__ == '__main__':
	app.run(debug=True)