# One example of polymorphism is when different classes have the same method names
# We can use these methods even without knowing the which classes they belong
# In this example, 3 different classes will have their own definition of method say_id()
class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
    print("My id is {}.".format(self.id))

class Admin(Employee):
  def say_id(self):
    super().say_id()
    print("I am an admin.")

class Manager(Admin):
  def say_id(self):
    super().say_id()
    print("I am in charge!")

meeting = [Employee(), Admin(), Manager()]

for meet in meeting:
  meet.say_id()