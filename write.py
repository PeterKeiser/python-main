# write

# with open("haiku.txt", "w") as file:
#     file.write("Writing files is great\n")
#     file.write("Here's another line of test\n")
#     file.write("Closing now, goodbye!")

# with open("haiku.txt", "w") as file:
#     file.write("Here's one more  haiku\n")
#     file.write("What about the older one?\n")
#     file.write("Let's go check it out")

# with open("lol.txt", "w") as file:
#     file.write("haha" * 10000)
   
# with open("haiku.txt", "a") as file:
#     file.seek(0)
#     file.write(";o))\n")
    
 
with open("haiku.txt", "r+") as file:
    file.write(";o)))")
    file.seek(10)
    file.write(";o(((")

    





  