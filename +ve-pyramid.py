m = True
while m == True: 
    n = int(input("Enter number of rows: "))
    i = int(1)
    while n != 0:
        print("* "*i, "\n")
        i += 2
        n -= 1
    m = input("repeat the program? (y/n): ")
    if m == "y":
        m = bool(1)
    else:
        m = bool(0)
