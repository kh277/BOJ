# 백준 8896

import sys

input = sys.stdin.readline
canUse = {'R': 0, 'P': 1, 'S': 2}


# phase번째 라운드의 승자 체크
def checkWinner(phase, survive):
    useCount = [set() for _ in range(3)]

    # 가위, 바위, 보의 개수를 세서 useCount에 저장
    for i in survive:
        useCount[canUse[robot[i][phase]]].add(i)
    
    # 가위, 바위, 보 중 하나라도 없는 것이 있다면 -> 승부 결정
    for i in range(3):
        if len(useCount[i]) == 0 and len(useCount[(i+1)%3]) != 0 and len(useCount[(i+2)%3]) != 0:
            return useCount[(i+2)%3]

    # 무승부인 경우
    return survive


def solve():
    survive = set()
    for i in range(N):
        survive.add(i)
    
    # 각 페이즈마다 우승한 로봇 저장
    for phase in range(len(robot[0])):
        survive = checkWinner(phase, survive)
        if len(survive) == 0:
            return 0
        elif len(survive) == 1:
            return list(survive)[0]+1
    
    return 0


# main 함수 ----------
T = int(input())
for _ in range(T):
    robot = []
    N = int(input())
    for _ in range(N):
        robot.append(input().rstrip())
    print(solve())
