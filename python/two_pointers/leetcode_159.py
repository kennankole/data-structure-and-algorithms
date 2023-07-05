'''
Given a string s, return the length of the longest substring that contains at most two distinct characters.

Example 1:

Input: s = "eceba"
Output: 3
Explanation: The substring is "ece" which its length is 3.

Example 2:

Input: s = "ccaabbb"
Output: 5
Explanation: The substring is "aabbb" which its length is 5.

Constraints:

1 <= s.length <= 105
s consists of English letters.
'''

def length_of_longest_substring(s):
  last_occurence = dict()
  max_length = 0
  slow = 0
  for fast in range(len(s)):
    last_occurence[s[fast]] = fast
    fast += 1
    if len(last_occurence) == 3:
      # remove the smaller last_occurrence[char] 
      # to maintain a longers substring
      slow = min(last_occurence.values()) + 1
      del last_occurence[s[slow - 1]]
    max_length = max(max_length, fast - slow)
  return max_length
s = "eceba"
s2 = "ccaabbb"
print(length_of_longest_substring(s))


'''
In the given implementation, slow is used to track the starting index of the current substring. 
When we encounter a character that violates the constraint of having at most two distinct characters, 
we need to adjust the slow index to maintain the longest substring with at most two distinct characters.

By setting slow = min(last_occurrence.values()) + 1, 
we are moving the slow index to the position right after the earliest 
occurrence of the character that needs to be removed. 
Adding 1 ensures that the character at slow is not included in the new substring. 
It allows us to exclude the character and start a new substring right after it.

Let's go through an example to understand this better:

Suppose we have the input string s = "eceba". 
The variable last_occurrence is used to store the indices of the last 
occurrences of characters encountered so far. 
Here's how the algorithm works step-by-step:

Initially, slow = 0 and fast = 0. 
We encounter the character 'e' and update last_occurrence['e'] = 0.

Now, fast moves to the next position. 
We encounter the character 'c' and update last_occurrence['c'] = 1.

Since the number of distinct characters (2) is still within the limit, we continue.

fast moves to the next position. 
We encounter the character 'e' again. 
Now, last_occurrence['e'] = 2.

The number of distinct characters (2) is still within the limit.

fast moves to the next position. We encounter the character 'b' for the first time. 
Now, last_occurrence['b'] = 3.

The number of distinct characters (3) exceeds the limit (2). 
We need to adjust the slow index to maintain the longest substring with at most two distinct characters.

We calculate slow = min(last_occurrence.values()) + 1 = min([0, 1, 2]) + 1 = 1 + 1 = 2. 
So, slow becomes 2.

At this point, we have the substring 'ece' from indices 2 to 4, 
which is the longest substring with at most two distinct characters encountered so far.

The + 1 in slow = min(last_occurrence.values()) + 1 is necessary 
to exclude the character at the slow index from the new substring. 
It allows us to start a fresh substring right after the earliest 
occurrence of the character that needs to be removed.

In summary, adding 1 to slow ensures that the new substring starts 
from the next position after excluding the character that violates 
the constraint of having at most two distinct characters.
'''

  
