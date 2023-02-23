 # to print fibnocci serise of given number.
n=int(input(" enter the n : "))
i=1
a=0
b=1
while i<=n :
    fib=a+b
    a=b
    b=fib
    i+=1
    print ( fib )