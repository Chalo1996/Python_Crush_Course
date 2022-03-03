def describe_pet(pet_type, pet_name):
    """Display Information about a Pet."""
    print("\nI have a "+pet_type.title()+".")
    print("My "+pet_type+"'s name is "+pet_name.title()+".")

describe_pet("hamster", "harry")
describe_pet("dog", "willie")