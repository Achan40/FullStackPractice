# Objects
class Dog():

    # Class object attributes
    species = 'mammal'

    # Method that refers to the object itself
    def __init__(self, breed, name):
        # Attributes of the object
        self.breed = breed
        self.name = name

mydog = Dog(breed = 'lab', name = 'Django')

print(mydog.breed)
print(mydog.name)
print(mydog.species)

class Circle():

    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * Circle.pi

    # Set new radius with a method
    def set_radius(self, new_r):
        self.radius = new_r

myc = Circle(3)
myc.set_radius(999)
print(myc.area())

#Inheritance
class Animal():
    
    def __init__(self):
        print("Animal Created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")

class Dog(Animal):
    
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")

mydog = Dog()
mydog.whoAmI()
mydog.eat()

# Special Methods
class Book():

    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    # string special method
    def __str__(self):
        return "Title: {}, Author: {}, Pages: {}".format(self.title,self.author,self.pages)

    # length special method
    def __len__(self):
        return self.pages

    # delete special method
    def __del_(self):
        print("a book is destroyed")

b = Book("Python","Aaron",200)
print(b)
print(len(b))
del b

mylist = [1,2,3]
print(mylist)