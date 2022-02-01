def list():
    print('')
    mylist=[1,2,"Hello",[1,2]]  #list can hold any data type and is mutable
    print("mylist:[",end='')
    for val in mylist:  #priniting list
        print(val,end=',')
    print("]")
    print("Accessing index mylist[3][0]:",mylist[3][0])
    print("Negative indexing mylist[-1]:",mylist[-1]) #negative indexing start from the right side from zero
    print("Slicing [1:3]:",mylist[1:3])  #slicing the last element is non inclusive
    mylist.append(4) #add element at end

def tuple():
    print('')
    mytuple=(1,2,"Hello",[1,2]) #tuple is similar to list but  we cannot change the elements of a tuple once it is assigned
    print("mytuple:(",end='')
    for val in mytuple:  #priniting tuple
        print(val,end=',')
    print(")")
    print("Accessing index mytuple[3][1]:",mytuple[3][1])
    print("Negatvie indexing mytuple[-2]:",mytuple[-2]) #negative indexing start from the right side from zero
    print("Slicing [:4]:",mytuple[:4])  #slicing the last element is non inclusive
#in tuples we cannot use functions like append,insert or other such function as tuple is immutable
#we can change value of mutable element in the tuple like a tuple in list and we can also reassign the entire tuple

def mystring():
    print("")
    str1="Hello"
    str2="World"
    print("str1:",str1)
    print("str2:",str2)
    print("str1[2]:",str1[2]) #we can access character of string like character array
    print("Slicing str1[:3]:",str1[:3],)
    str3=str1+str2
    print("str3=str1+str2:",str3)

def set():
    print("")
    myset={1,2,3,5} #a set is unordered.a set will not have duplicate values.we can perform the set operations available in maths
    myset2={2,3,7,8}               #we can use with set datatype.A set can immutable data like tuple,string,int etc
    print("myset:{",end='')
    for val in myset:  #priniting tuple
        print(val,end=',')
    print("}") 
    print("myset2:{",end='')
    for val in myset2:  #priniting tuple
        print(val,end=',')
    print("}") 
    print("myset.add(4):",myset.add(4))
    print("myset.remove(2):",myset.remove(2)) 
    print("myset:{",end='')
    for val in myset:  #priniting tuple
        print(val,end=',')
    print("}") 
    print("set operations")
    print("myset union myset2:",(myset|myset2))
    print("myset intersection myset2:",(myset&myset2))
    print("myset difference(minus) myset2:",(myset-myset2))
    print("myset symmetric difference(In A and In B but not in A&B) myset2:",(myset^myset2))



list()
tuple()
mystring()
set()
