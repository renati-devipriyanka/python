class Product:
    def __init__(self,product_price,quantity):
        self.product_price=product_price
        self.quantity=quantity
    def total_cost(self):
        print("enter product name",self.product_price)
        print("enter quantity ",self.quantity)
        return self.product_price*self.quantity
p=Product(20000,3)
a=p.total_cost()
print(a)