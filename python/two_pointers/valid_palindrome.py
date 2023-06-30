def is_palindrome(s):
  return s[:] == s[::-1]

def valid_palindrome(s):
  left = 0
  right = len(s) - 1
  while left < right:
    if s[left] != s[right]:
      return is_palindrome(s[left+1:right+1]) or is_palindrome(s[left:right])
    left += 1
    right -= 1
  return True
    
print(valid_palindrome('abca'))
print(is_palindrome('b'))