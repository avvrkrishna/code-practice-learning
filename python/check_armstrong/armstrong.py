def power(x, y):
      '''
      Function to calculate x raised to the power y
      '''
      
    if y == 0:
        return 1
    if y % 2 == 0:
        return power(x, y // 2) * power(x, y // 2)
          
    return x * power(x, y // 2) * power(x, y // 2)
  
def order(x):
      '''
      Function to calculate order of the number
      '''
  
    # Variable to store of the number
    n = 0
    while (x != 0):
        n = n + 1
        x = x // 10
          
    return n
  
def isArmstrong(x):
      '''
      Function to check whether the given number is Armstrong number or not
      '''
      
    n = order(x)
    temp = x
    sum1 = 0
      
    while (temp != 0):
        r = temp % 10
        sum1 = sum1 + power(r, n)
        temp = temp // 10
  
    # If condition satisfies
    return (sum1 == x)
