x = int(input("Enter side 1:"))
y = int(input("Enter side 2:"))
z = int(input("Enter side 3:"))
if x == y and y == z and x == z:
    print("Equilatral triangle !")
else:
    if x == y:
        print("Isoceles triangle !")
    elif y == z:
        print("Isoceles triangle !")
    elif z == x:
        print("Isoceles triangle !")
    else:
        print("Scalene triangle !")
