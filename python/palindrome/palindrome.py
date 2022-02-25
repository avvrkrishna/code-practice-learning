def isPalindrome(s):
    '''
    Palindrome Function to check whether given string is Palindrome or not
    '''
    
    return s == s[::-1]
 
# Sample Input & Output
s = "madam"
ans = isPalindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")
