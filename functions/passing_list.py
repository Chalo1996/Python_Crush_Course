def greet_user(names):
    """Print a Simple Greeting to every user in the List"""
    for name in names:
        msg = "Hello, "+name.title()+"!"
        print(msg)

usernames = greet_user['emmanuel', 'chalo', 'martin']