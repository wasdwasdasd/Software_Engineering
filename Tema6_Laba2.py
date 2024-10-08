#Tema6_Laba2

from pprint import pprint

my_dict = {'first': 'so easy'}

def dict_maker(**kwargs):
    my_dict.update(**kwargs)

dict_maker(a = 1, b = 2, c = 3)
dict_maker(name = 'qweqwe', age = 20, weight = 65)

pprint(my_dict)