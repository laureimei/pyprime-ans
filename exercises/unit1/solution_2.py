import math
def Unit1_quadratic():
    a = -1  # coefficient of x^2
    b = 8  # coefficient of x
    c = -1  # term c/constant term

    # discriminant calculation starts here
    discriminant = b ** 2 - 4 * a * c

    # use the quadratic formula to find 2 solutions
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)

    root1 = round(root1, 2)
    root2 = round(root2, 2)

    return (root1, root2)


result = Unit1_quadratic()
print(result)
