def swapList(newList):
  '''
  To find the length of the list and simply swap the first element with (n-1)th element.
  '''
    size = len(newList)
     
    # Swapping
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp
     
    return newList
     
# Driver code
newList = [12, 35, 9, 56, 24]
