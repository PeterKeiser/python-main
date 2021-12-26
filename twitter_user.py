# twitter_user

users = [
    {"username": "samuel", "tweets": ["I love cake", "I love croisant"]},
    {"username": "katie", "tweets": ["I love my cat"]},
    {"username": "jeff", "tweets": [], "colour": "purple", },
    {"username": "bob123", "tweets": [], "num": 10, "colour": "teal" },
    {"username": "boddo_luvr", "tweets": ["Dogs are the best"]},
    {"username": "quital_gal", "tweets": []},
]

# print(sorted(users()))
# print(sorted(users, key=len))
# print(sorted(users, key=lambda user: user["username"]))
# print(sorted(users, key=lambda user: len(user["tweets"])))
# print(sorted(users, key=lambda user: len(user["tweets"]), reverse=True))



songs = [
    {"title": "happy birthday", "playcount": 1},
    {"title": "Survive", "playcount": 6},
    {"title": "YMCA", "playcount": 99},
    {"title": "Toxic", "playcount": 31},
]

# print(sorted(songs, key=lambda song: song["playcount"]))
print(sorted(songs, key=lambda song: song["playcount"], reverse=True))