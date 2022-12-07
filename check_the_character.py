inp = True
while inp == True:
    inp = input("Enter anything : ")
    if inp >= "a" and inp <= "z" or inp >= "A" and inp <= "Z":
        print("input is alphabet")
    elif inp>="0":
        print("input is number")
    else:
        print("special character")

    inp = input("Do you want to run the program again? (y/n):")
    if inp == "y":
        inp = bool(1)
    else:
        inp = bool(0)