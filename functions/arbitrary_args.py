# The asterisk in the parameter name *toppings tells Python to make an empty tuple called toppings and pack whatever values it receives into this tuple. The print statement in the function body produces output showing that Python can handle a function call with one value and a call with three values. It treats the different calls similarly. Note that Python packs the arguments into a tuple.

def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)

    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings: ")
    for i in toppings:
        print("- "+i)

make_pizza('mushrooms', 'green peppers', 'extra cheese')
make_pizza('pepperoni')
