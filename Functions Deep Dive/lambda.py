# Lambda Functions
# one-line shorthand for function

#Take for example, a function called `add_two()`:


def add_two(my_input):
  return my_input + 2


#The same function could be written as a lambda function:


add_two = lambda my_input: my_input + 2


#Using a conditional *if statement* in a lambda function, with syntax that looks like this:

check_if_A_grade = lambda grade: 'Got an A!' if grade >= 90 else 'Did not get an A.'
