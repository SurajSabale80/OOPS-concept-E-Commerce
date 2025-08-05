# Base Class - Product
class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def display_info(self):
        print(f"Product ID: {self.product_id}, Name: {self.name}, Price: ₹{self.price}")

# Inherited Class 
class ElectronicProduct(Product):
    def __init__(self, product_id, name, price, warranty):
        super().__init__(product_id, name, price)
        self.warranty = warranty

    def display_info(self): 
        super().display_info()
        print(f"Warranty: {self.warranty} years")

# Customer Class
class Customer:
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email

    def display_profile(self):
        print(f"Customer ID: {self.customer_id}, Name: {self.name}, Email: {self.email}")

# Cart Class
class Cart:
    def __init__(self):
        self.items = []  

    def add_to_cart(self, product, quantity):
        self.items.append((product, quantity))
        print(f"Added {quantity} x {product.name} to cart.")

    def view_cart(self):
        print("\n🛒 Cart Contents:")
        total = 0
        for product, qty in self.items:
            product.display_info()
            print(f"Quantity: {qty}")
            total += product.price * qty
            print("-" * 30)
        print(f"Total Amount: ₹{total}")

# Order Class (Encapsulation)
class Order:
    def __init__(self, customer, cart):
        self.__order_id = f"ORD{customer.customer_id}"
        self.customer = customer
        self.cart = cart
        self.__status = "Pending"

    def place_order(self):
        print(f"\nPlacing order for {self.customer.name}")
        self.cart.view_cart()
        self.__status = "Placed"
        print(f"Order {self.__order_id} placed successfully!")

    def get_status(self): 
        return self.__status

# Example Usage
if __name__ == "__main__":
    # Create products
    p1 = Product(1, "T-Shirt", 499)
    p2 = ElectronicProduct(2, "Smartphone", 14999, 2)

    # Create customer
    c1 = Customer(101, "Suraj", "suraj@example.com")

    # Add to cart
    cart = Cart()
    cart.add_to_cart(p1, 2)
    cart.add_to_cart(p2, 1)

    # Place Order
    order = Order(c1, cart)
    order.place_order()
    print("Order Status:", order.get_status())
