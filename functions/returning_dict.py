#You can pass an arbitrary argument in the function definition as shown below by providing a keword argument followed by an empty string.

def build_person(fname, lname, age = ""):
    """Return a dictionary of information about a person"""
    person = {"First Name":fname, "Last Name":lname}

    if age:
        person["age"] = age

    return person

musician = build_person("Emmanuel", "Chalo", 25)
musician = build_person("David", "Mutune")
print(musician)