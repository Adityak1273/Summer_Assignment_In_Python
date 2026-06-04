n=int(input("Enter the number : "))
copy=n
count=0
digit=0
add=0    
while copy>0:
    factor=1
    digit=copy%10
    for j in range(1,digit+1):
        factor*=j
    copy//=10
    add=add+factor
if n==add:
    print(n," is a strong number.")
else:
    print(n," is not a strong number.")
