email_id = [str(input("Enter Email ID:")) for _ in range(10)]
# loop to repeat the cycle of checking and deleting.
for _ in range(len(email_id)):
    for x in email_id:  # loop to iterate the list
        # conditional loop to check for faulty email IDs
        while x.find("@vit.edu") == -1:
            del email_id[email_id.index(x)]  # fault email ID deleter
            break
print(email_id)
