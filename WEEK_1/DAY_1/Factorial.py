a=int(input("Enter the Factorial Number : "))
fac=1
if(a==0 and a==1):
    print("Factorial of ",a," is 1 ")
else:
    for i in range(1,a+1):
        fac*=i
    print("Factorial of ",a," is ",fac)