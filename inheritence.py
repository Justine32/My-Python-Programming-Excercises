class BaseClass:
    def __init__(self):
        print("Baseclass init")

    def set_name(self,name):
        self.name=name


class SubClass(BaseClass):
    def __init__(self):
        print("Subclass init")

    def welcome(self):
        print("welcome")
    
    def display_name(self):
        print("Name "+self.name)


x=BaseClass()
y=SubClass()

#x.set_name("Justine")
y.welcome()
y.set_name("Justine")
y.display_name()