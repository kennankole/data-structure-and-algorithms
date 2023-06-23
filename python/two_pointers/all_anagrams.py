def find_all_anagrams(original, check):
  original_len = len(original)
  check_len = len(check)
  
  if original_len < check_len:
    return []
  result = []
  check_counter = [0] * 26
  window = [0] * 26
  a = ord('a')
  for i in range(check_len):
    check_counter[ord(check[i]) - a] += 1
    window[ord(original[i]) - a] += 1
  if window == check_counter:
    result.append(0)
  
  for i in range(check_len, original_len):
    window[ord(original[i - check_len]) - a] -= 1
    window[ord(original[i]) - a] += 1
    if window == check_counter:
      result.append(i - check_len + 1)
  return result

print(find_all_anagrams("abab", "ab"))
    