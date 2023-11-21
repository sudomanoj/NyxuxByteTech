 2. Create a guessing game where the user has to guess a number between 1 and 100.
Use a loop to give the user 3 attempts, and provide hints (higher/lower) based on their guesses until they get it right.

def guess_game():
    import random
    secret_num = random.randint(0, 100)
    # secret_num = 23
    number = int(input('Enter a number between 1 and 100: '))

    
    for i in range(3):
        if number > secret_num:
            print('Your guess is greater than secret num')
            number = int(input('Enter a smaller guess'))
        elif number < secret_num:
            print('Your guess is less than secret num')
            number = int(input('Enter a greater guess'))
        
        elif number == secret_num:
            print('You have guessed the correct number')
            break

        else:
            print('Enter a valid number!')
            number = int(input('Enter a valid number'))
        
    print('Secret Number was ', secret_num)
    
guess_game()
while True:
    ans = input('Wanna Play again ?(y/n)').lower()
    if ans in ['y', 'Y']:
        guess_game()
    else:
        break
