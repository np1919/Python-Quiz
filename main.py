import numpy
import random
import pandas
import string as string_functions 

class PythonQuiz:

    def __init__(self, types=[str, list, int, dict, set, tuple, float]):
        self.size_of_sample=26
        self.all_types = types 
        
        # not necessarily accurate or extensive...
        self.symbols = [x for x in """<>?/"':;|\}]{[+=_-*%)($%^&#@!~`"""]
        self.reserved_names = ['False','def','if','raise','None','del','import','return','True','elif','in','try','and','else','is','while',
                              'as','except','lambda','with','assert','finally','nonlocal',
                              'yield','break','for','not','class','form','or','continue','global','pass']
        self.exceptions = self.symbols + self.reserved_names
        #print(symbols, "are reserved symbols and operators")
        #print(reserved_names, "are some reserved names in Python")
        
        

        self.all_examples = {bool : [True, False], 
                             # only two boolean values
                         str : ['StackAdapt'] + [str(y) for y in numpy.random.choice([x for x in string_functions.ascii_lowercase.upper() + string_functions.ascii_lowercase], size=self.size_of_sample)] + ['%','/','//','+','-','*'],
                             # 
                             
                         int : [int(x) for x in numpy.random.randint(-100,100,self.size_of_sample)],
                         float : [round(x + y,2) for x, y in zip([float(x) for x in numpy.random.normal(0,50,size=self.size_of_sample)], [int(x) for x in numpy.random.random_sample(self.size_of_sample)])],
                         type : [x for x in self.all_types],

                         tuple : [(1,2),('one',2),(7,(12,14)),('str',7)],
                         list : [[0],['0'],['one',sum], ['a','1'],[[1,'2'],['three','four']],['seven','eight']],
                         dict : [{'a':1, 2:'b'},{1:'a', 'three':'c'},{(12,14):['a','b'], 'a':'2'}],
                         set : [{1,2,3},{314,1},{0,1,1,2,3,5,7}],}
        
        #self.exceptions = [str(f'{x.__name__}') for x in self.all_types] +  + ['%','/','//','+','-']    
        #self.single_value_options = [bool, str, int, float]
        #self.data_container_options = [tuple,list,dict,set]
        # + list(__builtins__.__dict__.keys())

    
    def make_container(self
                      ,kind=list
                      ,length=4
                      ,restrict_values=[]):
        assert kind in [list,dict,set,tuple], 'thats not a container'

        if len(restrict_values) == 0:
            restrict_values = self.all_types
        immutable_keys = []
        [[immutable_keys.append(y) for y in self.all_examples[x]] for x in [tuple,str,int,float, type]]
          
        potential_values = []
        [[potential_values.append(y) for y in self.all_examples[x]] for x in restrict_values]

        if kind == dict:
            output = {k:v for k,v in [(random.choice(immutable_keys),random.choice(potential_values)) for i in range(length)]}        
        if kind == list:
            output = [random.choice(potential_values) for i in range(length)]  
        if kind == set:
            output = set(random.choice(immutable_keys) for i in range(length))
        if kind == tuple:
            output =  tuple(random.choice(immutable_keys) for i in range(length))
        
        return output
    
    
    def make_nested_list(self,length=4):
        
        # we don't have enough list examples so far. I want to experiment with slicing and indexing in lists and tuples
        for i in range(10):
            self.all_examples[list] += self.make_container(list)

        return [self.make_container(list, restrict_values=[list]) for i in range(length)]
    
            
    # GAME A #   
    def guess_the_output(self):
        response = ''
        while response != 'quit':
            response = ''

            # pick a 'type' 
            type_index = numpy.random.randint(0, high=len(self.all_types))
            type_selection = self.all_types[type_index]
            # select a question from that list
            question_index = numpy.random.randint(0, high=len(self.all_examples[type_selection]))
            question_selection = self.all_examples[type_selection][question_index]   
            # set the answer of the question
            answer = type(question_selection)
            print('What Python built-in type is the following output?', question_selection)
            response = input("Enter the type.__name__ attribute : ")

            if response == answer.__name__:
                print('You win!')
            print(f"{question_selection} is a {answer}. You picked {response}")
    
    # GAME B #
    def input_a_type(self):
        response = ''
        while response != 'quit':
            response = input('Enter your code below, and it will tell you its Python `type`. Remember, you can always use `type()` or `isinstance()` to check the type of your variables in a notebook.')
            try:
                response = eval(response)
            except:
                print(response, "failed")
                print('Woops, converting that to a string. Did you mean to enclose that in quotes?')
                response = f'{response}'
            if response in self.exceptions:
                print('thats a reserved name in python!')
                if response in self.symbols:
                    print('almost all symbols can be used in Python syntax, one way or another -- even in Pandas')
                if response in self.reserved_names:
                    print('that name already has a definition in Python syntax')
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
            input_list = self.make_container(list, length=length_of_values)
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
    def guess_the_len(self, types=[list,dict,tuple,str]):

        response = ''
        while response != 'quit':
            a = self.single_value
            print(a)
            response = input("What is the len() of the above? ")
            
            if len(a) == int(response):
                print('You win!')
                print()
                
    ####
    @property
    def single_value(self, types=[]):     
        """generate a random value from all examples in self.examples which are in `types`"""
        if len(types) == 0:
            types = self.all_types
        available =  random.choice([[y for y in self.all_examples[x]] for x in types])
        return random.choice(available)
            

if __name__ == '__main__':
    #### CREATE OUR GAME
    a = PythonQuiz()
    a.guess_the_len()
    ### MENU
#     print_menu = {'a':'guess the type',
#                   'b':'try entering your own types',
#                   'c':'multiple choice'}
    
#     menu = {'a':a.guess_the_output,
#             'b':a.input_a_type,
#             'c':a.multiple_choice}
    
#     #### MAIN LOOP ####
#     user_input = ''
#     while user_input != 'quit':
#         [print(f"{x} : {y}") for x,y in print_menu.items()]

#         #print(print_menu)
#         user_input = input('Select Your Game: ')
#         if user_input != 'quit':
#             menu[user_input]()
#         else:
#             pass
