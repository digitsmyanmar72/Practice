class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)
    
x = Person("nay","aung")

class student(Person):
  pass

y = student("yun","yu")
y.printname()