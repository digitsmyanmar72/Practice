class myclass:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
        
    def myfunction(self):
        print (self.firstname,self.lastname)
        
myobj = myclass("nay","aung")
print(myobj.firstname)
myobj.myfunction()