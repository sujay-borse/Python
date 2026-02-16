# print("Enter number of rows=")
rows=int(input("Enter number of rows="))
i=1
while i<=rows:
    j=rows
    while j>i:
        print(" ",end="")
        j=j+1
    k=1
    while k<=i:
        print("*",end=" ")
        k=k+1
    print( )
    i=i+1

# rows = int(input("Enter the number of rows for the pyramid: "))
# i = 0
# while i < rows:
#     print(" " * (rows - i - 1) + "*" * (2 * i + 1))
#     i += 1


# rows=int(input("Enter rows="))
# i=0
# while i<rows:
#     print(" " * (rows-i-1)+"*"*(2*i+1))
#     i+i+1