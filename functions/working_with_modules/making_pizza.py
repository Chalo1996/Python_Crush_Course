import  pizza as p
#Here, I have imported the module pizza as an alias 'p' which allows for easy calling of the nodule's functions.

p.make_pizza(16, "pepperoni")
p.make_pizza(12, "mushrooms", "green peppers", "extra cheese")

# You can also import a specific function from a module. Here’s the general syntax for this approach: from module_name import function_name

#Example:
from pizza import make_pizza as mp
#Here, I have imported the function make_pizza from pizza instead of importing the entire module, as an alias 'mp' which allows for easy calling of the function.

mp(16, "pepperoni")
mp(12, "mushrooms", "green peppers", "extra cheese") #This piece code serves the same purpose as the first code above

# Importing All Functions in a Module
# You can tell Python to import every function in a module by using the asterisk ( * ) operator:
from pizza import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')