# censor

import re

def censor(input):
    censor_regex = re.compile(r'\bfrack\w*\b', re.IGNORECASE)
    return censor_regex.sub("CENSORED", input)



print(censor("Frack you!"))
print(censor("I hope you fracking die!"))
print(censor("you fracking Frack"))


