class Car:
    def __init__(self, brand):
        self.brand = brand  # Instance variable
        self.model = 'Corola'  # Instance variable

    def display(self):
        print(f"This car is a {self.brand} {self.model}")

# Creating objects (instances)
car1 = Car("Toyota")
car2 = Car("Tesla")

car1.display()  # Output: This car is a Toyota Corolla
car2.display()  # Output: This car is a Tesla Model 3
