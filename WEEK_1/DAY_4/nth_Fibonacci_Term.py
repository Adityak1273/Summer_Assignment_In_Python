n=int(input("Enter the nth term : "))
num1=0
num2=1
for i in range(0,n):
    sum=num1+num2
    num1=num2
    num2=sum
print("The nth fibonacci series term of ",n," are : ",sum)    