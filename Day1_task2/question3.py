def car_racing():
    initial_state = 'stop'
    hint = """ Enter start->To start the car 
    Enter stop->To stop the car
    Enter exit->To exit the game
    """
    print(hint)
    play = True
    while play:
        new_state = input('Enter the new state of car: ')
        new_state = new_state.lower()
        states = ['start', 'stop', 'exit']
        if new_state in states:
            if(new_state == initial_state):
                print(f'Car is already in {initial_state} state')
            elif(new_state == 'exit'):
                are_you_sure = input('Are you sure to exit the game?(yes/no)').lower()
                if are_you_sure == 'yes':
                    play = False
                    
            elif(new_state != initial_state or new_state != 'exit'):
                initial_state = new_state
                print(f'Car shifted to {initial_state}')
                
            else:
                print('Enter a valid input!')
        else:
            print('Invalid Input!!!')
            print(hint)

car_racing()
            
