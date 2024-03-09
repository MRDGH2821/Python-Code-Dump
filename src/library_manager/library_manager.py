from openpyxl import load_workbook

details_file = "./Details.xlsx"
books_file = "./Books.xlsx"


def account():
    print("###### WELCOME TO BAJRANGDAS CENTRAL LIBRARY ######")
    choice = input("\nDo you have an existing account?(y/n)\n")
    details_file_path = details_file
    details_workbook = load_workbook(details_file_path)
    details_sheet = details_workbook[details_workbook.sheetnames[0]]

    n = details_sheet.max_row

    flag = 0
    if choice == "y" or choice == "Y":
        username = input("Enter Your Username: ")
        password = input("Enter Your Password: ")
        for i in range(1, details_sheet.max_row):
            username_value = details_sheet.cell(i, 2).value
            password_value = details_sheet.cell(i, 3).value
            if username_value == username and password_value == password:
                """Comment the next 2 lines and add function call when the function issue() is created"""
                # for k in range(sheet2.max_row):
                #         print (sheet2.cell(k, 0).value,"  ",sheet2.cell(k, 1).value)
                issue(username)
                flag = 1
            if flag == 0:
                print("INCORRECT USERNAME OR PASSWORD")
    elif choice == "n" or choice == "N":
        f = 0
        while f != 1:
            name = input("Enter Your Name: ")
            gr_number = int(input("Enter Your GR Number: "))
            username = input("Enter Your Username: ")
            password = input("Enter Your Password: ")

            for i in range(1, details_sheet.max_row):
                gr_number_value = details_sheet.cell(i, 1).value
                username_value = details_sheet.cell(i, 2).value
                password_value = details_sheet.cell(i, 3).value

                if username_value == username or gr_number_value == gr_number:
                    print(
                        "USERNAME ALREADY TAKEN or Duplicate GR Number\nTRY AGAIN"
                    )
                    f = 0
                    break
                else:
                    f = 1
                    c1 = details_sheet.cell(n + 1, 1)
                    c1.value = name
                    c2 = details_sheet.cell(n + 1, 2)
                    c2.value = gr_number
                    c3 = details_sheet.cell(n + 1, 3)
                    c3.value = username
                    c4 = details_sheet.cell(n + 1, 4)
                    c4.value = password
                    details_workbook.save(details_file_path)
                    """Comment the next 2 lines and add function call when the function issue() is created """
            # for k in range(sheet2.max_row):
            #          print (sheet2.cell(k, 0).value, "  ", sheet2.cell(k, 1).value)
            issue(username)


def issue(username: str):
    books_file_path = books_file
    books_workbook = load_workbook(books_file_path)
    books_sheet = books_workbook[books_workbook.sheetnames[0]]

    details_file_path = details_file
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
            for k in range(1, books_sheet.max_row):
                print(books_sheet.cell(k, 0).value,
                      "  ", books_sheet.cell(k, 1).value)
                while choice == "y":
                    serial = int(
                        input(
                            "Enter the Serial Number of the book you want to issue:")
                    )
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
                                        n = details_sheet.max_column
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
            cnt = 1
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
                            cnt,
                            ".",
                            details_sheet.cell(
                                i, j).value,
                            end="\n",
                        )
                        cnt = cnt + 1
                        return_choice = "y"
                        for i in range(1, details_sheet.max_column - 4):
                            ret = int(
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
                                            num, 4 + ret - 1
                                        ).value
                                        != ""
                                    ):
                                        break
                                    else:
                                        ret = ret + 1
                                    if books_sheet.cell(
                                        k, 1
                                    ).value == details_sheet.cell(
                                        num, 4 + ret - 1
                                    ).value:
                                        c = books_sheet.cell(
                                            k + 1, 6
                                        )
                                        c.value = (
                                            int(books_sheet.cell(k, 5).value) + 1)
                                        # sheetd .delete_cells(num+1,ret+4)
                                        details_sheet.cell(
                                            num + 1, ret + 4
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
            cnt = 1
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
                            cnt,
                            ".",
                            details_sheet.cell(
                                i, j
                            ).value,
                            end="\n",
                        )
                        cnt = cnt + 1


account()
