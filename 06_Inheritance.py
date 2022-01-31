class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):#This is how we inherit the mammal class
    pass#pass is placeholder for future code.here we use as python doesnt like empty class


class Cat(Mammal):
    pass


mammal1=Mammal()
print("From Mammal object:",end=" ")
mammal1.walk()

doggy=Dog()
print("From Dog object:",end=" ")
doggy.walk()

catty=Cat()
print("From Cat object:",end=" ")
catty.walk()
