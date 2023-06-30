'''
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:

Input: s = "hello"
Output: "holle"

Example 2:

Input: s = "leetcode"
Output: "leotcede"
'''

def reverse_vowels(s):
  s = list(s)
  vowels = ['a', 'e', 'i', 'o', 'u']
  left_pointer = 0
  right_pointer = len(s) - 1
  while left_pointer < right_pointer:
    if s[left_pointer].lower() not in vowels:
      left_pointer += 1
    elif s[right_pointer].lower() not in vowels:
      right_pointer -= 1
    else:
      s[left_pointer], s[right_pointer] = s[right_pointer], s[left_pointer]
      left_pointer += 1
      right_pointer -= 1
  return ''.join(s)      
