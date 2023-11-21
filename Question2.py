 2. Create a guessing game where the user has to guess a number between 1 and 100.
Use a loop to give the user 3 attempts, and provide hints (higher/lower) based on their guesses until they get it right.

i = 1
while i <=3:
    if number > secret_num:
        print('Your guess if less than secret num')
        number = int(input('Enter a guess greater than secret num: '))
    elif number < secret_num:
        print('Your guess if greater than secret num')
        number = int(input('Enter a guess less than secret num: '))
    
    elif number == secret_num:
        print('You have guessed the correct number')
        break

    else:
        print('Enter a valid number!')
        number = int(input('Enter a valid number'))
    i+=1
print('Secret Number was ', secret_num)
