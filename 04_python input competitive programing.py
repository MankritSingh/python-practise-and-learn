#taking input in python for competitive coding

#Important:In python a new line is a new input therefore when input with space is given we have to use these methods

#1st way:when the number of input is less like 3 or 4
#find sum of 3 element
a,b,c=map(string,input().split())
print(a+b+c)

#2nd way:when we have to take array input for n element we take input in list ie take one input and split it in list
#For string
all=[i for i in input().split()]# this is called List Comprehension
print(all)
#For Integer
all=[int(i) for i in input().split()]# this is called List Comprehension
print(all)
