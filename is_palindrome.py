# is_palindrome

def is_palindrome(string):
    stripped = string.replace(" ", "").lower()
    return stripped == stripped[::-1]

print(is_palindrome("a man a plan a canal Panama"))
print(is_palindrome("anna"))


