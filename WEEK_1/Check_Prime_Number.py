n=int(input("Enter the Number : "))
notprime=0
for i in range(2,n):
    if(n%i==0):
        notprime+=1
if(n==1 or n==0 or notprime==1):
    print(n," is not prime number.")
else:
    print(n," is prime number.")