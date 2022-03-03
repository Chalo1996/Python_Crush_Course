# Setting a Default Value for an Attribute.
# Every attribute in a class needs an initial value, even if that value is 0 or an empty string. In some cases, such as when setting a default value, it makes sense to specify this initial value in the body of the __init__() method; if you do this for an attribute, you don’t have to include a parameter for that attribute. Let’s add an attribute called odometer_reading that always starts with a value of 0. We’ll also add a method read_odometer() that helps us read each car’s odometer:

class Car:
    def __init__(self, make, model, year) -> None:
        self.make = make
        self.year = year
        self.model = model
        self.odometer_reading=0

    def describe_car(self):
        return str(self.year)+" "+self.make+" "+self.model

    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back the odometer.")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

my_car = Car("audi", "a4", 2016)
print(my_car.describe_car())
my_car.read_odometer()

# Modifying an Attribute’s Value Directly 
# The simplest way to modify the value of an attribute is to access the attribute directly through an instance. Here we set the odometer reading to 23 directly:

my_car.odometer_reading = 23
my_car.read_odometer()

# Modifying an Attribute’s Value Through a Method
# It can be helpful to have methods that update certain attributes for you. Instead of accessing the attribute directly, you pass the new value to a method that handles the updating internally. Here’s an example showing a method called update_odometer():

def update_odometer(self, mileage):
    if mileage >= self.odometer_reading:
        self.odometer_reading = mileage
    else:
        print("You can't roll back the odometer.")

my_car.update_odometer(23)

# Incrementing an Attribute’s Value Through a Method
# Sometimes you’ll want to increment an attribute’s value by a certain amount rather than set an entirely new value. Say we buy a used car and put 100 miles on it between the time we buy it and the time we register it. Here’s a method that allows us to pass this incremental amount and add that value to the odometer reading:

def increment_odometer(self, miles):
    self.odometer_reading += miles

used_car = Car("Subaru", "outback", 2013)
print(used_car.describe_car())

used_car.update_odometer(23500)
used_car.read_odometer()

used_car.increment_odometer(100)
used_car.read_odometer()