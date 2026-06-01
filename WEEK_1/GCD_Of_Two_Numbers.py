first=int(input("Enter the first number : "))
second=int(input("Enter the second number : "))
add=0
n=0
m=0
if(first>second):
    n=first
    m=second
elif(first<second):
    n=second
    m=first
else:
    n=first
    m=second        
for i in range(1,n):
    if(n%i==0 and m%i==0):
        add=i
print("GCD of first number ",first," and second number ",second," are : ",add)   
