# Setting a Default Value for an Attribute.
# Every attribute in a class needs an initial value, even if that value is 0 or an empty string. In some cases, such as when setting a default value, it makes sense to specify this initial value in the body of the __init__() method; if you do this for an attribute, you don’t have to include a parameter for that attribute. Let’s add an attribute called odometer_reading that always starts with a value of 0. We’ll also add a method read_odometer() that helps us read each car’s odometer:

class Car:
    def __init__(self, make, model, year) -> None:
        self.make = make
        self.year = year
        self.model = model
        self.odometer_reading = 0

    def describe_car(self):
        return str(self.year)+" "+self.make+" "+self.model

    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" miles on it.")

my_car = Car("audi", "a4", 2016)
print(my_car.describe_car())
my_car.read_odometer()