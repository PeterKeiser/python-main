# kwargs_exercise

def combine_words(word, **kwargs):
    if "prefix" in kwargs and word:
        return kwargs["prefix"] + word
    elif "suffix" in kwargs and word:
        return word + kwargs['suffix']
    else:
        return word

print(combine_words("child"))
print(combine_words("child", prefix = "man"))
print(combine_words("child", suffix = "ish"))



