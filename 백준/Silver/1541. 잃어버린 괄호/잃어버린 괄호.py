# 백준 1541

'''
먼저 어느 상황에 계산 값이 작아지는지 생각해보면,
- 뒤에 오는 숫자들이 커질수록 값이 작아질 것이다.
따라서 계산 값이 가장 작아지는 경우는 - 뒤에 오는 +들을 전부 묶는 경우이다.
예시로 a+b-c-d+e+f-g라고 치면, 최소값은 a+b-(c)-(d+e+f)-(g)가 된다.

다음으로 생각해야 할 것은 주어진 문자열을 어떻게 나누는가이다.
split()을 사용해서 문자열을 -를 기준으로 자를 경우, 첫 번째 값만 +, 나머지 뒤의 값은 전부 -가 된다.
따라서 -를 기준으로 자르고, 남은 값들을 +를 기준으로 자르고 전부 더하면 된다.
'''

import sys

input = sys.stdin.readline


def solve(expr: str):
  num = list(map(str, expr.split('-')))
  result = 0
  
  # 첫 번째 분할 계산
  split_1 = list(map(str, num[0].split('+')))
  for i in split_1:
    result += int(i)
      
  # 두 번째 이후 분할
  if len(num) > 1:
    
    # 모든 분할에 대해
    for i in range(1, len(num)):
      split_2 = list(map(str, num[i].split('+')))
      temp = 0
      
      # +로 잘린 숫자를 더하기
      for j in split_2:
        temp += int(j)
      result -= temp
        
  return result
  
  
def main():
  expr = input()
  print(solve(expr))
  

main()
