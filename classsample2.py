class TeamMebers:
    year=2020                              #global 
    def __init__(self,name,age,place):     #__init__ [constructor]
        self.name=name
        self.age=age
        self.place=place
    
    def add_age(self):
        self.age=self.age+1

    def relocate(self,place):
        self.place=place


    def display(self):
        print("Year  : "+str(TeamMebers.year))
        print("Name  : "+self.name)
        print("age   : "+str(self.age))
        print("Place : "+self.place)
    
    @classmethod                          #shared to all memory space
    def add_year(cls):
        cls.year=cls.year+1
        print(cls.year)
    @staticmethod                         # used without affecting other code  
    def display_welcome():
        print("Welcome")


x=TeamMebers("Justine",21,"kochi")
y=TeamMebers("kevin",28,"Kottayam")

x.display()
y.display()
print("---------------------------------------")
TeamMebers.year=TeamMebers.year+1
x.add_age()
y.add_age()


x.display()
y.display()
print("---------------------------------------")
TeamMebers.add_year()

x.add_age()
y.add_age()
x.relocate("delhi")
y.relocate("goa")
x.display()
y.display()

