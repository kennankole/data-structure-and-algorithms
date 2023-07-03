'''
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. 
Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.

Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

Example 2:

Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.

Example 3:

Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"]. 
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".

Constraints:

1 <= chars.length <= 2000
chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.
'''
def compress(char):
  def compress_char(write, curr, counter):
    char[write] = curr
    write += 1
    if counter == 1:
      return write
    length = str(counter)
    for c in length:
      char[write] = c
      write += 1
    return write
  write = 0
  counter = 1
  curr = char[0]
  for read in range(1, len(char)):
    if char[read] == curr:
      counter += 1
    else:
      write = compress_char(write, curr, counter)
      counter = 1
    curr = char[read]
  write = compress_char(write, curr, counter)
  return write

def compressing(chars):
  slow_ptr = 0
  fast_ptr = 0
  
  while fast_ptr < len(chars):
    count = 1
    while fast_ptr + 1 < len(chars) and chars[fast_ptr] == chars[fast_ptr + 1]:
      count += 1
      fast_ptr += 1
    chars[slow_ptr] = chars[fast_ptr]
    slow_ptr += 1
    
    if count > 1:
      for digit in str(count):
        chars[slow_ptr] = digit
        slow_ptr += 1
    fast_ptr += 1
  return  slow_ptr
    

chars = ["a","a","b","b","c","c","c"]
print(compressing(chars))
