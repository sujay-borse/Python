a=int(input("Enter a Number:"))
num=str(a)
num2=num[::-1]
if num!=num2:
    print(num,"this number is not palindrome")
else:
    print(num,"this number is palindrome")