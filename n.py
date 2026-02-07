rows = int(input("Enter the number of rows for the pyramid: "))
i = 0
while i < rows:
    spaces = rows - i - 1
    stars = 2 * i + 1
    j = 0
    while j < spaces:
        print(" ", end="")
        j += 1

    j = 0
    while j < stars:
        print("*", end="")
        j += 1

    print()
    i+=1