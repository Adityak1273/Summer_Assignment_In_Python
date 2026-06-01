n=int(input("Enter the Number : "))
pro=1
b=n
while(b>0):
    a=b%10
    pro*=a
    b//=10
print("Product of ",n," is ",pro)    