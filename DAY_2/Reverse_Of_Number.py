n=int(input("Enter the Number : "))
rev=0
b=n
while(b>0):
    a=b%10
    rev=rev*10+a
    b//=10
print("Reverse of ",n," is ",rev)    