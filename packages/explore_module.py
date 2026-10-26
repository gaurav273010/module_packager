
def explore_module():
    while True:
        print("Select an option: ")
        print("1. For Datetime and time module")
        print("2. For Mathematical module")
        print("3. For Random module")
        print("4. For UUID module")
        print("5. Back to Main Menu")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            from datetime import datetime
            import time
            print(dir(datetime))
            print(dir(time))

        elif choice == 2:
            import math
            print(dir(math))

        elif choice == 3:
            import random
            print(dir(random))

        elif choice == 4:
            from uuid import uuid4
            print(dir(uuid4))

        elif choice == 5:
            break

        else:
            print("Invalid Input!")