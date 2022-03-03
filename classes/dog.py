class  Dog:
    """A simple attempt to model a dog."""
    def __init__(self, name, age) -> None:
        """Initialize name and age attributes."""
        self.name = name
        self.age = age


    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title()+" is now sitting.")

    def roll_over(self):
        """Simulate a dog rolling over in response to a command."""
        print(self.name.title()+" is rolled over.")

my_dog = Dog("Simba", 8)
print("My dog's name is "+my_dog.name.title())
print(my_dog.name.title()+" is "+str(my_dog.age)+" years old.")
my_dog.sit()
my_dog.roll_over()
print("\n")

# We can create as many instances as we want. For example, lets create another dog called 'your_dog'
your_dog = Dog("lucy", 6)
print("Your dog's name is "+your_dog.name.title())
print(your_dog.name.title()+" is "+str(your_dog.age)+" years old.")
your_dog.sit()
your_dog.roll_over()

# The __init__() Method
# All the functions in this class are methods. When a function is used inside a class it is called a method.