# 백준 1946

'''
서류 성적을 오름차순으로 정렬한 뒤, 면접 성적을 하나씩 체크한다.
현재 지원자의 면접 성적이 이전에 체크했던 모든 면접자보다 작다면 그 지원자는 선발할 수 있다.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, score):
    score.sort(key= lambda x: x[0])
    candidate = 0
    beforeMin = N+1
    for i in range(N):
        _, scoreB = score[i]
        if scoreB < beforeMin:
            candidate += 1
            beforeMin = scoreB
    
    return candidate


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        score = []
        for _  in range(N):
            score.append(list(map(int, input().split())))
        print(solve(N, score))


main()