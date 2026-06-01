b=int(input("Enter the Number to check Palindrome or Not : "))
rev=0
n=b
while(n>0):
    a=n%10
    rev=rev*10+a
    n//=10
if(rev==b):
    print(b," is a Palindrome. ")
else:
    print(b," is not a Palindrome. ")            
