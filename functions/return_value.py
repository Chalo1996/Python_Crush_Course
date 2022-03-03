def get_formatted_name(fname, lname):
    """Return a full name neatly formatted."""
    full_name = fname+" "+lname
    return full_name
    

while True:
    print("\nPlease Tell Me your Name: ")
    first_name = input("First Name: ")
    if first_name == "q":
        break

    last_name = input("Last Name: ")
    if last_name == "q":
        break

    musician = get_formatted_name(first_name, last_name)
    print("\nHello, "+musician+".")
