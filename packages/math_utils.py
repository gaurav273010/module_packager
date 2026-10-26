from datetime import datetime
import time
import math
from uuid import uuid4
import random
import string


def dt_operation():
    while True:
        print("\nDatetime and Time Operations:")
        print("1. Display current date and time")
        print("2. Calculate difference between two dates/times")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")
        print()

        choice = int(input("\nEnter your choice:"))

        if choice == 1:
            print(datetime.now())

        elif choice == 2:
            dt1 = input("\nEnter first Date:")
            dt2 = input("Enter second Date:")

            dt1 = datetime.strptime(dt1, "%d-%m-%Y")
            dt2 = datetime.strptime(dt2, "%d-%m-%Y")

            new_dt = abs(dt2-dt1)
            print(f"Difference between two dates is {new_dt}")

        elif choice == 3:
            current_dt = datetime.now()
            print("1. For Date")
            print("2. For Time")
            print("3. For Both")

            choice = int(input("\nEnter your choice: "))

            if choice == 1:
                print(current_dt.strftime("%d/%m/%Y"))
            elif choice == 2:
                print(current_dt.strftime("%H:%M:%S"))
            elif choice == 3:
                print(current_dt)
            else:
                print("Invalid Input")

        elif choice == 4:
            start = time.time()
            stop = input("\nPress enter to stop: ")
            end = time.time()
            print(f"Stopwatch difference {end-start}")

        elif choice == 5:
          num = int(input("\nEnter a number for countdown: "))
          while num > 0:
              print(num)
              time.sleep(1)
              num-=1
              
        elif choice == 6:
            print()
            break
        else:
            print("Invalid Input")


def maths_operation():
    while True:
        print("\nMathematical Operations: ")
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trignometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Back to Main Menu")

        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            num = int(input("\nEnter a number: "))
            fact = math.factorial(num)
            print(f"Factorial of {num} is {fact}.")

        elif choice == 2:
            money = int(input("\nEnter amount: "))
            rate = float(input("Enter rate of interest: "))
            year = int(input("Enter duration (in years): "))

            CI = money * (1 + rate/100)** year
            print(f"Compound Interest is {CI}")
            
        elif choice == 3:
            value = int(input("\nEnter the value: "))
            radian = math.radians(value)
            print(f"Sine is: {math.sin(radian)}")
            print(f"Cosine is: {math.cos(radian)}")

        elif choice == 4:
            print("\nSelect an option: ")
            print("1. Area of Circle")
            print("2. Area of Rectangle")

            choice = int(input("\nEnter your choice: "))

            if choice == 1:
                radius = float(input("\nEnter the Radius of Circle:"))
                Area = math.pi * radius*radius
                print(f"Area of Circle is {Area}")

            elif choice == 2:
                length = float(input("\nEnter the length of rectangle: "))
                width = float(input("Enter the breadth of rectangle: "))
                Rectangle = length * width
                print(f"Area of Rectangle is {Rectangle}")

            else:
                print("Invalid Input!")

        elif choice == 5:
            print()
            break
        else:
            print("Invalid Input")


def uuid_function():
    id = uuid4()
    print("\nGenerate Unique Identifiers: ")
    print(f"Generated UUID: {id}\n")    


def random_opration():
    while True:
        print("Select an option: ")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Back to Main Menu")

        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            number = random.randint(1,10)
            print(number,"\n")

        elif choice == 2:
           list = [16,29,11,9,7]
           random.shuffle(list)
           print(list,"\n")

        elif choice == 3:
            len = int(input("Enter a length for the password: "))
            character = string.ascii_letters + string.punctuation + string.digits
            password = "".join(random.choices(character,k=len))
            print(f"Generated Password: {password}\n")

        elif choice == 4:
            otp = random.randrange(100000,999999)
            print(otp,"\n")

        elif choice == 5:
            break

        else:
            print("Invalid Input")
