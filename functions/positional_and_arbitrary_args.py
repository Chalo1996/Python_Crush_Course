# If you want a function to accept several different kinds of arguments, the parameter that accepts an arbitrary number of arguments must be placed last in the function definition. Python matches positional and keyword arguments first and then collects any remaining arguments in the final parameter. For example, if the function needs to take in a size for the pizza, that parameter must come before the parameter *toppings :

def make_pizza(size, *toppings):
    print("\nMaking a "+str(size)+"-inch Pizza with the following toppings: ")

    for i in toppings:
        print("- "+i)

make_pizza(16, "pepperoni")
make_pizza(12, "mushrooms", "green peppers", "extra cheese")