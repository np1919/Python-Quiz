import numpy
import random
import pandas
import string as string_functions 
import pprint
from ..common_functions import CommonFunctions
from ..python_quiz import PythonQuiz

class PQLevelTwo(PythonQuiz):
    """To practice indexing with nested lists and nested dictionaries"""
    def __init__(self):
        PythonQuiz.__init__(self)
        
        self._all_games.update({'Guess the index (nested lists)':self.guess_the_index_nested,
                                'Nested `dict` indexing practice':self.nested_dict_indexing})
        pass
    

    ### LIST PRACTICE    
    def make_matrix(self, dims=2, width=4):
        """ensures all values are unique"""
        output = []
        for nesting in range(dims-1): #indexing starts at 0
            for i in range(1,width+1):
                row = [self.simple_value() for x in range(width)]
                while len(set(row)) != len(row):
                    row = [self.simple_value() for x in range(width)]
                output.append(row)
        return output

    def nested_list_indexing(self, dims=2, width=4):
        mtrx = self.make_matrix(dims=dims, width=width)
        c = pandas.DataFrame(mtrx).shape
        random_index = random.choice(range(1,c[0]*c[1]+1))
        rows = 0
        while random_index > 3:
            rows += 1
            random_index -= 4
        
        return mtrx, (rows,random_index), mtrx[rows][random_index]
    
    #### DICT PRACTICE 
    
    def keys_and_values(self, size=4):
        base = self.simple_dict(size=size)
        pair_selection = random.choice([x for x in base.keys()]) 
        return base,pair_selection,base[pair_selection]
        
        
    def keys_and_values_nested(self, outer_keys=int,rows=4, size=4):              
        if int == outer_keys:
            base = dict(enumerate([self.simple_dict(size=size) for i in range(rows)]))
        elif str == outer_keys:
            base = dict([(self.make_str(force_length=2), self.simple_dict(size=size)) for i in range(rows)])   
 
        dict_selection = random.choice([x for x in base.keys()]) 
        pair_selection = random.choice([x for x in base[dict_selection].keys()]) 
        return base, dict_selection, pair_selection, base[dict_selection][pair_selection]
        
      
    #### NEW GAMES
    ### GAME G
    def guess_the_index_nested(self,dims=2,width=4):
        response = ''
        while response != 'quit': 

            mtrx, correct_index, correct_value = self.nested_list_indexing(dims=dims,width=width)
            pprint.pprint(mtrx) # only works in anaconda
            response = input(f"What is the 'row and column' (`x,y`) of {correct_value} in the 2-D matrix above? ")
            try:
                response = tuple(eval(response))
            except:
                pass
            if tuple(response) == correct_index:
                self.increment_score()
                pprint.pprint('**** You Win ****!')
            if response != 'quit':
                self.increment_tries()

    ### GAME H
    def nested_dict_indexing(self, outer_keys=int,rows=4, size=4):
        response = ''
        while response != 'quit':

            base, first_index, second_index, value = self.keys_and_values_nested(outer_keys=outer_keys,
                                                                                rows=rows,
                                                                                size=size)
            pprint.pprint(base)
            response = input(f"If this nested dictionary is called `base`, what is the correct way to index for value `{value}`? ")
            if response == 'quit':
                break
            try:
                response = eval(response)
            except:
                response = f'{response}'
            #print(response,  f'base[{first_index}][{second_index}]' )
            if response == value:#f'base[{first_index}][{second_index}]':
                pprint.pprint('**** You Win ****!')
                self.increment_score()
            if response != 'quit':
                self.increment_tries()
