# substitution_basics

import re
import typing_extensions

text = "Last night Mrs. Daisy and Mr. White murdered Ms. Chow."

pattern = re.compile(r'(Mrs\.|Mr\.|Ms\.) ([a-z])[a-z]+', re.IGNORECASE)
# print(pattern.findall(text))
result = pattern.sub("\g<1> \g<2>", text)
print(result)




