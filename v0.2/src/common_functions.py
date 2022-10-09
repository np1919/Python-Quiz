import numpy
import random
import pandas
import string as string_functions 


class CommonFunctions:
    
    def __init__(self,):
        pass

    # Functions for Creating an instance of a class -- an instance of a type of object, a particular detail of data


    ### IMMUTABLE TYPES GENERATORS

    def make_bool(self):
        return random.choice([True, False])
    
    ### these functions create a random instance of str;int;float;type respectively
    def make_str(self, random_max_length=8, force_length=False, add_symbols=False):
        """make a random assortment of characters
        chosen from a random range of 1 : random_max_length by default

        input an integer to force_length to a specific value"""
        calculated_length = random.randrange(1,random_max_length)

        if force_length != False:
            calculated_length = force_length
        characters = [x for x in string_functions.ascii_lowercase]
        if add_symbols == True:
            characters += [x for x in """<>?/"':;|\}]{[+=_-*%)($%^&#@!~`"""] 
        reserved_words = ['False','def','if','raise','None','del','import','return','True','elif','in','try','and','else','is','while',
                                  'as','except','lambda','with','assert','finally','nonlocal','sum', 'sorted', 'any', 'all', 'max', 'min'
                                  'yield','break','for','not','class','form','or','continue','global','pass', 'zip', 'enumerate']
        random_words = [''.join([random.choice(characters) for i in range(calculated_length)]).capitalize() for x in range(50)] 
        wordlist = reserved_words + random_words
        if force_length!=False:
            wordlist = [x for x in wordlist if len(x) <= force_length]

        output = random.choice(wordlist)   
    #     if output in self.reserved_names:
    #         print('thats a reserved name in Python')    
        return output

    def make_int(self, scale=50):
        return int(numpy.random.normal(0,scale))

    def make_float(self, scale=50):
        return random.choice([round(x + y,2) for x, y in zip([float(x) for x in numpy.random.normal(0,scale,size=100)], [int(x) for x in numpy.random.random_sample(100)])])

   # def make_type(self, types=[str, list, int, dict, set, tuple, float, type]):
    #    return random.choice(types) # note that we can't actually include `class` in this list, nor to call type() on it

    def make_tuple(self, size=None, types=[str,int,float],
                   #depth=None
                  ):
        """size argument allows you to set the length of the tuple generated"""
        if not size:
            length = int(numpy.random.normal(2, .333))
        else:
            length = size

#         if not depth:
#             width = int(numpy.random.normal(2, .3))

        output = tuple([self.simple_value(types=types) for x in range(length)])
        return output


    def simple_value(self, types=[str,int,float,tuple]):  
        '''links to the functions above, as well as any others we might make'''
        #
        all_types = [bool,str,int,
                 float,tuple,set]
        generators = [self.make_bool, self.make_str, self.make_int,
                      self.make_float, self.make_tuple, self.simple_set]

        mapping = dict(zip(all_types,generators))
        #
        if 'all' in [types]:
            #print('adding all types')
            kind = random.choice(types)
        else:
            kind = random.choice(types)

        # call the mapped function
        value = mapping[kind]()

        return value

    def simple_list(self, size=None, types=[bool,str,int,float, tuple]):
        if not size:
            length = int(numpy.random.normal(3, .667))
        else:
            length = size
        output = [self.simple_value(types=types) for x in range(length)]
        #types = [type(x) for x in outputs]
        return output


    def simple_dict(self, size=None, types=[str,int,float]):
        if not size:
            length = int(numpy.random.normal(3, .667))
        else:
            length = size
        output = {x:y for (x, y) in [(self.simple_value(types=types),self.simple_value(types=types)) for x in range(length)]}

        return output
    
    
    def simple_set(self, size=None, types=[str,int,float]):
        if not size:
            length = int(numpy.random.normal(3, .667))
        else:
            length = size
            
        output = set(self.simple_list(length, types=types))
        output = set(output)

        return output