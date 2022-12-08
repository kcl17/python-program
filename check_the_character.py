inp = True
while inp == True:
    inp = input("Enter anything : ")
    if inp >= "a" and inp <= "z" or inp >= "A" and inp <= "Z":
        print("input is alphabet")
    elif inp>="0":
        print("input is number")
    else:
        print("special character")

    inp = input("repeat the program? (y/n):")
    if inp == "y":
        inp = bool(1)
    else:
        inp = bool(0)
