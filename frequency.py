
str = str(input("Enter a string: "))

# create dictionary to store key value pair
freq = {}

for i in str:
    # if i already appears as key in dict, increment the count
    if i in freq:
        freq[i] += 1

    # else i appears for the first time, add to dict
    else:
        freq[i] = 1

# printing result 
print(freq)