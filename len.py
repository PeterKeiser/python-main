# len

# len("awesome")
# print(len("awesome"))

# print(len((1, 2, 3, 4)))
# print(len([1, 2, 3, 4]))
# print(len(range(0,10)))

# print(len({1, 2, 3, 4}))
# print(len({"a": 1, "b": 2, "c": 2}))

# from types import DynamicClassAttribute


# print("hello".__len__())

# print([1, 2, 3, 4,5 ,6].__len__())


# class SpecialList:

#     def __init__(self, data):
#       self.__data=data 

#     def __len__(self):
#         return 50

# l1 = SpecialList([1,40,30,100])
# l2 = SpecialList([])

# print(len(l1))
# print(len(l2))





class SpecialList:

    def __init__(self, data):
      self.__data=data 

    def __len__(self):
        return self.__data.__len__() // 2

l1 = SpecialList([1,40,30,100, 1, 2, 3, 4])
l2 = SpecialList([1, 2, 3, 4, 5])

print(len(l1))
print(len(l2))






