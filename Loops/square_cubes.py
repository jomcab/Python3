# Loops, break, continue, list comprehentions
# Jomer Cabrera

single_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
squares = []
for digit in single_digits:
  print(digit)
  squares.append(digit**2)

print("squares:", squares)

cubes = [num ** 3 for num in single_digits]
print("cubes:", cubes)