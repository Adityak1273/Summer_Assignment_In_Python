import math
start=int(input("Enter the starting number of range : "))
end=int(input("Enter the ending number of range : "))
list=[]
for i in range(start,end+1):
    digit=0
    count=0
    sum=0
    copy=i
    while copy>0:
       count+=1
       copy//=10
    copy=i
    for j in range(0,count):
        digit=copy%10
        sum+=math.pow(digit,count)
        copy//=10
    if i==sum:
        list.append(i)
print("Armstrong numbers in the range are : ",list) 
