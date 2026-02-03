a=int(input("Enter marks of subject 1= "))
b=int(input("Enter marks of subject 2= "))
c=int(input("Enter marks of subject 3= "))
d=int(input("Enter marks of subject 4= "))
e=int(input("Enter marks of subject 5= "))
p=((a+b+c+d+e)/5)*100
print("percentage=",p)
if p<40:
    print("Fail")
elif p<50:
    print("Pass")
elif p<60:
    print("Second class")
elif p<70:
    print("First class")
else p<100:
    print("Distinction")