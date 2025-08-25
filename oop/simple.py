"""
Simple file to demonstrate simple object-oriented programming 
"""
class Person:
    name: str
    age: int
    
    def __init__(self, name: str = "Stranger", age: int = None):
        self.name = name
        self.age = age

adam = Person("Adam")
eve = Person("Eve", 35)
stranger = Person()

def main():
    
