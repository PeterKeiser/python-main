# nested_list

# nested_list = [1, 2, 3],[4, 5, 6], [7, 8, 9]

# print(nested_list)

# for l in nested_list:
#     for val in l:
#         print(val)

# coords = [[10.423, 9.132], [37.212, -14.092], [21.367, 32.572]]
# print(coords)

# for loc in coords:
#     print(loc)

# for loc in coords:
#     for coord in loc:
#         print(coord)

# [[print(val) for val in l] for l in coords]

# board = [[num for num in range(1,4) ] for val in range(1,4)] 
# print(board)

# print([["X" if num % 2 != 0 else "O" for num in range(1,4)] for val in range(1,4)])

# print([["*" for val in range (1,4)] for num in range(1,4)])



# answer =([[l for l in range(3)] for num in range(3)])
# print(answer)

answer = [[i for i in range(0,10)] for num in range(0,10)]
print(answer)