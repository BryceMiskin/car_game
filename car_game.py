######### TTHIS IS MADE FOR FUN. THE USER WILL BE ABLE TO INTEREACT WITH AN IMAGINARY CAR IN THIS PROGRAM #########
import sys

# To do list:
# + Automatically close all doors when beginning to drive
# + Status command reports if the car is on and driving
# + Status command report which doors are open
# + Automatically close all doors when beginning to drive
# + 

############################ VARIABLE STORAGE TO PREPARE INTRO ############################

# For the "else" block in "if question_choice == "y" and what not"
# Also used in the (y / n) below
question_mispell = """\n(y / n) means to submit "y" for yes and "n" for no. Try again.\n"""

############################ INTRO TO PREPARE THE VARIABLE STORAGE (INTERACTION INCLUDED) ############################

name = input("\nYour name: ")

while True:
    car_name = input("Name your car: ")
    car_name_verify = input(f"\nName your car {car_name}? \n(y / n): ").lower()
    if car_name_verify == "y":
        break
    elif car_name_verify == "n":
        print("\nAlright here's a second shot.")
        continue
    if car_name_verify != "y" "n":
        print(question_mispell)
        car_name_verify = input(f"Name your car {car_name}? \n(y / n): ")

print(f"""\n{car_name} is an impressive car name, {name}!""")

############################ VARIABLE STORAGE ############################

# Users can call this variable later 
help = (f"""
Available Commands:
On/Off - Turn {car_name} on or off
Go/Stop - Drive when the car is on
Open/Close - Open a car door, trunk, hood, or gasoline door (Try "Open All" or "Close All")
Status - Is {car_name} on?
Help - Get this helpful list
Quit - End the program""")

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

creators = ["Bryce Miskin"]
credits = f"Credit for this code goes to {creators}."

############################ INTERACTION RESUMED ############################

print('Never worry about CaPiTaLiZaTiOn in this program from now on. \nEnter "Help" for command options.\n')

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

    # Open car doors, trunk, hood, or gasoline door. If a door is false then it is open.
    elif command == "open":
        if driving:
            print(f"{car_name} cannot open anything while the car is driving.")
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
        close_num = int(input("Number: ").lower())
        ## 1-driver door 2-Passenger 3- the hood 4- the trunk 5- gas door 6-all doors
        ## True means closed and secured
        if close_num == 1:
            if not driver_door:
                driver_door = True
                print(f"")
            if driver_door:
                print(f"{name}'s {car_name}'s door already closed.")
        elif close_num == 2:
            if not passenger_door:
                passenger_door = True
                print(f"Okay, {car_name}'s passenger door closed.")
            if passenger_door:
                print(f"Passenger on {car_name} is already secured.")
        elif close_num == 3:
            if not hood:
                hood = True
                print(f"")
            if hood:
                print(f"")
        elif close_num == 4:
            if not trunk:
                trunk = True
                print(f"Hood closed. The children are trapped.")
            if trunk:
                print("The children already can't escape {car_name}. Hopefully they don't eat your groceries...")
        elif close_num == 5:
            if not gas_door:
                gas_door = True
                print("Gas door closed.")
            if gas_door:
                print(f"The gas door isn't isn't open... Nice try though, {name}.")
        elif close_num == 6:
                driver_door = True; passenger_door = True; hood = True; trunk = True; gas_door = True
    elif command == "status":
        if power:
            print(f"""{car_name} is turned on! When {car_name} is on all doors close. \nTry "go" """)
        if not power:
            print(f"""{car_name} is off and awaiting your arrival.""")
            print("See which doors are open and closed?")
            question_choice = input("(y / n): ")
            if question_choice == "y":
                ###### FINISH
                print()
            if question_choice == "n":
                break
            else:
                print()
                ###### FINISH

    # Close all doors
    elif command =="close all":
        driver_door = True; passenger_door = True; hood = True; trunk = True; gas_door = True
        print(f"All doors on {car_name} are locked and secured!")
    elif command == "help":
        print(help) # See the beginning of the code for the help variable.
    elif command == "quit":
        print(f"\nSee you next time, {name}!")
        print(credits)
        sys.exit()
    # Unknown command?
    else:
        print(f"""That's a spelling error, {name}! Enter "Help" or try again. """)
    print()
