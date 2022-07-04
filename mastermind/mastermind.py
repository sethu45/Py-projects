import random

def computer():
    comp = random.randint(1000,10000)
    return comp

def play():
    player = int(input('Enter the number :'))
    return player

def mastermind():
    print('The number generated, Player please guess the number')
    comp = computer()

    player = play()

    # counting number of tries
    p_tries = 0

    if comp == player:
        print('WOW you guessed within first try')
        p_tries+=1
    else:

        while comp != player:

            p_tries+=1

            # count total digit are match
            count = 0

            # Changing int to string for int has no len
            comp = str(comp)
            player = str(player)

            cor = ['X']*len(comp)

            for i in range(len(comp)):
                if comp[i] == player[i]:
                    count+=1
                    cor[i] = player[i]
                
                else:
                    continue

            # guessed number match 
            if count < 4 and count != 0:
                print(f'Number of digit guessed correct{count}')
                
                for j in cor:
                    print(j, end=' ')
                print('\n')
                player = int(input('try again: '))

            # number are not in the given number
            elif count == 0:
                print('There is no digit correctly guessed')
                player = int(input('try again: '))
            
        if comp == player:
            print('WOW Player you guessed all digits')

def main():
    while True:
        if input('Want to enter the game press "y" want qiut press "q" : ').upper() == 'Y':
            mastermind()
        else:
            print('See You again')
            break

if __name__ == '__main__':
    main()
