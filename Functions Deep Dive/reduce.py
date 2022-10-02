letters = ['r', 'e', 'd', 'u', 'c', 'e']

# your code below:
from functools import reduce

# remember to import the reduce function
word = reduce(lambda x, y : x + y , letters)
# store the result of your reduce function in the variable word


# print word
print(word)