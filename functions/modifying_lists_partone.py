unprinted_designs = ["iPhone case", "robot pendant", "dodecahedron"]

printed_designs = []

while unprinted_designs:
    new_designs = unprinted_designs.pop()

    print("Printing model: "+new_designs)
    printed_designs.append(new_designs)

print("The current models have been completed: ")

for i in printed_designs:
    print(i)

