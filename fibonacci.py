f=0
a=0
b=1
count=int(input("How many number you want="))
print("Fibonacci series is =")
print(a)
print(b)
while(f<=count):
    temp=a+b
    print(temp)
    a=b
    b=temp
    f=f+1