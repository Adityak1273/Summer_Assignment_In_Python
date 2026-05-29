starting=int(input("Enter the starting range number : "))
ending=int(input("Enter the ending range number : "))
sub=0
prime=[]
for i in range(starting,ending):
    for j in range(2,i):
        if(i%j==0 or i==0 or i==1):
            sub=i
    if(i!=sub):
        add=0
        prime.append(i)
        add+=1
print("Prime number in range are : ",prime)        
