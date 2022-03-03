# Sometimes you’ll want to accept an arbitrary number of arguments, but you won’t know ahead of time what kind of information will be passed to the function. In this case, you can write functions that accept as many key-value pairs as the calling statement provides. One example involves building user profiles: you know you’ll get information about a user, but you’re not sure what kind of information you’ll receive. The function build_profile() in the following example always takes in a first and last name, but it accepts an arbitrary number of keyword arguments as well:


def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""

    profile = {}
    profile["first_name"] = first
    profile["last_name"] = last

    for k, v in user_info.items():
        profile[k] = v
    return profile

user_info = build_profile("albert", "einstein", location = "princeton", field = "physics")

print(user_info)