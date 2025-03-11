class Mammal:
    def walk(self):
        print("Can walk")
        
    def talk(self):
        print("Can't talk")
        
class Dog(Mammal):
    pass

class Cat(Mammal):
    pass


dog1 = Dog()
dog1.walk()
dog1.talk()