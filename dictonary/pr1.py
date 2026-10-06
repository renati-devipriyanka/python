d=dict()
print(d)
l=[10,20,30]
print(type(d))
d[1]=100
d[2]=200
d[3]=400
print(d)
print(d.keys())
print(d.values())
print(d.items())
print(d.get(4,"hello"))
print(d.fromkeys(l,0))
s="python is easy programing languge, python is simple"
s=s.split(" ")
d={}
print(d)

for i in s: 
	if i not in d:
		d[i]=1
	else:
		d[i]+=1
	
print(d)
d={ i:s.count(i) for i in s }
print(d)
d.popitem()
print(d)
