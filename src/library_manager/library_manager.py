from openpyxl import load_workbook

import os

current_directory = os.path.dirname(os.path.abspath(__file__))

details_file_path = f"{current_directory}/Details.xlsx"
books_file_path = f"{current_directory}/Books.xlsx"


def find_user(username: str):
    details_workbook = load_workbook(details_file_path)
    details_sheet = details_workbook[details_workbook.sheetnames[0]]

    for i in details_sheet.iter_rows(min_row=1):
        username_value = i[2].value
        if username_value == username:
            return i
    return None


def account():
    print("###### WELCOME TO BAJRANGDAS CENTRAL LIBRARY ######")
    choice = input("\nDo you have an existing account?(y/n): ")
    details_workbook = load_workbook(details_file_path)
    details_sheet = details_workbook[details_workbook.sheetnames[0]]

    if choice == "y" or choice == "Y":
        print("\nUser login")
        username = input("Enter Your Username: ")
        password = input("Enter Your Password: ")
        i = find_user(username)
        if i:
            username_value = i[2].value
            password_value = i[3].value
            # print(username_value, password_value)
            if username_value == username and password_value == password:
                issue(username)
            else:
                raise ValueError("Invalid Username or Password.")
        else:
            raise ValueError("Unknown Username or Password. Please register.")

    elif choice == "n" or choice == "N":

        print("\nUser Registration")
        name = input("Enter Your Name: ")
        gr_number = int(input("Enter Your GR Number: "))
        username = input("Enter Your Username: ")
        password = input("Enter Your Password: ")

        i = find_user(username)
        if i:
            gr_number_value = i[1].value
            username_value = i[2].value
            password_value = i[3].value

            if username_value == username or gr_number_value == gr_number:
                raise ValueError(
                    "USERNAME ALREADY TAKEN or Duplicate GR Number\nTRY AGAIN")

        else:
            details_sheet.append([name, gr_number, username, password])
            details_workbook.save(details_file_path)

        issue(username)


def issue(username: str):
    books_workbook = load_workbook(books_file_path)
    books_sheet = books_workbook[books_workbook.sheetnames[0]]

    details_workbook = load_workbook(details_file_path)
    details_sheet = details_workbook[details_workbook.sheetnames[0]]

    choice = "y"
    # print (n)
    while True:
        print("\n\nMain Menu:")
        print("1. View Available Books")
        print("2. View the books issued by you")
        print("3. Return Books")
        print("4. Login Again")
        print("0. Exit")
        option = int(input("Enter choice: "))
        if option == 1:
            for k in books_sheet.iter_rows():
                print(k[0].value, "  ", k[1].value)
                while choice == "y":
                    serial = int(
                        input("Enter the Serial Number of the book you want to issue:"))
                    # print (ch)
                    if books_sheet.cell(serial + 1, 5).value == 0:
                        print("No Copies Left\n")
                        continue
                    else:
                        for k in range(1, books_sheet.max_row):
                            if books_sheet.cell(k, 0).value == serial:
                                for i in range(1, details_sheet.max_row):
                                    if details_sheet.cell(i, 2).value == username:
                                        # n = sheetd.max_column
                                        c1 = details_sheet.cell(
                                            i + 1, len(details_sheet[i + 1]) + 1)
                                        c1.value = books_sheet.cell(k, 1).value
                                        c2 = books_sheet.cell(serial + 2, 6)
                                        c2.value = books_sheet.cell(
                                            serial + 1, 5).value - 1
                                        details_workbook.save(
                                            details_file_path)
                                        books_workbook.save(books_file_path)
                                        print(
                                            "\n\n\nSUCCESSFULL !!!!!\n The changes will be reflected in your account \n When you Login Again"
                                        )
                                        choice = input(
                                            "Do You want to continue?(y/n)\n")
                                        if choice == "n" or choice == "N":
                                            break
        elif option == 3:
            count = 0
            print("The books issued by you are:\n")
            num = 0
            for i in range(1, details_sheet.max_row):
                if details_sheet.cell(i, 2).value == username:
                    num = i
                for j in range(4, details_sheet.max_column):
                    if (
                        details_sheet.cell(
                            i + 1, j + 1).value
                        is not None
                    ):
                        print(
                            count,
                            ".",
                            details_sheet.cell(
                                i, j).value,
                            end="\n",
                        )
                        count = count + 1
                        return_choice = "y"
                        for i in range(1, details_sheet.max_column - 4):
                            return_qty = int(
                                input(
                                    "Enter the number You want to return:"
                                )
                            )
                            for k in range(1, books_sheet.max_row):
                                for j in range(
                                    4, len(
                                        details_sheet[num + 1])
                                ):
                                    if (
                                        details_sheet.cell(
                                            num, 4 + return_qty - 1
                                        ).value
                                        != ""
                                    ):
                                        break
                                    else:
                                        return_qty = return_qty + 1
                                    if books_sheet.cell(
                                        k, 1
                                    ).value == details_sheet.cell(
                                        num, 4 + return_qty - 1
                                    ).value:
                                        c = books_sheet.cell(
                                            k + 1, 6
                                        )
                                        c.value = (
                                            int(books_sheet.cell(k, 5).value) + 1)
                                        # sheetd .delete_cells(num+1,ret+4)
                                        details_sheet.cell(
                                            num + 1, return_qty + 4
                                        ).value = None
                                        print(
                                            "\nReturn successful"
                                        )
                                        details_workbook.save(
                                            details_file_path)
                                        books_workbook.save(
                                            books_file_path)
                                        return_choice = input(
                                            "Do you have any books to return ?(y/n)"
                                        )
                                    if (
                                        return_choice == "n"
                                        or return_choice == "N"
                                    ):
                                        break
                                    elif (
                                        return_choice == "y"
                                        or return_choice == "Y"
                                    ):
                                        print(
                                            "\n\n\nCONFIRM YOUR LOGIN DETAILS\n"
                                        )
                                        account()
        elif option == 0:
            print(
                "###### Thank You ######\n\n###### Visit Again #####"
            )
            exit(0)
        elif option == 4:
            account()
        elif option == 2:
            count = 1
            print(
                "The books issued by you are:\n"
            )
            for i in range(1, details_sheet.max_row):
                if (
                    details_sheet.cell(
                        i, 2
                    ).value
                    == username
                ):
                    num = i
                for j in range(
                    4, details_sheet.max_column
                ):
                    if (
                        details_sheet.cell(
                            i + 1, j + 1
                        ).value
                        is not None
                    ):
                        print(
                            count,
                            ".",
                            details_sheet.cell(
                                i, j
                            ).value,
                            end="\n",
                        )
                        count = count + 1


try:
    account()
except Exception as e:
    print("\n")
    print(e)
    print("Please try again later.")