print("1 add")
print("2 subtract")
print("3 multiply")
print("4 divide")
print("5 power")
choice = int(input("enter choice (1/2/3/4): "))
a = float(input("enter the first number"))
b = float(input("enter the second number"))
if choice == 1:
    print(a,"+",b,"=",a+b)
elif choice == 2:
    print(a,"-",b,"=",a-b)
elif choice == 3:
    print(a,"x",b,"=",a*b)
elif choice ==4:
    print(a,"/",b,"=",a/b)
elif choice == 5:
    print(a,"^",b,"=",a**b)
