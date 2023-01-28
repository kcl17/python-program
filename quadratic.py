def find_roots(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant >= 0:

        sqrt_discriminant = discriminant**0.5
        root1 = (-b + sqrt_discriminant) / (2*a)
        root2 = (-b - sqrt_discriminant) / (2*a)
        return (root1, root2)
    else:

        real_part = -b / (2*a)
        imag_part = discriminant**0.5 / (2*a)
        return (real_part + imag_part*1j, real_part - imag_part*1j)

print(find_roots(1, -3, 2))  
