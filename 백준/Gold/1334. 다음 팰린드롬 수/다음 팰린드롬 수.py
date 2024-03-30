# 백준 1334

import sys

input = sys.stdin.readline


def solve(N: list) -> list:
    length = len(N)

    # 0. N이 9로만 이루어진 경우 (ex: 999 -> 정답은 : 1001)
    if all(i == '9' for i in N):
        return '1' + '0'*(length-1) + '1'
      
    # 0. N이 한 자리일 경우 (ex: 3 -> 정답은 4)
    if length == 1:
        return str(int(N[0]) + 1)
    
    # 0. 대칭시킨 수가 N보다 작을 경우 (ex: 1234111 -> 정답은 1234321)
    for i in range((length-1)//2, -1, -1):
        if N[i] == N[-i-1]:
            continue
        elif N[i] >= N[-i-1]:          
            temp = N[:length//2]
            if length % 2 == 0:
                return temp + temp[::-1]
            else:
                return temp + [N[length//2]] + temp[::-1]
        else:
            break

    # 1. N에서 축을 포함한 앞 반쪽만 추출한다
    half = N[:(length+1)//2]

    # 2. 중앙 축에서부터 1을 증가시킴
    # ex: 123456의 경우 -> 123만 따로 추출한 후 1 증가시키고 반전 -> 124421
    for i in range(-1, -len(half)-1, -1):
        half[i] = str(int(half[i]) + 1)
        # 2-1. 반올림이 되는 경우
        if half[i] == '10':
            half[i] = '0'
        # 2-2. 바로 종료되는 경우
        else:
            if length % 2 == 0:
                return half + half[::-1]
            else:
                return half + half[:-1][::-1]


def main():
    N = input().rstrip()
    print(''.join(solve(list(N))))


main()
