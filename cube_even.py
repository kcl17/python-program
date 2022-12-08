num = int(input ("Enter any number : "))

if (num % 2) == 0:

   cube = num * num * num
   print("The Cube of a Given Number {0}  = {1}".format(num, cube))

else:

    print("The provided number is odd")