# Python Code Challenges: Lists (Advanced)
# Jomer Cabrera

# 1. Every Three Numbers
def every_three_nums(start):
  return list(range(start, 101, 3))

print(every_three_nums(91))

# 2. Remove Middle
def remove_middle(lst, start, end):
  return lst[:start] + lst[end+1:]

print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

# 3. More Frequent Item
def more_frequent_item(lst, item1, item2):
  if lst.count(item1) >= lst.count(item2):
    return item1
  else:
    return item2
    
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))

# 4. Double Index
def double_index(lst, index):
  if len(lst) > index:
    lst[index] = lst[index] * 2
  return lst
print(double_index([3, 8, -10, 12], 2))

# 5. Middle Item
def middle_element(lst):
  lenth = len(lst)
  if lenth % 2 == 1:
    return lst[round(lenth / 2)]
  else:
    sum = (lst[round((lenth / 2) - 1)] + lst[round(lenth / 2)])
    return sum / 2

print(middle_element([5, 2, -10, -4, 4, 5]))