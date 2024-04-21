# 백준 1676


import sys

input = sys.stdin.readline

def solve(N: int) -> list:
    result = [0, 0]

    for i in range(1, N+1):
        temp = i
        
        while True:
            if temp % 2 == 0:
                result[0] += 1
                temp = temp // 2
                continue
            elif temp % 5 == 0:
                result[1] += 1
                temp = temp // 5
                continue

            else: # 더 이상 2와 5로 나눠떨어지지 않는 경우
                break

    return min(result)


def main():
    N = int(input())
    print(solve(N))


main()