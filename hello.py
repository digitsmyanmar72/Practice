class Person:
  def __init__(self, fname, lname,gra):
    self.firstname = fname
    self.lastname = lname
    self.grau = gra

  def printname(self):
    print(self.firstname, self.lastname,self.grau)

obj = Person("nay","aung",15)
obj.printname()