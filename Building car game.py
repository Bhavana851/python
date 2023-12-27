command = ""
started = False

while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("car is already started")
        else:
            started = True
            print("Car is started")
    elif command == "stop":
        if not started:
            print("car is already stoped")
        else:
            started = False
            print("Car is stoped")
    elif command == "help":
        print(""" 
        start-to start the car
        stop-to stop the car
        quit-to quit the car
        """)
    elif command == "quit":
        break
    else:
        print("I dont understand that")
        break


