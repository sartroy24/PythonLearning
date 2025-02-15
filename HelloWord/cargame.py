command = ""
while command.lower() != "quit":
    command = input("Enter the command:")
    if command.lower() == "start":
        print("Your car has started")
    elif command.lower() == "stop":
        print("Your car has stopped")
    elif command.lower() == "quit":
        break
    else:
        print("Wrong command")
