class Product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.quantity=quantity
        self.price=price
    def get_total_value(self):
        return self.quantity*self.price
    def change_price(self,new_price):
        self.price=new_price
    def increase_stock(self,amount):
        self.quantity+=amount
    def decrease_stock(self,amount):
        self.quantity-=amount


p1=Product("Tv",100,1)
p2=Product("AC",2000,2)

print(Product.get_total_value(p2))

