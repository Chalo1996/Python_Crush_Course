# EXERCISE ONE
class Restaurant():
    def __init__(self, name, cuisine_type) -> None:
        self.name = name
        self.type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("My restaurant name is "+self.name+" and my cuisine type is "+self.type)

    def open_restaurant(self):
        print("Welcome to our restaurant! Today we are open!")
    def show_num_served(self):
        print("The number of served customers is: "+str(self.number_served))

    def set_number_served(self, num):
        if num >= self.number_served:
            self.number_served = num
        else:
            print("No one has been served yet.")

    def increment_num_served(self, num_served):
        self.number_served += num_served

restaurant = Restaurant("Touche", "Italian Cuisine")
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.number_served = 50
restaurant.set_number_served(55)
restaurant.show_num_served()
restaurant.increment_num_served(50)
restaurant.show_num_served()

# EXERCISE TWO
# class User():
#     def __init__(self, first_name, last_name, **userinfo) -> None:
#         self.first = first_name
#         self.last = last_name
#         self.userinfo = userinfo

#     def user(self):
#         info = {}
#         info["first name"] = self.first
#         info["last name"] = self.last
#         print("\n",info["first name"]+", you are becoming a great programmer. Be a little patient!\n")

#         for k, v in self.userinfo.items():
#             info[k] = v

#         return info

#     def greet(self):
#         fullname = self.first+" "+self.last
#         print("Hello Mr. "+fullname)

# my_info = User("Emmanuel", "Chalo", age=25, location="Chala", educational_level="University")

# print(my_info.user())
# print("\n")
# my_info.greet()