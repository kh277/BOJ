# 백준 2409

'''
M개의 배낭에 N개의 파이프를 담을 때, 최대로 담을 수 있는 파이프의 개수를 구하는 문제로 보았다.
기본적으로는 이분 탐색으로 담을 수 있는 최대의 파이프 개수를 찾도록 했다.
탐색의 효율을 위해 큰 가방부터, 작은 파이프부터 처리하도록 했다.
사용한 가지치기는 다음과 같다.
- 가방을 순차적으로 탐색할 때, 직전에 실패했던 가방의 용량과 현재 가방의 용량이 같다면 탐색할 필요 없이 불가능하다고 판정한다.
- 배낭에 파이프를 담고 남은 공간에 어떠한 파이프도 들어갈 수 없는 경우 해당 배낭의 남은 공간을 낭비된 용량으로 본다.
탐색 중 전체 배낭의 여유 공간보다 담고자 하는 파이프 총합이 커지는 경우엔 불가능하다고 판정한다.
- 현재 넣은 파이프와 다음에 넣을 파이프의 길이가 같다면, 다음 DFS에서는 0번 배낭이 아닌 현재 탐색한 배낭부터 이어서 탐색한다.
- 현재 배낭의 용량과 파이프의 길이가 일치해 최적의 상태를 만들었음에도 불구하고 이후 DFS 탐색에서 실패한 경우 불가능하다고 판정한다.
- 파이프를 담기 위해 해집합을 탐색한 횟수가 100,000번이 넘어간 경우 불가능하다고 판정한다.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
DFS_COUNT = 0
MAX_COUNT = 100000


# [0, pipeI]의 파이프를 M개의 배낭에 나누어 담을 때, targetK개 만큼의 파이프를 담을 수 있는지 체크
# bagI : 현재 탐색 대상인 배낭의 인덱스, pipeI : bagI번 배낭에 담고자 하는 파이프의 인덱스, waste : 현재까지 낭비된 배낭의 용량
def DFS(M, bag, pipe, targetK, pipeI, bagI, waste):
    global DFS_COUNT

    # 가지치기 : MAX_COUNT만큼 탐색해도 해집합을 찾지 못한 경우
    if DFS_COUNT > MAX_COUNT:
        return False
    DFS_COUNT += 1

    # 종료 조건 : 모든 파이프를 배낭에 다 담은 경우
    if pipeI < 0:
        return True

    # 가지치기 : 낭비된 용량이 너무 많아 필요한 총합을 만들지 못하는 경우
    if totalCapacity - waste < accSum[targetK]:
        return False

    failSize = -1
    for i in range(bagI, M):
        # 가지치기 : 직전에 실패한 배낭과 용량이 같은 경우 스킵
        if i > bagI and bag[i] == bag[i-1]:
            continue

        if bag[i] >= pipe[pipeI] and bag[i] != failSize:
            bag[i] -= pipe[pipeI]

            # 현재 배낭의 빈 부분에 가장 작은 파이프도 들어가지 못하는 경우 낭비된 용량으로 체크
            curWaste = 0
            if bag[i] < pipe[0]:
                curWaste = bag[i]

            # 가지치기 : 다음에 탐색할 파이프의 길이가 같은 경우 현재 배낭부터 이어서 탐색
            nextBagI = 0
            if pipeI > 0 and pipe[pipeI] == pipe[pipeI-1]:
                nextBagI = i

            # 다음 파이프에 대해 탐색
            if DFS(M, bag, pipe, targetK, pipeI-1, nextBagI, waste+curWaste) == True:
                return True

            # 상태 복구 : 넣었던 파이프 꺼내기 및 bag[i] 용량을 가진 배낭에는 현재 파이프가 들어갈 수 없다는걸 체크
            bag[i] += pipe[pipeI]
            failSize = bag[i]

            # 가지치기 : 현재 배낭에서 낭비된 용량이 0인데도 전체 배치가 실패한 경우 불가능 판정
            if bag[i] == pipe[pipeI]:
                break

    return False


def solve(M, N, bag, pipe):
    global totalCapacity, accSum, DFS_COUNT

    totalCapacity = sum(bag)
    bag.sort(reverse=True)
    pipe.sort()

    accSum = [0] * (N+1)
    for i in range(N):
        accSum[i+1] = accSum[i] + pipe[i]

    start = 0
    end = N
    result = 0

    # 아예 불가능한 파이프 개수는 미리 제거
    while end > 0 and accSum[end] > totalCapacity:
        end -= 1

    # 이분 탐색으로 가능한 해집합 찾기
    while start <= end:
        mid = (start + end)//2
        DFS_COUNT = 0
        if DFS(M, bag[:], pipe, mid, mid-1, 0, 0) == True:
            start = mid + 1
            result = mid
        else:
            end = mid - 1

    return result


def main():
    M = int(input())
    bag = list(map(int, input().split()))
    N = int(input())
    pipe = list(map(int, input().split()))

    print(solve(M, N, bag, pipe))


main()
