l = [str(input("Enter Email ID:")) for i in range(10)]
for i in range(len(l)):  # loop to repeat the cycle of checking and deleting.
    for x in l:  # loop to iterate the list
        # conditional loop to check for faulty email IDs
        while x.find('@vit.edu') == -1:
            del l[l.index(x)]  # fault email ID deleter
            break
print(l)
