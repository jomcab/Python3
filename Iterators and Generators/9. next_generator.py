def student_standing_generator():
  student_standings = ['Freshman','Senior', 'Junior', 'Freshman']
  for ss in student_standings:
    if ss == 'Freshman':
      yield 500
  
standing_values = student_standing_generator()
print(next(standing_values))
print(next(standing_values))
print(next(standing_values))