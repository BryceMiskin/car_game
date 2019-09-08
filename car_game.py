# Turn a car on and off
import sys

# To do list:
# + Finish the "close" command
# + Status command reports if the car is on and driving
# + Status command report which doors are open
# + Automatically close all doors when beginning to drive
# + 

# This block of code is used in some of the following variables. Do not move it!
print()
name = input("Your name: ")
car_name = input("Give me an epic car name: ")
print()
print(f"""Seriously {name}? I could do better than "{car_name}" and I'm a program...""")

# The help menu and credits which can be recalled later.
help = (f"""
Available Commands:
On/Off - Turn {car_name} on or off
Go/Stop - Drive when the car is on
Open/Close - Open a car door, trunk, hood, or gasoline door (Try "Open All" or "Close All")
Status - Is {car_name} on?
Help - Get this helpful list
Quit - End the program""")

creators = ["Bryce Miskin"]
credits = f"Credit for this code goes to {creators}."

# This variable is called later.
door_list = ("""1 - Driver door
2 - Passenger door
3 - The hood
4 - The trunk
5 - Gas door
6 - All choices
7 - Nevermind
""")

# Starting the program with the car off and not driving
power = False
driving = False

# --------------------------------------------------


print('\nNever worry about CaPiTaLiZaTiOn in this program for now on. \nEnter "Help" for command options.\n')

while True:
    command = input("> ").lower()
    if command == "on":
        if power:
            print(f"{car_name} is already started")
        if not power:
            # Car power
            power = True
            print(f"{car_name} ready for takeoff!")
    elif command == "off":
        driving = False
        power = False
        print(f"{car_name} will be waiting for your arrival.")
    elif command == "go":
        if power:
            driving = True
            print(f"{car_name} is driving!")
        if not power:
            driving = False
            print(f"{car_name} must be on")
    elif command == "stop":
        if power:
            if not driving:
                print(f"{car_name} is on but isn't going anywhere already so...")
            if driving:
                driving = False
                print(f"{car_name} stopped.")

        if not power:
            print(f"{car_name} is off and not moving. Wierd flex to make me push the brake anyway but okay...")
    # Is the car on or off?
    elif command == "status":
        if power:
            print(f"""{car_name} is ready to roll! \nTry "go" """)
        elif not power:
            print(f"{car_name} is off and awaiting your arrival.")
    # Open car doors, trunk, hood, or gasoline door. If a door is false then it is open.
    elif command == "open":
        if power:
            print(f"{car_name} cannot open anything while the car is on.")
        if not power:
            print("\nOpen what? Enter a number.")
            print(door_list)
            open_num = int(input("Number: ").lower())
            # Driver door
            if open_num == 1:
                driver_door = False
                print("Driver door opened")
            # Passenger door
            elif open_num == 2:
                passenger_door = False
                print("Passenger door opened")
            # The hood
            elif open_num == 3:
                hood = False
                print("Hood opened")
            # The trunk
            elif open_num == 4:
                trunk = False
                print("Go get your groceries or kidnap children. QUICK!")
            # Gas door
            elif open_num == 5:
                gas_door = False
                print("Time to hydrate the car!")
            # All doors
            elif open_num == 6:
                # Opens all doors
                driver_door = False; passenger_door = False; hood = False; trunk = False; gas_door = False
                print("All doors opened!")
            elif open_num == 7:
                continue
            else:
                print("That's not a number...")
    # Close car doors, trunk, hood, or gasoline door. If a door is true then it is closed and secure.
    elif command == "close":
        print("\nClose what? Enter a number.")
        print(door_list)
        close_num = int(input ("Enter number: "))
        if close_num = 1:
            driver_door = True
####### FINISH THE CLOSE COMMAND
    elif command =="close all":
        driver_door = True; passenger_door = True; hood = True; trunk = True; gas_door = True
        print(f"All doors on {car_name} are locked and secured!")
    elif command == "help":
        print(help) # See the beginning of the code for the help variable.
    elif command == "quit":
        print()
        print(f"See you next time, {name}!")
        print(credits)
        sys.exit()
    # Unknown command?
    else:
        print(f"""That's a spelling error, {name}! Enter "Help" or try again. """)
    print()
