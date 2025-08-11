# 백준 34031

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(A, B):
    # A에서 괄호 처리
    openA = [0 for _ in range(len(A)+1)]
    curBrac = 0
    for i in range(len(A)):
        # 괄호 개수 처리
        if A[i] == '(':
            curBrac += 1
        else:
            curBrac -= 1

        # A의 괄호 개수가 음수가 되면 이후 접두사는 전부 불가
        if curBrac < 0:
            break
        openA[curBrac] += 1

    # B에서 괄호 처리
    openB = [0 for _ in range(len(A)+1)]
    curBrac = 0
    minP = 0
    for i in range(len(B)):
        # 괄호 개수 처리
        if B[i] == '(':
            curBrac += 1
        else:
            curBrac -= 1
        
        # curBrac == minP <= 0일 때만 카운트
        if curBrac <= 0 and curBrac <= minP:
            if -curBrac <= len(A):
                openB[-curBrac] += 1
        if curBrac < minP:
                minP = curBrac

    result = 0
    for i in range(len(A)+1):
        result += openA[i]*openB[i]

    return result


def main():
    A = list(input().decode().strip())
    B = list(input().decode().strip())
    print(solve(A, B))


main()
