# 백준 2502

'''
1일차에는 A개, 2일차에는 B개만큼 주었다고 했으니 이후 수열의 값을 계속 계산해보면,
3 - A+B
4 - A+2B
5 - 2A+3B
6 - 3A+5B
7 - 5A+8B
8 - 8A+13B
...
과 같이 된다.

피보나치 수열은 1, 1, 2, 3, 5, 8, ... 이므로
위 수열은 a_i = fib(i-2)*A + fib(i-1)*B 가 된다.
DP를 이용해 값을 구해보자.
'''

import sys

input = sys.stdin.readline
INF = 10e6


def solve(D: int, K: int) -> list:
    fib = [0 for _ in range(D)]
    fib[0] = 0
    fib[1] = 1
    fib[2] = 1
    
    for i in range(3, D):
        fib[i] = fib[i-1] + fib[i-2]

    A = 1
    B = 1
    
    while True:
        while True:
            temp = fib[D-2]*A + fib[D-1]*B
            if temp == K:
                return [A, B]
            elif temp > K:
                break
            else:
                B += 1
        A += 1
        B = 1


def main():
    D, K = map(int, input().split())
    
    for i in solve(D, K):
        print(i)


main()