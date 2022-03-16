def area_of_triangle(a,b,c):
  '''
  Python Program to find the area of triangle
  '''

  # calculate the semi-perimeter
  s = (a + b + c) / 2

  # calculate the area
  area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
  print('The area of the triangle is %0.2f' %area)

# Driver Code
a = float(input('Enter first side: '))
b = float(input('Enter second side: '))
c = float(input('Enter third side: '))

area_of_triangle(a,b,c)
