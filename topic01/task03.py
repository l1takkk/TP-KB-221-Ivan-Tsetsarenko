def calculate_discriminant(a, b, c):
    discriminant = b**2 - 4*a*c
    return discriminant

a = 2
b = 5
c = 1

discriminant = calculate_discriminant(a, b, c)
print("Discriminant:", discriminant)