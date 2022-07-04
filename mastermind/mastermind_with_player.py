
def player_one():
    player1 = int(input('Player 1, Enter the number: '))
    return player1

def player_two():
    player2 = int(input('Player 2, Enter the number: '))
    return player2

def player_guess():
    player1 = player_one()

    
    player2_guesses = int(input('Player 2, Enter your guess: '))
    
    p2_guess = 0
    if player1 == player2_guesses:
        print('you have Won. You\'re now MASTERMIND ')
        p2_guess+=1

    else:
        
        while player1 !=player2_guesses:
            p2_guess+=1

            count = 0

            player1 = str(player1)

            player2_guesses = str(player2_guesses)
            
            cor = ['X']*len(player1)

            for i in range(len(player1)):
                if player1[i] == player2_guesses[i]:
                    count+=1
                    cor[i] = player2_guesses[i] 
                else:
                    continue

            if count < len(player1) and count != 0:
                print('the number you have guessed',count,'the digits')
                
                for k in cor:
                    print(k,end=' ')
                print('\n')
                player2_guesses = int(input('Try another guess: '))
            
            elif count == 0:
                print('you guess the digit none where matched')
                player2_guesses = int(input('try another guess: '))

        if player1 == player2_guesses:
            print('your are won. Your MASTERMIND')
    
    # now for Player 2 to set the number.

    player2 = player_two()

    player1_guesses = int(input('Player 1, Enter your guess: '))

    p1_guess = 0
    if player2 == player1_guesses:
        print('You have won, Won within one try. YOUR MASTERMIND')
        p1_guess+= 1
    else:
        

        while player2 != player1_guesses:
            p1_guess+=1

            count_p2 = 0

            player2 = str(player2)

            player1_guesses = str(player1_guesses)

            correct = ['X']*len(player2)

            for i in range(len(player2)):
                if player2[i] == player1_guesses[i]:
                    count_p2+=1
                    correct[i] = player1_guesses[i]

                else:
                    continue
            if count_p2 < len(player2) and count_p2 != 0:
                print('the digit your correctly guessed', count_p2,' the digits')
                for j in correct:
                    print(j, end = ' ')
                print('\n')
                player1_guesses = int(input('try again: '))
                
            elif count_p2 == 0:
                print('none of them matched, try again')
                player1_guesses = int(input('try again: '))

        if player1_guesses == player2:
            print('You won the match')
            print('Now going to select who is mastermind')


    if p2_guess > p1_guess:
        print('Player1 is MASTERMIND')
        print('Number of guesses player 1: ',p1_guess,'and player two: ', p2_guess )
    else:
        print('player 2 is Mastermind, because ')
        print('Number of guesses player 2: ',p2_guess,'and player one: ', p1_guess )

def main():
    while True:
        if input('Type "Y" to enter the game or want QUIT the game Typw "Q": ').upper() == 'Y':
            player_guess()
        else:
            print('Bye Bye.')
            break


if __name__ == "__main__":
    main()















