#Python Function to perform arithnmetic operation
def do_arithmetic(x,y,op='add'):
    '''
    Python function do_arithmetic(x,y,op) which takes three input arguments: a number x, a number y, and a string op representing an operation. 
    The function has to perform the operation on the two numbers and return the result
    '''
    operations = ['add','subtract','multiply','divide','+','-','*','/']

    if op.lower() in operations:
        if op.lower() == 'add' or op.lower() == '+':
            print(float(x + y))
        elif op.lower() == 'subtract' or op.lower() == '-':
            print(float(x - y))
        elif op.lower() == 'multiply' or op.lower() == '*':
            print(float(x * y))
        elif op.lower() == 'divide' or op.lower() == '/':
            try:
                print(float(x / y))
            except ZeroDivisionError:
                print('Division by 0!')
    else: 
        print('Unknown operation')
