# Turn a car on and off

import sys

# The help menu and credits which can be recalled later.
help = ("""
Available commands:
on - Turn the car on
off - Turn the car off
status - Is the car on?
open - Open a car door, trunk, hood, or gasoline door
help - Get this list of commands
quit - End the program""")
credits = "Credit for this code goes to Bryce Miskin."

open_close_list = ("""1 - Driver door
2 - Passenger door
3 - The hood
4 - The Trunk
5 - Gas door
""")

# --------------------------------------------------

print()
print('Enter "help" for available options')

# Starting the program with the car off
power = False

while True:
    command = input("> ").lower()
    if command == "on":
        power = True
        print("Ready for takeoff!")
    elif command == "off":
        power = False
        print("Turned off.")

# Is the car on or off?
    elif command == "status":
        if power:
            print("The car is ready to roll!")
        elif not power:
            print("The car is waiting patiently for your return.")

# Open car doors, trunk, hood, or gasoline door
    elif command == "open":
        if power:
            print("Cannot open anything while the car is on.")
        if not power:
            print("\nOpen what? Enter a number.")
            print(open_close_list)
            open_num = input("> ").lower()
            # Driver door
            if open_num == 1:
                driver_door = "open"
                print("Driver door opened")
                break
            # Passenger door
            elif open_num == 2:
                passenger_door = "open"
                print("Passenger door opened")
                break
            # The hood
            elif open_num == 3:
                hood = "open"
                print("Hood opened")
            # The trunk
            elif open_num == 4:
                trunk = "open"
                print("Go get your groceries!")
            # Gas door
            elif open_num == 5:
                gas_door = "open"
                print("Time to hydrate the car!")
            else:
                print("That's not a number...")
# See the 'help' variable at the beginning of the code.
    elif command == "help":
        print(help)
    elif command == "quit":
        print()
        print("See you next time!")
        print(credits)
        sys.exit()
    else:
        print("Oops, I don't know that. ")
    print()
