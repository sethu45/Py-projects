# Import random library
import random

# ask the user to enter a number for range value.
# if user enter some string then make user to enter number again 
# until the user correctly entered.
while True:
    try:
        user_num = int(input('Enter the range of number: '))
    except:
        print('Sorry! Try to enter number')
    else:
        break

# select random number from the user given number 
comp_chioce = random.choice(range(user_num))

# how many time user try to guess the number
guess_count = 0

# the game will run until the user guess the number
while True:

    # asking user to guess the number
    user_guess = int(input('Enter number to guess: '))

    # if user guess the correct number then game will end
    if user_guess == comp_chioce:
        guess_count = guess_count+1
        print('WOW! You Guessed it correctly.')
        break

    elif user_guess <= comp_chioce:
        guess_count = guess_count+1
        print('the value is less than try to guess number again')

    elif user_guess >= comp_chioce:
        guess_count = guess_count+1
        print('The value is greater than try to guess number again')


# print out number of time user used to guess the number
print('Your Guess Count = ',guess_count)

if guess_count < 2:
    print('Congarts! You have guessed within first try.')
