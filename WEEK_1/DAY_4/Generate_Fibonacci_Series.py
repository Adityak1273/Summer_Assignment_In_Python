n=int(input("Enter the series number : "))
num1=0
num2=1
list=[]
for i in range(0,n):
    sum=num1+num2
    list.append(sum)
    num1=num2
    num2=sum
print("The Fibonacci series are : ",list)    
