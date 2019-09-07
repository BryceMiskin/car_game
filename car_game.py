# Turn a car on and off

# The help menu and credits which can be recalled later.
help = ("""
Available commands:
on - Turn the car on
off - Turn the car off
help - Get this list of commands
quit - End the program
""")
credits = "Code created by Bryce Miskin."

# --------------------------------------------------

print()
print('Enter "help" for available options')
power = False

while True:
    command = input("> ").lower()
    if command == on:
        power = True
        print("Ready for takeoff!")
    elif command == off:
        power = False
        print("Turned off.")
    elif command == help:
        print(help)
    elif command == quit:
        print()
        print("See you next time!")
        print(credits)
    else:
        print("Oops, I don't know that. ")



# Open a car door when the car is off
    # elif command == open:
    #     if power: