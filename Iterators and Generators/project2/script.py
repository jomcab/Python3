from roster import student_roster 
from classroom_organizer import ClassroomOrganizer
import itertools

# Working with iterator
student_roster_iterator = iter(student_roster)
print(next(student_roster_iterator))
print(next(student_roster_iterator))
print(next(student_roster_iterator))
print(next(student_roster_iterator))
print(next(student_roster_iterator))
print(next(student_roster_iterator))
print(next(student_roster_iterator))
print(next(student_roster_iterator))
print(next(student_roster_iterator))
print(next(student_roster_iterator))

class_org = ClassroomOrganizer()
print(class_org.get_sitting_arrangement())

# Math and Science / 4 students per table
studs_math = class_org.get_students_with_subject("Math")
studs_science = class_org.get_students_with_subject("Science")
all_studs = itertools.chain(studs_math, studs_science)
stud_combi = list(itertools.combinations(all_studs, 4))
print(stud_combi)