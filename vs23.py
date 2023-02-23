# WAP to convert decimal num into binary.
n=int(input(" enter the decimal num : "))
while (n!=0) :
    bn=n%2
    print( bn )
    n=n//2
