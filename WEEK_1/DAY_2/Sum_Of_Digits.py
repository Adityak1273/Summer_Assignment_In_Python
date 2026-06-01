n=int(input("Enter the Number : "))
sum=0
b=n
while(b>0):
    a=b%10
    sum+=a
    b//=10
print("Sum of Digits are ",sum)