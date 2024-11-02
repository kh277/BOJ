# 백준 27889

import sys

input = sys.stdin.readline


def solve():
    if string == 'NLCS':
        return 'North London Collegiate School'
    elif string == 'BHA':
        return 'Branksome Hall Asia'
    elif string == 'KIS':
        return 'Korea International School'
    else:
        return 'St. Johnsbury Academy'


# main 함수 ----------
string = input().rstrip()
print(solve())
