
from src.common_functions import CommonFunctions
from src.nested.python_quiz import PythonQuiz
import numpy
import random 
import pprint

if __name__ == '__main__':
#     #### CREATE OUR GAME
    a = PythonQuiz()
    ## MENU

    #### MAIN LOOP ####
    user_input = ''
    while user_input != 'quit':
        
        print_menu = zip([x for x in 'abcdefghijklmnop'],['guess the ouput type','try entering your own types','multiple choice','guess the index','guess the length'])
        [print(x) for x in print_menu]
        menu = dict(zip([x for x in 'abcdefghi'], a.all_games.values()))
        user_input = input('Select Your Game: ')
        if user_input in menu.keys():
            menu[user_input]()