a=int(input("first value"))
b=int(input("second value"))
for num in range(a,b+1):
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)