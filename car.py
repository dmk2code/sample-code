command=""
started = False
while True:
    command = input('> ').lower()
    if command == 'start' :
        if started :
          print('car is already started')
        else:
            started = True
            print('car started')
    elif command == 'stop':
        if not started:
           print ('car is already stopped')
        else:
            print("car stopped")
    elif command == 'help':
        print('''
START - TO START THE CAR
STOP - TO STOP THE CAR
QUIT - TO EXIT THE GAME 
        ''')
    elif command == 'quit':
        break
    else :
        print("i don't understand")


