ste = str(input("Enter a string "))
ct = 0
for x in ste:
    if x == 'a' or 'e' or 'i' or 'o' or 'u' or 'A' or 'E' or 'I' or 'O' or 'U':
        ct = ct + 1
print("Total vowels = ", ct)
print("a= ", ste.count('a', 0, len(ste)))
print("e= ", ste.count('e', 0, len(ste)))
print("i= ", ste.count('i', 0, len(ste)))
print("o= ", ste.count('o', 0, len(ste)))
print("u= ", ste.count('u', 0, len(ste)))
print("A= ", ste.count('A', 0, len(ste)))
print("E= ", ste.count('E', 0, len(ste)))
print("I= ", ste.count('I', 0, len(ste)))
print("O= ", ste.count('O', 0, len(ste)))
print("U= ", ste.count('U', 0, len(ste)))
