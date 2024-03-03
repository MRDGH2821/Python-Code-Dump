x = int(input("Enter side 1:"))
y = int(input("Enter side 2:"))
z = int(input("Enter side 3:"))

if x == y and y == z and x == z:
    print("Equilateral triangle !")
elif x != y and y != z and z != x:
    print("Scalene triangle !")
else:
    print("Isosceles triangle !")
