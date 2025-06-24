# 백준 4096

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


# 1334번 코드 참고
def nextPelin(N):
    length = len(N)

    if all(i == '9' for i in N):
        return '1' + '0'*(length-1) + '1'

    if length == 1:
        return str(int(N[0]) + 1)

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

    half = N[:(length+1)//2]
    for i in range(-1, -len(half)-1, -1):
        half[i] = str(int(half[i]) + 1)
        if half[i] == '10':
            half[i] = '0'
        else:
            if length % 2 == 0:
                return half + half[::-1]
            else:
                return half + half[:-1][::-1]


def solve(N):
    for i in range(len(N)//2+1):
        # 팰린드롬이 아니면 다음 팰린드롬 수와의 차이 구하기
        if N[i] != N[len(N)-i-1]:
            return int(''.join(nextPelin(list(N)))) - int(N)

    return 0


def main():
    while True:
        N = input().decode().rstrip()
        if N == '0':
            break
        print(solve(N))


main()
