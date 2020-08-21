'''
Checks if the string entered by the user is a palindrome. That is that it reads the same forwards as backwards like “racecar”
'''


def palindrome(n):
    if n == n[::-1]:
        return True
    else: return False


print(palindrome("racecar"))
print(palindrome("sure"))
