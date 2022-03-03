def make_pizza(size, *toppings):
    print("\nMaking a "+str(size)+"-inch pizza with the following toppings: ")

    for i in toppings:
        print("- "+i)