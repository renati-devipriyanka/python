class Add:
	def __init__(self,a,b):
		self.a=a
		self.b=b
	def addition(self):
		c=self.a+self.b
		return c
d=Add(10,20)
e=d.addition()
print(e)