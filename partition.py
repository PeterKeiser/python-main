# partition

# lst = [1, "g", "", 0, False]
# # func = 1**2
# def func(x):
#     if x:
#         return True
#     else:
#         return False

# def partition(collection2, fn):
#     print(collection2)
#     print(fn)
#     truthy_list=[]
#     falsy_list=[]
#     for n in collection2:
#         if fn(n):
#     # if (n % 2 == 0 for n in collection2):
#             truthy_list.append(n)
#         else:
#             falsy_list.append(n)
#     return[truthy_list, falsy_list]

# a = partition(lst, func)
# print(a)

# print(partition([1, "g", "", 0, False], ))

def func(x):
    if x:
        return True
    else:
        return False

def partition(collection2, fn):
    print(collection2)
    print(fn)
    truthy_list=[]
    falsy_list=[]
    for n in collection2:
        if fn(n):
            truthy_list.append(n)
        else:
            falsy_list.append(n)
    return[truthy_list, falsy_list]


print(partition([1, "g", "", 0, False],func))


















# #############################################################################
# def partition(lst, fn):
#     return [[n for n in lst if fn(n)],[n for n in lst if not fn(n)]]

# print(partition([1, "g", "", 0, False], 1**1))
 
# #############################################################################
# def partition(lst, callback):
#     return[[lst.pop(lst.index(i)) for i in lst if callback(i)], lst]

