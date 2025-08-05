 🛒 Simple E-commerce System using Python (OOP)

This is a basic E-commerce system implemented in Python using Object-Oriented Programming (OOP) concepts. It simulates the core functionality of an online shopping system such as:

- Creating products
- Managing a customer
- Adding products to a cart


 📚 OOP Concepts Used

| Concept         | Implemented In                            |
|----------------|--------------------------------------------|
| Class & Object  | All classes (`Product`, `Customer`, etc.) |
| Encapsulation   | Private variables in `Order` class        |
| Inheritance     | `ElectronicProduct` inherits from `Product` |
| Polymorphism    | Method overriding in `display_info()`     |
| Abstraction     | Getter method for order status            |


 🧱 Classes Overview

- **Product**: Base class for all products.
- **ElectronicProduct**: Inherits from `Product`, adds warranty info.
- **Customer**: Stores customer details.
- **Cart**: Adds and lists products selected by the customer.
- **Order**: Places an order and tracks status using encapsulation.


 ▶️ How to Run

Make sure you have Python installed.

1. Save the code in a file called `ecommerce.py`
2. Open terminal or command prompt
3. Run the program:

```bash
python ecommerce.py
