"""
Decode Variations
A letter can be encoded to a number in the following way:

'A' -> '1', 'B' -> '2', 'C' -> '3', ..., 'Z' -> '26'
A message is a string of uppercase letters, and it is encoded first using this scheme. For example, 'AZB' -> '1262'

Given a string of digits S from 0-9 representing an encoded message, return the number of ways to decode it.

Examples:

input:  S = '1262'
output: 3
explanation: There are 3 messages that encode to '1262': 'AZB', 'ABFB', and 'LFB'.
"""

def decodeVariations(s):
  if not s:
    return 0
  n=len(s)
  dp=[0]*(n+1)
  dp[0]=1
  dp[1]=1 if s[0]!=0 else 0
  for i in range(2,n+1):
    if s[i-1]!='0':
      dp[i]+=dp[i-1]
    
    if 10<=int(s[i-2:i])<=26:
      dp[i]+=dp[i-2]
  return dp[n]
  