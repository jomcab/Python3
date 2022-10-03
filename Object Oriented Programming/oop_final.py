class School():
  def __init__(self, name, level, numberOfStudents):
    self.name = name
    self.level = level
    self.numberOfStudents = numberOfStudents

  def get_name(self):
    return self.name

  def get_level(self):
    return self.level

  def get_numberOfStudents(self):
    return self.numberOfStudents

  def set_numberOfStudents(self, num):
    self.numberOfStudents = num

  def __repr__(self):
    return "A {level} school named {name} with {numberOfStudents} students.".format(level=str(self.level), name=str(self.name), numberOfStudents=str(self.numberOfStudents))

a = School("Sample School", "Sample Level", 100)
print(a.get_numberOfStudents())
a.set_numberOfStudents(101)
print(a)

class PrimarySchool(School):
  def __init__(self, name, numberOfStudents, pickupPolicy):
    super().__init__(name, 'primary', numberOfStudents)
    self.pickupPolicy = pickupPolicy

  def getPickupPolicy(self):
    return self.pickupPolicy

  def __repr__(self):
    parentRepr = super().__repr__()
    return parentRepr + "\nThe pickup policy is " + self.pickupPolicy

b = PrimarySchool("Sample Primary School", 200, "Sample pickup policy")
print(b.get_numberOfStudents())
b.set_numberOfStudents(201)
print(b)

class HighSchool(School):
  def __init__(self, name, numberOfStudents, sportsTeams):
    super().__init__(name, 'high', numberOfStudents)
    self.sportsTeams = sportsTeams

  def getSportsTeams(self):
    return self.sportsTeams

  def __repr__(self):
    parentRepr = super().__repr__()
    return parentRepr + "\nSports Teams: " + self.sportsTeams

c = PrimarySchool("Sample Primary School", 300, "Sample pickup policy")
print(c.get_numberOfStudents())
c.set_numberOfStudents(301)
print(c)