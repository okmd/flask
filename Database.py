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
			print("Unable to create table!")
			return False

	def insert(self, emp_id, name, position, emp_doj):
		# self.query = "insert into employees values ('{}','{}','{}','{}')".format(emp_id, name, position, emp_doj)
		self.query = 'insert into employees values (?,?,?,?)'
		try:
			self.cursor.execute(self.query,(emp_id, name, position, emp_doj))
			self.connection.commit()
			return True
		except:
			print("Unable to insert!!")
			return False

	def update(self, emp_id, name, position, emp_doj):
		self.query = "update employees set emp_name='{}', emp_position='{}', emp_doj='{}'  where emp_id = '{}' ".format(name, position, emp_doj, emp_id)
		try:
			self.cursor.execute(self.query)
			self.connection.commit()
			return True
		except:
			print("Unable to update!!")
			return False
	
	def delete(self, emp_id):
			# self.query = "insert into employees values ('{}','{}','{}','{}')".format(emp_id, name, position, emp_doj)
			self.query = "delete from employees where emp_id = '{}'".format(emp_id)
			try:
				self.cursor.execute(self.query)
				self.connection.commit()
				return True
			except:
				print("Unable to delete!!")
				return False

	def select_all(self):
		self.query = "select * from employees"
		try:
			self.cursor.execute(self.query)
			return self.cursor.fetchall()
		except:
			print("Unable to select!!")
			return False


	def select_one(self, emp_id):
		self.query = "select * from employees where emp_id = '{}'".format(emp_id)
		try:
			self.cursor.execute(self.query)
			return self.cursor.fetchone()
		except:
			print("Unable to select!!")
			return False

