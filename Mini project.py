#-------------------------------------------------------------------------------
# Name:
# Purpose:     Group project
#
# Author:      Nikhil kr.sah
#
# Created:     28-09-2022
# Copyright:   (c) Nikhil kr SAH 2022
# Licence:     <Troms licence>
#-------------------------------------------------------------------------------
while True:
        print("""
        ====== Bike Rental Shop =======
        1. Display available bikes
        2. Request a bike on hourly basis $5
        3. Request a bike on daily basis $20
        4. Request a bike on weekly basis $60
        5. Return a bike
        6. Exit
        """)

        choice = input("Enter choice: ")

        try:
            choice = int(choice)
        except ValueError:
            print("That's not an int!")
            break

        if choice == 1:
            print("available bikes")
            break

        elif choice == 2:
            print("bike on hourly basis")
            break

        elif choice == 3:
            print("bike on daily basis ")
            break


        elif choice == 4:
            print("bike on weekly basis")
            break


        elif choice == 5:
            print("Return a bike")
            break

        elif choice == 6:
            break
        else:
            print("Invalid input. Please enter number between 1-6 ")
print("Thank you for using the bike rental system.")
