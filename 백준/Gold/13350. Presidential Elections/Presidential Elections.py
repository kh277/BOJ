# 백준 13350

'''
i번째 주에서 C당에 투표할 인원은 C_i, F당에 투표할 인원은 F_i이고, 아직 결정되지 않은 인원은 U_i이다.
한 주에서 가장 많은 표를 득표한 당은 +1점을 얻을 때, 가장 많은 점수를 얻은 당이 최종적으로 승리한다.
이 때, C당이 승리하기 위해 설득해야 하는 유권자의 최소 수를 구하는 문제이다.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 10e10


def solve():
    # 각 주마다 승리하기 위해 확보해야 하는 유권자의 수 구하기
    bag = [[0, 0]]
    for i in range(S):
        totalVoter = state[i][1] + state[i][2] + state[i][3]
        needVoter = totalVoter//2 + 1 - state[i][1]

        if needVoter <= state[i][3]:
            bag.append([max(needVoter, 0), state[i][0]])

    allScore = sum([x[0] for x in state])

    # DP[i][score] = i번째 주까지 결과를 취합할 때, score점을 얻기 위해 확보해야 하는 최소 유권자 수
    DP = [[INF for _ in range(allScore+2)] for _ in range(len(bag))]
    DP[0][0] = 0
    maxScore = 0

    # DP 계산
    for curState in range(1, len(bag)):
        cur = bag[curState]
        maxScore += cur[1]
        for curScore in range(maxScore, -1, -1):
            if curScore - cur[1] >= 0:
                DP[curState][curScore] = min(DP[curState][curScore+1], DP[curState-1][curScore], DP[curState-1][curScore-cur[1]]+cur[0])
            else:
                DP[curState][curScore] = min(DP[curState][curScore+1], DP[curState-1][curScore])

    result = INF
    for i in range(allScore//2+1, allScore+1):
        result = min(result, DP[len(bag)-1][i])

    return 'impossible' if result == INF else result


# main 함수 ----------
S = int(input())
state = []
for _ in range(S):
    state.append(list(map(int, input().split())))

print(solve())
