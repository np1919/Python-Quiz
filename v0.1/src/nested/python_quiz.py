import numpy
import random
import pandas
import string as string_functions 

from src.common_functions import CommonFunctions

class PythonQuiz(CommonFunctions):
            
    def __init__(self, types=[bool, int, float, str, tuple, list, dict, set]):
        CommonFunctions.__init__(self)
#         self.all_types = types 
        self.immutable_types = [bool, str, int, float, tuple]
#         self.mutable_types = [list, dict, set]
#         self.iterable_types = [str, tuple, set, list, dict] # bool, int, and float types are NOT ITERABLE --> use a pandas Series, or even a list to construct data
        
        self.sos = 25
        self.simple_examples = dict()
        for x in self.immutable_types:
            self.simple_examples[x] = self.simple_list(self.sos, types=[x])
        self.simple_examples[dict] = [self.simple_dict() for x in range(self.sos)]
        self.simple_examples[list] = [self.simple_list() for x in range(self.sos)]
        self.simple_examples[set] = [self.simple_set() for x in range(self.sos)]   



#         self.tries = 0
#         self.correct = 0
#         if response == 'score':
#             print(f"Not including this entry, you've made {tries} attempts and gotten {correct} right. That's {round(correct/tries*100,1)}%!")
#             continue 
#         @property
#         def all_examples(self):
#             return self.simple_examples + self.complex_examples
#         # check the length of all sub-lists? if there's more than a double nesting it might be bad.
#         pass

        self._all_games = [self.guess_the_output_type, self.input_a_type, self.multiple_choice,
                          self.guess_the_len, self.guess_the_index]
    @property
    def all_games(self):
        return dict(enumerate(self._all_games))
    
    @property
    def all_types(self):
        return list(self.simple_examples.keys())
    
    
    # GAME A #   
    def guess_the_output_type(self, types=[bool,str,int,float,tuple,list,set,dict]):

        response = ''
        while response != 'quit':
            response = ''

            # pick a 'type' 
            type_index = numpy.random.randint(0, high=len(self.all_types))
            type_selection = self.all_types[type_index]
            # select a question from that list
            question_index = numpy.random.randint(0, high=len(self.simple_examples[type_selection]))
            question_selection = self.simple_examples[type_selection][question_index]   
            # set the answer of the question
            answer = type(question_selection)
            print([question_selection])
            response = input(f"Enter the type.__name__ attribute of the object [enclosed in square brackets]: ")
            if response=='':
                continue
            if response == answer.__name__:
                print(f'You win!')
            print(f"{question_selection} is a {answer}. You picked {response}")

            #tries += 1


    # GAME B #
    def input_a_type(self):
        response = ''
        while response != 'quit':
            response = input('Enter your code below, and it will tell you its Python `type`. Remember, you can always use `type()` or `isinstance()` to check the type of your variables in a notebook. ')
            if response == 'quit':
                break
            try:
                response = eval(response)
            except:
                print(response, "failed")
                print('Woops, converting that to a string. Did you mean to enclose that in quotes?')
                response = f'"{response}"'
#             if response in self.exceptions:
#                 print('thats a reserved name in python!')
#                 if response in self.symbols:
#                     print('almost all symbols can be used in Python syntax, one way or another -- even in Pandas')
#                 if response in self.reserved_names:
#                     print('that name already has a definition in Python syntax')
            print(f"`{response}` is a {type(response)}. Nice!")
            print()

    # GAME C #
    def multiple_choice(self, length_of_values=4):
        #[[type(x) for x in y] for y in PythonQuiz().make_nested_list()]   
        
        response = ''
        while response != 'quit':
            output_dict = dict()
            choices = ['a','b','c','d']
            right_answer = choices.pop(choices.index(random.choice(choices)))   
            input_list = self.simple_list(size=length_of_values)
            output_dict.update({right_answer:[type(x).__name__ for x in input_list]}) 
            for remaining in choices:
                output_dict.update({remaining:[random.choice([x for x in self.all_types if x not in output_dict.values()]).__name__ for x in range(len(input_list))]})
            print(f"What are the types of the elements inside the following list? {input_list}")
            print()
            [print(x) for x in sorted(output_dict.items())]
            response = input("Select your answer: ")
            if response == right_answer:
                print('You win!')
                print()
            output_dict.clear()
    

    ## GAME D ###
    def guess_the_len(self):
        response = ''
        while response != 'quit':
            a = random.choice([self.simple_list(), self.simple_dict(), self.simple_value(types=[str]), self.simple_set()])
            if type(a) == str:
                print(f"'{a}'")
            else:
                print(a)
            response = input(f"What is the len() of the above data container? Hint: it's a {type(a)} ")
            if response == 'quit':
                break
            if len(a) == int(response):
                print('You win!')
                print()
     
    ## GAME E ##   
    def guess_the_index(self):
        """guess the index of an element in the container. list; dict; or str"""
        response = ''
        while response != 'quit':
            temp = random.choice([a.simple_list(), a.simple_dict(), a.simple_value(types=[str])])
            my_index = random.choice(range(len(temp)))

            if type(temp) == dict: 
                key = list(temp.keys())[my_index]
                #print(list(temp.values())[my_index])


            else:
                if len(set(temp)) != len(temp):
                    continue

                key = my_index

            print(temp) 
            print() # the value at the key

            print(f"What is the index of {temp[key]} in the above container?")
            
            response = input("")
            
            if response == 'hint':
                print(f"Hint: its a {type(temp)}")
                
            try:
                if temp[eval(response)] == temp[key]:
                    print('You win!')
            except:
                pass
              #  print()

