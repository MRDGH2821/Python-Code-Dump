"""Weight Converter.

Converts weight from KG to grams and vice versa.
"""

choice = int(input("Convert: \n1. Kg->g \n2.g->Kg \n\nEnter Choice: "))
if choice == 1:
    kg = int(input("Enter weight in KG "))
    g = kg * 1000
    print(kg, "kg =", g, "grams")
elif choice == 2:  # noqa: PLR2004
    g = int(input("Enter weight in grams "))
    kg = g // 1000
    print(g, "g =", kg, "KG")
else:
    print("Invalid choice")
