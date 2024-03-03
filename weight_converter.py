"""
Weight Converter
"""

fh = int(input("Convert Kg->g or g->Kg (1/2)? "))
if fh == 1:
    kg = int(input("Enter weight in KG "))
    g = kg * 1000
    print(kg, "kg =", g, "grams")
elif fh == 2:
    g = int(input("Enter weight in grams "))
    kg = g // 1000
    print(g, "g =", kg, "KG")
else:
    print("Invalid choice")
