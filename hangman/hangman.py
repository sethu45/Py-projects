#import module
import random
import list_of_words 


def list_of_word():

    words = list_of_words.list_words

    word = random.choice(words)

    return word.upper()

def list_of_alpha():

    alpha = list_of_words.alphabet
    return alpha


def hangman():

    word = list_of_word()
    alpha = list_of_alpha()
    list_word = set(word)
    list_alpha = set(alpha)
    used_let = set()
    
    tries = 6
    while len(list_word) > 0 and tries > 0:
        word_list = [letter if letter in used_let else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_guess = input('enter the letter: ').upper()
        if user_guess in list_alpha - used_let:  
            used_let.add(user_guess)

            if user_guess in list_word:
                list_word.remove(user_guess)
                print('')
            else :

                tries-=1
        elif user_guess in used_let:
            print('you have already used that letter')
            
        else:
            print('Its not valid letter')

    if tries == 0:
        print('you losed all your chances the word is ',word)
    else:
        print('YESSS! you won.')
    

def main():
    while True:
        if input('Want to play Hangman(enter y/n): ').upper() == 'y'.upper():
            hangman()
        else:
            print('see you soon')
            break

if __name__ == '__main__':
    main()




