class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Customer:
    def __init__(self, name):
        self.name = name

    def buy(self, product):
        print(f"{self.name} bought {product.name} for ₹{product.price}")

# Create a product
p = Product("Book", 300)

# Create a customer
c = Customer("Suraj")

# Customer buys product
c.buy(p)
