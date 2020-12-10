a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
D = b**2 - 4*a*c
x1 = (-b + D**(1/2))/2*a
x2 = (-b - D**(1/2))/2*a
print(f"x1 = {x1}")
print(f"x2 = {x2}")