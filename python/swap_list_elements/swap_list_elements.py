def swapList(newList):
  '''
  To find the length of the list and simply swap the first element with (n-1)th element.
  '''
    size = len(newList)
     
    newList[0], newList[-1] = newList[-1], newList[0]
 
    return newList
     
# Driver code
newList = [12, 35, 9, 56, 24]
print(swapList(newList))
