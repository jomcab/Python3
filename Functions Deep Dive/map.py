grade_list = [3.5, 3.7, 2.6, 95, 87]

# Your code below:
grades_100scale = map(lambda input : input*25 if input<=4 else input, grade_list)
# assign the result of your map function to the variable grades_100scale

# convert grades_100scale to a list and save it as updated_grade_list 
updated_grade_list = list(grades_100scale)
# print updated_grade_list
print(updated_grade_list)