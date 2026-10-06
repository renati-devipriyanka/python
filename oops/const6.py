class Student:
	def __init__(self):
		self.id=101
		self.name="ramya"
		self.age=21
	def details(self):
		print("student id is:",self.id)
		print("student name is:",self.name)
		print("student age is:",self.age)
		print()
s1=Student()
s1.details()
