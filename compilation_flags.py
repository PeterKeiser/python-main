# compilation_flags

import re

# pat = re.compile(r'^([a-z0-9_\.-]+)@([0-9a-z\.-]+)\.([a-z\.]{2,6})$')

pattern = re.compile(r"""
    ^([a-z0-9_\.-]+)    # first part of email
    @                   # singel @ sign
    ([0-9a-z\.-]+)      # email provider
    \.                  # sengle period
    ([a-z\.]{2,6})$     # com, org, net, etc.
""", re.VERBOSE| re.IGNORECASE)

match = pattern.search("ThomaS123@Yahoo.com")

print(match.group())
print(match.groups())