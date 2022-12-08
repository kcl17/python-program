l = True
while l == True: 
    n = int(input("Enter number of rows: "))
    while n != 0:
        print("* "*n)
        n -= 1
    l = input("repeat the program? (y/n): ")
    if l == "y":
        l = bool(1)
    else:
        l = bool(0)
