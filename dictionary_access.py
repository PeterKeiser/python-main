# dictionary access

from random import choice
food = choice(["cheese pizza", "quiche", "morning bun", "gummy bear", "tea cake"])
print(f"{food}")

backery_stock = {
    "almond croissant" : 12,
    "toffee cookie" : 3,
    "morning bun" : 1,
    "chocolate chunk cookie" : 9,
    "tea cake" : 25
}

if food in backery_stock.keys():
    print(f"food: {food}, backery stock is: {backery_stock[food]}")
else:
    print(f"food: {food} is not in the 'backery_stock' dictionary")



# if food in backery_stock:
#     print("{} left".format(backery_stock[food]))
# else:
#     print("We don't make that.")

# quantity = backery_stock.get(food)
# if quantity:
#     print("{} left".format(quantity))

