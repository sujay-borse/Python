a=int(input("Enter first number="))
b=int(input("Enter second number="))
ch=int(input("Enter choice:-addition=1 \n substaction=2 \n multiplication=3 \n division=4"))
if ch == 1:
    c=a+b
    print("Addition=",c)
elif ch == 2:
    c=a-b
    print("Substraction=",c)
elif ch == 3:
    c=a*b
    print("Multiplication=",c)
elif ch == 4:
    c=a/b
    print("Division=",c)
else:
    print("Invalid")
