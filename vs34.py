#to print fibnocci series using for loop.
n=int(input(" enter the n :"))
a=0
b=1
for i in range (1,n) :
    fib=a+b
    a=b
    b=fib
    print ( fib )