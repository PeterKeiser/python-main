# for loop exercise

x = 0
for num in range(10,21,2):
    # print(num+1)
    x = x + (num+1)
print(x)

x = 0
for n in range(10,22):
    if n % 2 != 0:
        x += n
print(x)