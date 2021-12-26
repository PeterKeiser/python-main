# define_class

# # class User:
# #     pass
# # user1 = User()
# # user2 = User()
# # user3 = User()
# # user4 = User()
# # print(type(user1))
# # print(user1)
# # print(user2)


# # class User:
# #     def __init__(self):
# #         print("A new user has been made!")
    
# # user1 = User()
# # user2 = User()


# # class User:
# #     def __init__(self, first):
# #         self.name = first
       
    
# # user1 = User("Joe")
# # user2 = User("Blanca")

# # # instance.attribute_name
# # print(user1.name)
# # print(user2.name)



# from sys import modules
# from types import ModuleType


# class User:
#     def __init__(self, first, last, age):
#         self.first = first
#         self.last = last
#         self.age = age
       
    
# user1 = User("Joe", "Smith", 68)
# user2 = User("Blanca", "Lopez", 41)

# # instance.attribute_name
# print(user1.first, user1.last)
# print(user2.first, user2.last)



# class Vehicle:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

# vehicle1 = Vehicle("Tesla", "Model S", 2021)
# vehicle2 = Vehicle("TEsla", "Model 3", 2020)

# print(vehicle1.make, vehicle1.model, vehicle1.year)
# print(vehicle2.make, vehicle2.model, vehicle2.year)




class User:

    active_users = 0

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1

    def logout(self):
        User.active_users -= 1
        return f"{self.first} has logged out"
       
    def full_name(self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]}. {self.last[0]}."

    def likes(self, thing):
        return f"{self.first} likes {thing}"

    def is_senior(self):
        return self.age >= 65

    def birthday(self):
        self.age += 1
        return f"Happy {self.age}-th Birthday, {self.first}"


print(User.active_users)
user1 = User("Joe", "Smith", 68)
user2 = User("Blanca", "Lopez", 41)
# print(user2.full_name())
# print(user2.initials())
# print(user1.likes("Ice Cream"))
# print(user2.likes("Chips"))
# print(user1.initials())
# print(user1.is_senior())
# print(user2.is_senior())
# print(user1.birthday())
# print(user2.birthday())
print(User.active_users)
print(user2.logout())
print(User.active_users)







