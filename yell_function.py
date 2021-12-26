# yell_function

def yell(word):
    return f"{word.upper()} !"

print(yell("go away"))
############################################################
def yell(word):
    return "{}!".format(word.upper())

print(yell("go away"))