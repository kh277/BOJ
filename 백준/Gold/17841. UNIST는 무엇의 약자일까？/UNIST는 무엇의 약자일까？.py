# 백준 17841

'''
어려움
로직에 문제가 있었는지 모르겠지만 1%에서 계속 틀림.
결국 다른 사람의 풀이를 보고 해결했음.

DP[i][j] = i ~ N-1번까지의 문자열을 이용해서 UNIST[j:5]를 만드는 경우의 수
top-down DP로 해결함.
'''

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**5)
MOD = 1000000007


def recur(stringIndex, curWord):
    # UNIST를 만든 경우
    if curWord >= 5:
        return 1

    # 마지막 단어까지 탐색한 경우
    if stringIndex >= N:
        return 0
    
    # DP에 값이 존재하는 경우
    if DP[stringIndex][curWord] != -1:
        return DP[stringIndex][curWord]
    
    # 현재 단어를 건너뛴 경우 계산
    result = recur(stringIndex+1, curWord)
    for i in range(5-curWord):
        if "UNIST"[curWord+i] != resizeString[stringIndex][i]:
            break
        result = (result + recur(stringIndex+1, curWord+i+1)) % MOD

    DP[stringIndex][curWord] = result

    return result


# main 함수 ----------
N = int(input())
string = []

DP = [[-1 for _ in range(5)] for _ in range(N)]
resizeString = [['' for _ in range(5)] for _ in range(N)]

for i in range(N):
    temp = (input().rstrip())
    for j in range(min(len(temp), 5)):
        resizeString[i][j] = temp[j]

print(recur(0, 0))
