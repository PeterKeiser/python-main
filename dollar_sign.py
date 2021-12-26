# dollar sign

def count_dollar_sighns(word):
    count = 0
    for char in word:
        if char == "$":
            count +=1
    return count

print(count_dollar_sighns("$uper $ize $uper $ize"))