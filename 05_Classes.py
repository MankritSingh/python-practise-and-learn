#class in python
class Dog:
    def __init__(self,age=1):#constructor   #def __init__(self,age=1): we can default values too like this   
        self.age=age
        
    def bark(self):#self mean the current object.We can think like for eg if we are working with 
    #object tommy so we can think tommy.x tommy.bark etc.
        print("Bhao Bhao")
    
    def potty(self):
        print("potty Kaun saaf karega?")


tommy=Dog(10)
tommy.bark()
tommy.potty()
print(tommy.age)
#______________________________________________________________________________________________________________#
class Person:
    def __init__(self,age=90):
        self.age=age
    def talk(self,mesg="Anab shanab"):#default value for function
        print(mesg)
    def tell_age(self):
        print(f"Hi my age is {self.age}")


person1=Person(20)
print(person1.age)
person1.talk("Hello sirji")
person1.talk()
person1.tell_age();
