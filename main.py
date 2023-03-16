active = True
while active:
    names = input("Enter your first and second name: ").title()
    names = names.strip()

    if names == "Help":
        print("\nType 'done' to end program.")
        print("Type 'list' to check the entered name list.\n")

    elif names == "Done":
        active = False

    elif names == "List":
        print("Name List")
        with open("Names.txt") as updated_list:
            print(updated_list.read())

    else:
        with open("Names.txt", "a") as name_list:
            name_list.write(f"{names}\n")
