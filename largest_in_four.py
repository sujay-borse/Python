a=int(input("Enter a number="))
b=int(input("enter a number="))
c=int(input("Enter a number="))
d=int(input("Enter a number="))
if a>b and a>c and a>d:
    print(a,"is largest")
elif b>a and b>c and b>d:
        print(b,"is largest")
elif c>a and c>b and c>d:
    print(c,"is largest")
else:
    print(d,"is largest")