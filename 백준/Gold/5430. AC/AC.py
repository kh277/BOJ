# 백준 5430

'''
R은 뒤집기 D는 버리기 연산이므로, deque를 사용하면 된다.
R : popleft 대신 pop 사용
D : 상황에 맞는 pop 연산 사용

주의할 점은 배열을 출력할 때 리스트의 원소 사이에 공백이 없어야 한다는 점,
p가 D이고 n이 0일 때 출력은 error가 되어야 하지만,
p가 R이고 n이 0일 때 출력은 []가 되어야 한다는 점이다. 
'''

import sys
from collections import deque

input = sys.stdin.readline


def solve(p: str, n: int, x: list) -> str:
    
  d = deque()
  if n is not 0:
    for i in x:
      d.append(int(i))
    
  reverse = False

  # 모든 연산에 대해 수행
  for i in p:
    # 뒤집기
    if i == 'R':
      reverse = not reverse
      
    # 덱이 비지 않은 경우 버리기
    elif d and i == 'D':
      if reverse:
        d.pop()
      else:
        d.popleft()
      
    # 덱이 비었는데 D 연산이 들어온 경우
    else:
      return "error"
      
  # 결과 출력 
  result = []
  while d:
    if reverse:
      result.append(d.pop())
    else:
      result.append(d.popleft())
    
  return '[' + ','.join(map(str, result)) + ']'
  
  
def main():
  T = int(input())
  for _ in range(T):
    p = input().rstrip()
    n = int(input())
    x = input().rstrip()
    x = list(map(str, x[1:-1].split(',')))
    print(solve(p, n, x), sep=',')


main()