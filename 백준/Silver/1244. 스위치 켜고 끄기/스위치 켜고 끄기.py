# 백준 1244

import sys

input = sys.stdin.readline


def solve(N: int, switch: list, case: int, simul: list) -> list:
    # 스위치의 값을 0, 1에서 False, True로 변경
    for i in range(N):
        if switch[i] == 1:
            switch[i] = True
        else:
            switch[i] = False

    for i in range(case):
        cur = simul[i][1]
        # 남학생이라면
        if simul[i][0] == 1:
            for j in range(cur, N+1, cur):
                switch[j-1] = not switch[j-1]
        
        # 여학생이라면
        if simul[i][0] == 2:
            count = 0
            while cur+count <= N and cur-count >= 1:
                if switch[cur+count-1] == switch[cur-count-1]:
                    count += 1
                else:
                    break

            for j in range(cur-count+1, cur+count):
                switch[j-1] = not switch[j-1]

    # False, True를 0, 1로 변경
    switch = [1 if i == True else 0 for i in switch]

    # 리스트를 20개씩 분할
    return [switch[i:i+20] for i in range(0, len(switch), 20)]


def main():
    N = int(input())
    switch = list(map(int, input().split()))

    case = int(input())
    simul = []
    for i in range(case):
        simul.append(list(map(int, input().split())))

    for i in solve(N, switch, case, simul):
        print(*i)


main()
