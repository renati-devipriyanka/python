class Priyanka:
	def __init__(self,number1,number2):
		self.number1=number1
		self.number2=number2
	def add(self):
		print("first number",self.number1)
		print("Second number",self.number2)
		a=self.number1+self.number2
		return a
p=Priyanka(10,20)

print(p.add())

	