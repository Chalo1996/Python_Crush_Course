from car import *

# INHERITANCE

# When modeling something from the real world in code, you may find that you’re adding more and more detail to a class. You’ll find that you have a growing list of attributes and methods and that your files are becoming lengthy. In these situations, you might recognize that part of one class can be written as a separate class. You can break your large class into smaller classes that work together. For example, if we continue adding detail to the ElectricCar class, we might notice that we’re adding many attributes and methods specific to the car’s battery. When we see this happening, we can stop and move those attributes and methods to a separate class called Battery. Then we can use a Battery instance as an attribute in the ElectricCar class:

class Battery():
    """
    A simple attempt to model a battery for an electric car.
    """
    def __init__(self, battery_size=70) -> None:
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a "+str(self.battery_size)+" kWh battery")


    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        msg = "This car can go approximately "+str(range)+ " miles on full charge."
        print(msg)

battery = Battery()

# The super() function at is a special function that helps Python make connections between the parent and child class. This line tells Python to call the __init__() method from ElectricCar ’s parent class, which gives an ElectricCar instance all the attributes of its parent class. The name super comes from a convention of calling the parent class a superclass and the child class a subclass.

class ElectricCar(Car):
    def __init__(self, make, model, year) -> None:
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery=Battery()

my_tesla = ElectricCar("tesla", "model s", 2016)
print(my_tesla.describe_car())
my_tesla.read_odometer()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

my_beatle = Car("volkswagen", "beetle", 2016)
my_beatle.describe_car()