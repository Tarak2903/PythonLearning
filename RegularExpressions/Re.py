import re

price = "Price: $1894.50"

expression= 'Price: (\\$[0-9\\.]*[0-9])'

matches=re.search(expression,price)

print(matches.group(1))

