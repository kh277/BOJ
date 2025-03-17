# 백준 33615

'''
3의 배수인 경우 -> 3의 배수
3의 배수 + 1인 경우
    1이 있는 경우 -> 1을 빼면 3의 배수가 됨
    1이 없는 경우 -> 5의 배수
3의 배수 + 2인 경우
    5가 있는 경우 -> 5를 빼면 3의 배수가 됨
    5가 없는 경우
        기존 수가 11로 나눠떨어짐 -> 11의 배수
        기존 수가 11로 나눠떨어지지 않음 -> 1을 빼면 11의 배수
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N):
    one = []
    five = []
    for i in range(len(N)):
        if N[i] == '1':
            one.append(i)
        else:
            five.append(i)
    
    # 수가 3의 배수인 경우
    if (len(one)*1 + len(five)*5) % 3 == 0:
        return [0, 3]
    
    # 수가 3의 배수 + 1인 경우
    elif (len(one)*1 + len(five)*5) % 3 == 1:
        # 1이 1개 이상 있는 경우
        if len(one) > 0:
            return [one[0]+1, 3]
        # 1이 하나도 없는 경우
        else:
            return [0, 5]

    # 수가 3의 배수 + 2인 경우
    elif (len(one)*1 + len(five)*5) % 3 == 2:
        # 5가 1개 이상 있는 경우
        if len(five) > 0:
            return [five[0]+1, 3]
        # 5가 하나도 없는 경우 (1로만 이루어진 경우)
        else:
            if int(N) % 11 == 0:
                return [0, 11]
            else:
                return [one[0]+1, 11]


def main():
    T = int(input())
    for _ in range(T):
        N = input().decode().rstrip()
        print(*solve(N))


main()