# 백준 2631

'''
LIS 문제와 같다.

전체 학생 수에서 LIS를 빼면 답이 된다.
'''


import sys

input = sys.stdin.readline


def solve(N: int, student: list) -> int:
    DP = [1 for i in range(N+1)]
    
    for i in range(1, N):
        cur = student[i]
        for j in range(0, i):
            if student[j] < student[i]:
                DP[i] = max(DP[i], DP[j]+1)
    
    return N - max(DP)


def main():
    N = int(input())
    
    student = []
    for i in range(N):
        student.append(int(input()))
    
    print(solve(N, student))


main()