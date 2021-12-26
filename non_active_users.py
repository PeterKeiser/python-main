# non_active_users

users = [
    {"username":"samuel", "tweets": ["I love cake", "I love croisant"]},
    {"username":"katie", "tweets": ["I love my cat"]},
    {"username":"jeff", "tweets": []},
    {"username":"bob123", "tweets": []},
    {"username":"boggo_luvr", "tweets": ["dogs are the best"]},
    {"username":"gal", "tweets": []}
]

# inactive_user = list(filter( lambda u: len(u["tweets"]) == 0, users))
# inactive_user2 = list(filter( lambda u: u["tweets"], users))
# inactive_user3 = list(filter( lambda u: not u["tweets"], users))

# print(inactive_user)
# print(inactive_user2)
# print(inactive_user3)


# inacive_userb = list(map(lambda user: user["username"], 
#                         filter(lambda u: not u["tweets"], users)))

# print(inacive_userb)

inactive_userc= [user for user in users if not user["tweets"]]
inactive_userd= [user["username"].upper() for user in users if not user["tweets"]]

print(inactive_userc)
print(inactive_userd)



