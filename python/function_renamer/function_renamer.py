#Importing required libraries
import re
from re import sub

def function_renamer(str1):
    '''
    Function to rename the function names in given string to camelcase and return the output
    1. The original input with modified function names
    2. A dictionary which provides hash value, camelcase version of function and all caps version
    '''
    d = {}
    camel_dict = {}
    func_names = []
    start = 'def'
    end = '('

    func_count = str1.count(start)
    for i in range(func_count):
        func_names.append(re.findall(re.escape(start)+"(.*)"+re.escape(end),str1)[i].strip())

    #print(func_names)

    for i in func_names:
        joined_str = ''
        modified_str = ''
        new_str = i.split('_')
        capitalize_str = []
        for j in new_str:
            capitalize_str.append(j.capitalize())
        
        for k in range(len(capitalize_str)):
            if len(capitalize_str[k]) !=0:
                joined_str+= capitalize_str[k]
            else:
                modified_str+= '_'
        camel_dict[i]= modified_str+joined_str

    #print(camel_dict)

    for func in func_names:
        d[func] = {}
        d[func]['hash'] = hash(func)
        if '_' not in func:
            d[func]['camelcase'] = func
        else:
            d[func]['camelcase'] = camel_dict[func]
        d[func]['allcaps'] = func.upper()
        
    for i in range(len(func_names)):
        temp = str1.replace(func_names[i], d[func_names[i]]['camelcase'])
        str1 = temp

    print(temp)
    print(d)

text= '''def __add_two_numbers(a,b):
               return a + b
           print(__add_two_numbers(10,20))
           def _check_truth(t= True):
               print('t is ',t)
           def MajorSplit(k,m):
               return k.split(m)
               _check_truth(False)
           MajorSplit('hello','h')'''
function_renamer(text)
