# dog.py
class Dog:
    def __init__(self, name):
        self.name = name
        print("dog initialized!")

my_dog = Dog("Rex")
# Adding the "breed" property on the fly
my_dog.name = "name:tommy "
my_dog.age = "age:7 "
my_dog.cc = "coat color:grey "
# will print "SuperDog"
print(my_dog.name)
print(my_dog.age)

print(my_dog.cc)

