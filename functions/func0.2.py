def bank():
	print("welcome to SBI bank")
	account()
def account():
	print("account details")
	with_draw()
def with_draw():
	total=10000
	draw=1009
	balance=total-draw
	print("balance",balance)
bank()
	