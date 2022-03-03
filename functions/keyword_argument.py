# Here, a default value of 'john' has been passed to the pet_name parameter. If a default argument is not provided in the function call, this value is treated as the default argument.

def describe_pet(pet_type, pet_name="john"):
    """Display Information about a Pet."""
    print("\nI have a "+pet_type.title()+".")
    print("My "+pet_type+"'s name is "+pet_name.title()+".")

describe_pet(pet_type='hamster',)
describe_pet(pet_type = "elephant", pet_name="julie")