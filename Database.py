import sqlite3
import datetime

class Database():
	database_name = "database.db"
	def __init__(self):
		try:
			self.connection = sqlite3.connect(Database.database_name)
			self.cursor = self.connection.cursor()
		except:
			print("Unable to establish connection!!")

	def create_table(self):
		self.query = '''create table if not exists employees(
		   emp_id INTEGER PRIMARY KEY UNIQUE,
		   emp_name TEXT NOT NULL,
		   emp_position TEXT NOT NULL,
		   emp_doj datetime NOT NULL)
		'''
		try:
			self.cursor.execute(self.query)
			self.cursor.commit()
		except:
			print("sorry")

	def insert(self, emp_id, name, position, emp_doj):
		self.query = '''insert into employees values (?,?,?,?, ?)'''
		try:
			self.cursor.execute(self.query,(emp_id, name, position, emp_doj))
			self.cursor.commit()
		except:
			print("Unable to insert!!")

	def select_all(self):
		self.query = "select * from employees"
		try:
			self.cursor.execute(self.query)
			return self.cursor.fetchall()
		except:
			print("Unable to select!!")

	def __del__(self):
		self.connection.close()
