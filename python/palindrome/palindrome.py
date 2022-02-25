def isPalindrome(s):
    return s == s[::-1]
 
# Sample Input & Output
s = "madam"
ans = isPalindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")
