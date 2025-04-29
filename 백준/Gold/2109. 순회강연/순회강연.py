# 백준 2109

'''
마감 시간과 가치가 주어질 때, 가치를 최대로 만들도록 스케줄링하기.
-> 가치 내림차순, 마감 시간 오름차순으로 정렬 후, 가장 늦은 시간에 작업 할당.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, task, maxD):
    visited = [False for _ in range(maxD)]
    task.sort(key= lambda x: (-x[0], x[1]))

    result = 0
    for i in range(N):
        curCost, curD = task[i]
        for j in range(curD-1, -1, -1):
            if visited[j] == False:
                visited[j] = True
                result += curCost
                break

    return result


def main():
    N = int(input())
    task = []
    maxD = 0
    for _ in range(N):
        a, b = map(int, input().split())
        task.append([a, b])
        maxD = max(maxD, b)
    
    print(solve(N, task, maxD))


main()
