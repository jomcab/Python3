global_variable = 'global'

print(' -- Local and global Namespaces with empty script -- \n')
# Checkpoint 1:
print(locals())
print("globals:", globals())

# Checkpoint 2:
def divide(num1, num2):
  result = num1 / num2
  print(locals())
  return result
# Checkpoint 3:
def multiply(num1, num2):
  product = num1 * num2
  print(locals())
  return product

print(' \n -- Local Namespace for divide -- \n')
# Checkpoint 4:
divide(3, 4)

print(' \n -- Local Namespace for multiply -- \n')
# Checkpoint 5:
multiply(4, 50)

print(' \n -- Local Namespace final -- \n')
# Checkpoint 6:
print(locals())