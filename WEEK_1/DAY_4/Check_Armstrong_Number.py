import math
n=int(input("Enter the number : "))
sum=0
digit=0
copy=n
count=0
while copy>0:
    count+=1
    copy//=10
copy1=n
for i in range(0,count):
    digit=copy1%10
    sum+=math.pow(digit,count)
    copy1//=10
if (n==sum):
    print(n," is a armstrong number.")
else:
    print(n," is not a armstrong number.")