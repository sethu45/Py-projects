# In this game, there is a list of words present, out of which 
# our interpreter will choose 1 random word. The user first has 
# to input their names and then, will be asked to guess 
# any alphabet. If the random word contains that alphabet, 
# it will be shown as the output(with correct placement) 
# else the program will ask you to guess another alphabet. 
# The user will be given 12 turns(which can be changed 
# accordingly) to guess the complete word.


import random 

def words():
    words = "double prison left courage hear physics pound buffet say bless plaintiff legislature eyebrow scrap flex withdraw craftsman elect reluctance poem consumer remunerate world appreciate undermine relative acquisition homosexual morsel need".split()

    rand_word = random.choice(words)
    return rand_word.upper()

def user_name():
    word = words()
    user_name = input('Enter your name: ')
    print('All the Best:', user_name)

    print('Hint for word')
    print('the word contain:',len(word), 'letter')

def word_guessing():
    guesses = ' '
    word = words()
    turns = 12
    print('you only have 12 guess')

    while turns > 0:

        loss_turn = 0
        lis = [let if let in guesses else '_' for let in word]
        print('the words ', ' '.join(lis))
        for lis in word:
            if lis in guesses:
                print('WOW! there is letter')
            else:
                loss_turn+=1
        
        if loss_turn == 0:
            print()
            print('Congrats! you won')
            break
        
        print()
        user_guess = input('Enter your guess: ').upper()
        guesses += user_guess

        if user_guess not in word:
            print('try agian')
            turns= turns-1
            print('you have',turns,'turns')
            
if __name__ == '__main__':
    word_guessing()



