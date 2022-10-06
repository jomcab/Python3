from roster import student_roster
import itertools

class ClassroomOrganizer:
  def __init__(self):
    self.sorted_names = self._sort_alphabetically(student_roster)

  def __iter__(self):
    self.count = 0
    return self

  def __next__(self):
    if self.count < len(self.sorted_names):
      index = self.count
      self.count += 1
      return self.sorted_names[index]
    else:
      raise StopIteration

  def _sort_alphabetically(self,students):
    names = []
    for student_info in students:
      name = student_info['name']
      names.append(name)
    return sorted(names)

  def get_students_with_subject(self, subject):
    selected_students = []
    for student in student_roster:
      if student['favorite_subject'] == subject:
        selected_students.append((student['name'], subject))
    return selected_students

  def get_sitting_arrangement(self):
    return list(itertools.combinations(self.sorted_names, 2))


classrom_organizer = ClassroomOrganizer()
for stud in classrom_organizer:
  print(stud)