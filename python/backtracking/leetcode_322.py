#https://leetcode.com/problems/coin-change/
from math import inf

def min_coins(coins, amount, sum,memo):
  if sum == amount:
    return 0
  
  if sum > amount:
    return inf
  
  if memo[sum] != -1:
    return memo[sum]
  
  ans = inf
  for coin in coins:
    result = min_coins(coins, amount, sum + coin, memo)
    if result == inf:
      continue
    ans = min(ans, result + 1)
  memo[sum] = ans
  return ans

def coin_change(coins, amount):
  memo = [-1] * (amount + 1)
  result = min_coins(coins, amount, 0, memo)
  return result if result != inf else -1

coins = [1, 2, 5]
amount = 11
print(coin_change(coins, amount))