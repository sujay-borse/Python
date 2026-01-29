fact=1
i=1
n=int(input("Enter the number:"))
if n<0:
    print("Number is negative")

while(i<=n):
    fact=fact*i
    i=i+1
print("Factorial of",n,"is:",fact)