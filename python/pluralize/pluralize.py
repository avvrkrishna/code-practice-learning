# CMT309 - CMT314 2021-2022 Coursework Q2 Test Code
# Oktay Karakus, PhD
# ************************************************************************************
def pluralize(word):
    '''
    1) Please copy and pass your codes for pluralize() function below.
    2) Do required changes in function definition for the arguments if needed.
    '''
    dict = {}

    vowels = ['a','e','i','o','u']
    my_file = open("proper_nouns.txt","r")
    content = my_file.read()
    #print(content)

    content_list = content.split("\n")
    my_file.close()
    #print(content_list)

    if word == '':
        dict['plural'] =  ''
        dict['status'] = 'empty_string'
        print(dict)
    elif word.lower() in content_list:
        dict['plural'] =  word
        dict['status'] = 'proper_noun'
        print(dict)
    elif word[-3:].lower() == 'ies' or word[-2:].lower() == 'es' or word[-1:] == 's':
        dict['plural'] =  word
        dict['status'] = 'already_in_plural'
        print(dict)
    elif word[-1:].lower() in vowels:
        dict['plural'] = word + 's'
        dict['status'] = 'success'
        print(dict)
    elif word[-2:].lower() == 'sh' or word[-2:] == 'ch' or word[-1:] == 'z':
        dict['plural'] = word + 'es'
        dict['status'] = 'success'
        print(dict)
    elif word[-1:].lower() == 'f':
        dict['plural'] = word[:-1] + 'ves'
        dict['status'] = 'success'
        print(dict)
    elif word[-1:].lower() == 'y' and word[-2:-1].lower() not in vowels:
        dict['plural'] = word[:-1] + 'ies'
        dict['status'] = 'success'
        print(dict)
    else:
        dict['plural'] = word + 's'
        dict['status'] = 'success'
        print(dict)


pluralize('failure')
pluralize('food')
pluralize('Zulma')
pluralize('elf')
pluralize('computers')
pluralize('PCs')
pluralize('')