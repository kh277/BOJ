# 백준 11294

import sys

input = sys.stdin.readline
modChange = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']


def formationChange(n, q):
    result = ''

    while n > 0:
        mod = n % q
        n = n // q
        result += modChange[mod]
    
    return result[::-1]


def solve():
    result = [name, ', ', str(num), ', ']
    result.append(str(formationChange(num, formation)))
    return ''.join(result)


# main 함수 ----------
while True:
    name = input().rstrip()
    if name == '#':
        break
    formation = int(input())
    num = int(input())
    print(solve())