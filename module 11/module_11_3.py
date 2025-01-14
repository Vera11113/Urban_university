from pprint import pprint
import requests
from Cython.Utils import replace_suffix
import inspect
import math


def instrospection_info(obj):
    info_dict = {}
    methods = []
    attr = []
    info_dict['type'] = type(obj)
    for i in inspect.getmembers(obj):
        if callable(i[1]):
            methods.append(i[0])
        else:
            attr.append(i[0])
    info_dict['Atr'] = attr
    info_dict['methods'] = methods
    info_dict['Module'] = inspect.getmodule(obj)

    return info_dict


number_info = instrospection_info(42)
pprint(number_info)
math_info = instrospection_info(math)
pprint(math_info)




