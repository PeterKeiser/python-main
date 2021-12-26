# fromkeys_exercise

# game_properties = ["current_score", "high_score", "number_of_lives", "items_in_inventory", "power_ups", "amo", "enemies_on_screen", "enemy_kills",
#                     "enemy_kills_stresks", "minutes_played", "notifications", "acheavements"]

# print(game_properties)

# initial_game_state = dict.fromkeys(["current_score", "high_score", "number_of_lives", "items_in_inventory", "power_ups", "amo", "enemies_on_screen", "enemy_kills",
#                     "enemy_kills_stresks", "minutes_played", "notifications", "acheavements"], [0])
# print(initial_game_state)

# initial_game_state = dict.fromkeys(game_properties, 0)

# print(initial_game_state)

# d = dict(a=1, b=2, c=3)
# print(d)

# d.pop("a")
# print(d)

instructor = {
    "name" : "Colt",
    "owns_dog" : True,
    "num_courses" : 4, 
    "favourite_language" : "Python",
    "is_hilarious" : True,
    44 : "my favourite number"
}
print(instructor)

# instructor.pop("owns_dog")
# print(instructor)

instructor.popitem()
print(instructor)



