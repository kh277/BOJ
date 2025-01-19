# 백준 5543

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve():
    burger.sort()
    drink.sort()
    
    return burger[0] + drink[0] - 50


# main 함수 ----------
burger = []
drink = []
for _ in range(3):
    burger.append(int(input()))
for _ in range(2):
    drink.append(int(input()))

print(solve())