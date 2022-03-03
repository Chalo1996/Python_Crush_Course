# We can make an argument Optional so that people will provide additional information if they want to. For example, middle name is an  optional in the following code. To make the middle name optional, we can give the middle_name argument an empty default value and ignore the argument unless the user provides a value.

def get_formatted_name(fname, lname, middle_name = ''):
    """Return a full name neatly formatted."""
    if middle_name:
        full_name = fname+" "+middle_name+" "+lname

    else:
        full_name = fname+" "+lname

    return full_name.title()

musician = get_formatted_name("emmnauel", "chalo")
print(musician)

musician = get_formatted_name("david", "mutune", "kimengu")
print(musician)