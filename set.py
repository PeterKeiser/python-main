# set

# s = {1, 4, 5}
# print(s)

# s2 = set({2,3,6})
# print(s2)


# s3 = set({6, 7, 8, 8, 8, 9, "b", 23.4445}) 
# print(s3)

# for num in s3:
#     print(num)

cities = ["Los Angeles", "Boulder", "Kyoto", "Florence", "Santiago", "Los Angeles", "Shanghai", "Boulder",
            "San Francisco", "Oslo", "Tokyo"]
print(cities)

# print(len(set(cities)))

print(set(cities))
# print(list(set(cities)))

cities2 = set(cities)
cities2.add("Vancouver")
print(cities2)

# cities2.add("Kyoto")
# print(cities2)

# cities2.remove("Moscow")
# print(cities2)

# cities2.remove("Oslo")
# print(cities2)

# cities2.discard("Florence")
# print(cities2)

# cities2.discard("Moscow")
# print(cities2)

another_cities2 = cities2.copy()
print(another_cities2)