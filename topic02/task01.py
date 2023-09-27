import math

# Function to calculate the discriminant
def calculate_discriminant(a, b, c):
    return b**2 - 4*a*c

# Function to calculate the roots
def calculate_roots(a, b, discriminant):
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return root,
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return root1, root2

# Enter coefficients
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Calculate the discriminant
discriminant = calculate_discriminant(a, b, c)

# Calculate the roots
roots = calculate_roots(a, b, discriminant)

# Display the result
if len(roots) == 2:
    print(f"Two real roots: {roots[0]} and {roots[1]}")
elif len(roots) == 1:
    print(f"One real root: {roots[0]}")
else:
    print(f"Complex roots: {roots[0]} and {roots[1]}")