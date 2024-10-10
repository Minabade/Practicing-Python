class Product:
    def __init__(self,name,price,stock,weight):
        self.name = name
        self.price = price
        self.stock = stock
        self.weight = weight

    def get_info(self):
        return f"Product Name: {self.name}, Price: ${self.price}, Stock: {self.stock}, Weight: {self.weight} kg"

    def apply_discount(self,discount_percentage):
        self.price -= discount_percentage * self.price

    def check_stock(self,quantity):
        if self.stock >= quantity:
            self.stock -= quantity
            return f"Order {quantity} units of {self.name}: Successful, Stock left: {self.stock}"
        else:
            return {"Out of stock"}
        
    def calculate_shipping_cost(self):
        shipping_cost = 10 * self.weight
        return f"shipping cost for {self.name}:${shipping_cost}"


class ElectronicProduct(Product):
    def __init__(self,name,price,stock,weight,warranty_years,brand):
        super().__init__(name,price,stock,weight)
        self.warranty_years  = warranty_years
        self.brand = brand
    
    def get_info(self):
        return f"Electronic Product: {self.name}: {self.brand}, Price: ${self.price}, Warranty: {self.warranty_years} Stock: {self.stock}, Weight: {self.weight} kg"
    
    def calculate_warranty_extension(self,extra_years):
        self.warranty_years += extra_years
        return f"Extended warranty for {self.name} is {self.warranty_years} years"

class GrocreyProduct(Product):
    def __init__(self,name,price,stock,weight,expiration_date,is_perishable):
        super().__init__(name,price,stock,weight)
        self.expiration_date  = expiration_date
        self.is_perishable = is_perishable

    def get_info(self):
        return f"Grocery Product: {self.name}, Price: ${self.price}, Expiration Date: {self.expiration_date} Stock: {self.stock}, Weight: {self.weight} kg, Perishable: {self.is_perishable}"
    
    def check_if_expired(self,current_date):
        if self.expiration_date == current_date:
            return f"Is {self.name} expired? True"
        else:
            return f"Is {self.name} expired? False"
        


Laptop = ElectronicProduct("Laptop",1500,10,2.5,3,"Dell")
Milk = GrocreyProduct("Milk",4,50,1,"2024-11-15","True")

print(Laptop.get_info())
Laptop.apply_discount(0.15)
print(Laptop.get_info())
print(Laptop.check_stock(5))
print(Laptop.calculate_shipping_cost())
print(Laptop.calculate_warranty_extension(2))

print(Milk.get_info())
Milk.apply_discount(0.15)
print(Milk.get_info())
print(Milk.check_stock(5))
print(Milk.calculate_shipping_cost())
print(Milk.check_if_expired("2024-10-01"))