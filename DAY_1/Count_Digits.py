n=int(input("Enter the Number : "))
a=0
while(n>0):
    if(n/10!=0):
        a=a+1
    n//=10
print("Number of Digits are : ",a)