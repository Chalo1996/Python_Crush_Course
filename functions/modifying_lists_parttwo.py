def print_media(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: "+current_design)

        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that have been printed"""
    print("The following models have been printed: ")

    for i in completed_models:
        print(i)

unprinted_media = (["iPhone case", "robot pendant", "dodecahedron"])

completed_models = []

print_media(unprinted_media, completed_models)
show_completed_models(completed_models)

# The slice notation [:] makes a copy of the list to send to the function. If we didn’t want to empty the list of unprinted designs in print_models.py, we could call print_models() like this:

# print_media(unprinted_media[:], completed_models)