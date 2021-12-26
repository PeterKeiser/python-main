# first_zip

# first_zip = zip([1, 2, 3],[4, 5, 6])

# # print(list(first_zip))
# print(dict(first_zip))


# nums1 = [1, 2, 3, 4, 5]
# nums2 = [6, 7, 8, 9, 10]

# print(list(zip(nums1, nums2)))

# words = ["hi", "lol", "haha", ":o)"]

# print(list(zip(words, nums1, nums2)))


# five_by_two = [(0,1), (1,2), (2,3), (3, 4), (4, 5)]
# print(five_by_two)

# print(list(zip(*five_by_two)))



# midterms = [80, 91, 78]
# finals = [98, 89, 53]
# students = ["dan", "ang", "kate"]

# # result should look like: 
# {"dan": 98, "ang": 91, "kate" : 78}

# final_grades = (dict(zip(students, max(midterms, finals))))
# print(final_grades)


# midterms = [80, 91, 78]
# finals = [98, 89, 53]
# students = ["dan", "ang", "kate"]

# print([max(pair) for pair in zip(midterms, finals)])
# print(dict(zip(students, [max(pair) for pair in zip(midterms, finals)])))


# midterms = [80, 91, 78]
# finals = [98, 89, 53]
# students = ["dan", "ang", "kate"]

# print({t[0]: max(t[1], t[2]) for t in zip(students, midterms, finals)})

# midterms = [80, 91, 78]
# finals = [98, 89, 53]
# students = ["dan", "ang", "kate"]

# final_grades = dict(
#     zip(
#         students, 
#         map(
#             lambda pair: max(pair),
#             zip(midterms, finals)
#         )
#     )
# )
# print(final_grades)


midterms = [80, 91, 78]
finals = [98, 89, 53]
students = ["dan", "ang", "kate"]

average_final_grades = dict(
    zip(
        students, 
        map(
            lambda pair: ((pair[0]+pair[1])/2),
            zip(midterms, finals)
        )
    )
)
print(average_final_grades)








