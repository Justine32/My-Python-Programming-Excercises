class Mysample:
    def hello(self,n):
        #print("hello "+n)
        self.name=n
    def print_name(self):
        print(self.name)
    
x=Mysample()
y=Mysample()
name="justine"
x.hello(name)
y.hello("kevin")
#Mysample.hello(x)  

x.print_name()
y.print_name()