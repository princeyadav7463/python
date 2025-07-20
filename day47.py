# dat 46 

# class and object in python
class Person:
  name = "Prince"
  occupation = "Software Developer"
  networth = 10
  def info(self):
    print(f"{self.name} is a {self.occupation}")  # self is used to access the instance variable

a= Person()
b= Person()
c= Person()
a.name = "Subham"
a.occupation = "Accountant"

b.name = "Nitika"
b.occupation = "HR"


# print(a.name,a.occupation)
a.info()
b.info()
c.info()
