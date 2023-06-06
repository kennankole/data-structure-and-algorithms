from typing import List

def feasible(nwsp_read_times: List[int], num_cowrks: int, limit: int) -> bool:
  time, num_wrks = 0, 0
  for read_time in nwsp_read_times:
    if time + read_time > limit:
      time = 0
      num_wrks += 1
    time += read_time
  if time != 0:
    num_wrks += 1
  return num_wrks <= num_cowrks

def newspapers_split(newspapers_read_times: List[int], num_coworkers: int) -> int:
  low = max(newspapers_read_times)
  high = sum(newspapers_read_times)
  ans = -1
  while low <= high:
    mid = (low + high) // 2
    if feasible(newspapers_read_times, num_coworkers, mid):
      ans = mid
      high = mid - 1
    else:
      low = mid + 1
  return ans

print(newspapers_split([7,2,5,10,8], 2))