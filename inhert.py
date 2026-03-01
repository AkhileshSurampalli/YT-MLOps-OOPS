# Simple inheritance

# Base class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound")


# Derived class
class Dog(Animal):

    def __init__(self):
        self.behaviour = "firendly"

    def speak(self):
        print(f"Buddy barks. He is very {self.behaviour}")

# Create an instance of Animal
animal = Animal("Generic Animal")
animal.speak()

# Create an instance of Dog
dog = Dog()
dog.speak()