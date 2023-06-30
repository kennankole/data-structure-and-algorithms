from collections import defaultdict
from typing import Counter

def get_minimum_window(original: str, check: str) -> str:
  len_org = len(original)
  len_chk = len(check)
  
  if len_org < len_chk: return ""
  
  def is_smaller(w1, w2):
    if w1[1] - w1[0] == w2[1] - w2[0]:
      for i in range(w1[1] - w2[0]):
        
    

def min_window(s: str, t: str) -> str:
  if t == "": 
    return ""
  count_t = {}
  window = {}
  
  for char in t:
    count_t[char] = 1 + count_t.get(char, 0)

  have = 0
  need = len(count_t)
  result = [-1, -1]
  result_length = float('infinity')
  left = 0
  
  for right in range(len(s)):
    char = s[right]
    window[char] = 1 + window.get(char, 0)
    
    if char in count_t and window[char] == count_t[char]:
      have += 1
      
    while have == need:
      if (right - left + 1) < result_length:
        result = [left, right]
        result_length = (right - left + 1)
      window[s[left]] -= 1
      if s[left] in count_t and window[s[left]] < count_t[s[left]]:
        have -= 1
  left, right = result
  return s[left:right + 1] if result_length != float('infinity') else ""

print(min_window("ADOBECODEBANC", "ABC"))
  