#reduce function
from functools import reduce
cost=[100,200,349,599,549,497]
total_cost=reduce(lambda x,y:x+y,cost)
print(total_cost)