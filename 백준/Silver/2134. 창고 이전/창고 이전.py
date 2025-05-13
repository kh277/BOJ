# 백준 2134

'''
인부가 몇 명이든 각 인부가 일한 시간에 비례해서 돈을 지불해야 하므로,
1명이 100번 이동시키나 100명이 1번 이동시키나 똑같다.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, M, before, after):
    sumBefore = sum(before)
    sumAfter = sum(after)
    result = 0

    needBox = sumAfter if sumBefore >= sumAfter else sumBefore
    pushBox = 0

    # 이전 창고에서 needBox만큼 꺼내기
    for i in range(N):
        if pushBox + before[i] <= needBox:
            result += before[i] * (i+1)
            pushBox += before[i]
        else:
            result += (needBox - pushBox) * (i+1)
            pushBox = needBox
            break

    # 이후 창고에 pullBox만큼 넣기
    pullBox = pushBox
    for i in range(M):
        if pullBox >= after[i]:
            result += after[i] * (i+1)
            pullBox -= after[i]
        else:
            result += pullBox * (i+1)
            break
    
    return [pushBox, result]


def main():
    N, M, _ = map(int, input().split())
    before = []
    for _ in range(N):
        before.append(int(input()))
    after = []
    for _ in range(M):
        after.append(int(input()))
    print(*solve(N, M, before, after))


main()
