class myclass:
  def __init__(self,fname,lname):
    self.firstname = fname
    self.lastname = lname
  def myfunc(self):
    print(self.firstname,self.lastname)

myobj = myclass ("nay","aung")
class son(myclass):
  pass

sonobj = son("win","aye")
sonobj.myfunc()