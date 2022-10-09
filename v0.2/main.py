from src.nested.python_quiz2 import PQLevelTwo
import numpy
import random 
import pprint

if __name__ == '__main__':
#     #### CREATE OUR GAME
    a = PQLevelTwo()
    ## MENU

    #### MAIN LOOP ####
    user_input = ''
    while user_input != 'quit':
        
        print_menu = zip([x for x in 'abcdefghijklmnop'],['guess the output type','try entering your own types','multiple choice','guess the index','guess the length', 'nested list indexing', 'nested dict indexing'])
        [print(x) for x in print_menu]
        menu = dict(zip([x for x in 'abcdefghi'], a.all_games.values()))
        user_input = input('Select Your Game: ')
        if user_input in menu.keys():
            menu[user_input]()