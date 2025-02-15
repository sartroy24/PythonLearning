command = ""
started = False
while True:
    command = input("Enter the command:").lower()
    if command == "start":
        if started:
            print("Your car has already started")
        else:
            print("Your car has started")
            started = True
    elif command == "stop":
        if not started:
            print("Your car has already stopped")
        else:
            started = False
            print("Your car has stopped")
    elif command.lower() == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
        """)
    elif command.lower() == "quit":
        break
    else:
        print("Wrong command")
