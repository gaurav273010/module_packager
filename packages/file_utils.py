

def create_file():
    try:
        name = input("Enter a File Name: ")
        with open (name,"x") as file:
            print("File created Successfully!")
            
    except:
        print("File already exists!")

def add_entry():
    try:
        file = input("Enter a new file name: ")
        entry = input("Enter a new entry: ")
        with open(file,"w") as file:
            file.write(entry + "\n")
            print("Entry Added Successfully!")
    except:
        print("Something went wrong!")

def read_file():
    try:
        file = input("Enter a file name:")
        with open(file,"r") as file:
            show_entry = file.read()
            print("File Content: ")
            print(show_entry)
    except:
        print("This file doesn't exists! Create a file firsts! ")


def append_file():
    try:
        file = input("Enter a file name: ")
        data = input("Enter data to append: ")
        with open(file,"a") as file:
            file.write(data + "\n")
            print("Data Append Successfully!")
    except:
        print("Something went wrong")

def update_file():
    try:
        file_name = input("Enter a file name: ")
        old_entry = input("Enter the entry to replace: ").strip()
        new_entry = input("Enter the new entry: ").strip()

        with open(file_name, "r") as file:
            data = file.read()

        if old_entry.strip() in data:
            data = data.replace(old_entry, new_entry)

            with open(file_name, "w") as file:
                file.write(data)

            print("Entry updated successfully!")
        else:
            print("Entry not found!")

    except:
        print("File doesn't exist!")


def file_operation():
    while True:
        print("\nSelect an option: ")
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Update to a file")
        print("6. Back to Main Menu")

        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            create_file()

        elif choice == 2:
            add_entry()

        elif choice == 3:
            read_file()

        elif choice == 4:
            append_file()

        elif choice == 5:
            update_file()

        elif choice == 6:
            break

        else:
            print("Enter a valid Input!")