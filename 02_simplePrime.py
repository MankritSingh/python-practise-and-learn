print("Simple Prime Number Verifier")
num=int(input("Enter a postive number"))
counter=0
if num>1:
    
    for i in range(num):
        if num%(i+1)==0:
            counter+=1
        
elif num==0 or num==1:
    counter=0
else:
    print("Wrong Input.Enter a positive number")

if counter==2:
    print("\nPrime Number")
else:
    print("\nNot Prime")
