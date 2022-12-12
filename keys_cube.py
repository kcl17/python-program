def generate_dict(number):
    return {i:i**3 for i in range(1,number+1)}

print(generate_dict(5))
