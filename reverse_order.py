string = str(input(" write the sentence:" ))
# split on spaces
split_str = string.split(' ') 
 # reverse words
reversed_str = reversed(split_str)
# join the reversed words back to string
final_str = ' '.join(reversed_str) 
print("Reversed string: " , final_str)