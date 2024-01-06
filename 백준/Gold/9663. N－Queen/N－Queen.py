# 백준 9663

'''
퀸의 위치를 파악하기 위해 이차원 배열을 사용할 수도 있지만,
한 행에 퀸이 2개가 들어갈 수 없으므로 퀸의 위치만 나타내는 일차원 배열을 사용하면 더 빠르게 처리할 수 있다.
이 경우, [0행에서 퀸이 위치한 열, 1행에서 퀸이 위치한 열, ..., N-1행에서 퀸이 위치한 열] 와 같이 표현한다.

전체적인 알고리즘
1. 한 행에서 0 ~ N-1까지 유망성을 판단한다.
2. 유망한 경우, 현재 배치된 퀸의 위치 리스트를 인자로 넘겨주면서 다음 행에 대해 탐색한다.
3. 마지막 행까지 탐색 성공한 경우 개수를 1 증가시킨다.

주의할 점
python으로 실행할 경우 시간이 부족하므로 PyPy3로 실행하여 통과할 수 있다.
'''

import sys
input = sys.stdin.readline


def promising(arr: list, row: int) -> bool:
    # 이미 퀸이 배치된 줄에 대해 반복
    for i in range(row):
        # 세로줄, 대각선에 퀸이 존재하는지 확인
        if arr[row] == arr[i] or row - i == abs(arr[row] - arr[i]):
            return False

    return True


def dfs(N: int, arr: list, row: int) -> int:
    # 마지막 행까지 탐색한 경우 -> 개수 +1
    if row == N:
        return 1

    count = 0
    # 0 ~ N-1까지의 열에 대해 반복
    for i in range(N):
        # i번째 열에 해당하는 위치에 퀸 배치
        arr[row] = i

        # row번째 행, i번째 열에 퀸을 놓은 경우 유망성 판단
        if promising(arr, row):
            # 유망한 경우, 다음 row+1행에 대해 재귀
            count += dfs(N, arr, row+1)

    return count


def main():
    N = int(input())
    print(dfs(N, [0 for i in range(N)], 0))


main()
