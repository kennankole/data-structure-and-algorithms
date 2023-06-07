from typing import List
'''
Given a phone number that contains digits 2-9, 
find all possible letter combinations the phone number could translate to.
Problem template

function dfs(start_index, path):
  if is_leaf(start_index):
    report(path)
    return
  for edge in get_edges(start_index):
    path.add(edge)
    dfs(start_index + 1, path)
    path.pop()
'''

KEYBOARD = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}

def letter_combination_of_phone_number_digits(digits: str) -> List[str]:
  def dfs(start_index, path):
    if start_index == len(digits):
      res.append(''.join(path))
      return
    next_number = digits[start_index]
    for letter in KEYBOARD[next_number]:
      path.append(letter)
      dfs(start_index + 1, path)
      path.pop()
  res = []
  dfs(0, [])
  return res

print(letter_combination_of_phone_number_digits('23'))