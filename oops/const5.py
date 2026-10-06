class Student:
	def __init__(self,id,name,age):
		self.id=id
		self.name=name
		self.age=age
	def details(self):
		print("student id is:",self.id)
		print("student name is:",self.name)
		print("student age is:",self.age)
		print()
s1=Student(101,"ramya",21)
s1.details()
s2=Student(102,"raju",20)
s2.details()


		