# day 47
class Person:
  def __init__(self, n, o):
    print("Hey I am a person")
    self.name = n
    self.occ = o

  def info(self):
    print(f"{self.name} is a {self.occ}")

a = Person("Prince","Developer")
b = Person("Soni", "HR")
a.info()
b.info()
