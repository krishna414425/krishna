a=int(input("enter a number"))
reverse=0
org=a
while a>0:
    digit=a%10
    reverse=reverse*10+digit
    a=a//10
if org==reverse:
    print("palindrome")
else:
    print("not a palindrome")