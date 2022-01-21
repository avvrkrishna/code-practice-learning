def sum_of_digits(str1):
    '''
    A function sum_of_digits(s) that takes as input a string s that contains some numbers. 
    The function calculates the sum of all the digits in the string, ignoring any symbols that are not digits.
    '''
    sum = 0
    count = 0
    digits = []
    alphabets = []

    for ch in str1:
        if(ch.isdigit()):
            digits.append(ch)
            sum += int(ch)
            count = count+1
        else:
            alphabets.append(ch)

    updt_str = '+'.join(digits)
    

    if count != 0:
        if str1 != '' and count != 0:
            print('The sum of digits operation performs ' + updt_str)
            print("The extracted non-digits are :",alphabets)
            print(sum)        
        else:   
            print('Empty string entered!')
            print(sum)
    else:
        print("The sum of digits operation could not detect a digit!")
        print("The returned input letters are:",alphabets)
        print(sum)
