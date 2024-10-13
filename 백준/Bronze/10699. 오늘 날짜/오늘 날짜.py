# 백준 10699


import sys
from datetime import datetime

input = sys.stdin.readline


def solve():
    now = datetime.now()
    return "{a}-{b}-{c}".format(a=now.year, b=now.month, c=now.day+1)


# main 함수 ----------
print(solve())
