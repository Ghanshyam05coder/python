#to calculate add, sub, multiply, devide of given condition 1-add,2-sub,3-multiply,4-devide.
n=int(input(" enter the option : "))
a=int(input(" enter the a : "))
b=int(input(" enter the b : "))
if(n==1):
    print(a+b)
elif(n==2):
    print(a-b)
elif(n==3):
    print(a*b)
elif(n==4):
    print(a/b)
else:
    print("wrong choice")                