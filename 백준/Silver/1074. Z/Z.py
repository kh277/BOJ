# 백준 1074

'''
이 문제는 필드를 4개의 그룹으로 나눴을 때,
우측 하단의 수 + 1이 4의 배수가 된다는 것을 생각하면 된다.

칸의 시작 행, 시작 열, 끝 행, 끝 열을 인자로 넘겨주면서
목표 행, 목표 열에 근접할 때까지 재귀를 통해 반복한다.
동시에 시작 숫자와 끝 숫자도 인자로 넘겨준다.
시작 숫자와 끝 숫자가 같아질 경우 그 값이 결과값이 된다.
'''

import sys

input = sys.stdin.readline


# 인자로 시작 숫자, 끝 숫자, [시작 행, 시작 열, 끝 행, 끝 열], [목표 행, 목표 열]을 받는다
def field(start: int, end: int, data: list, goal: list) -> int:

    # 만약 탐색 범위가 1칸인 경우
    if start == end:
        return start

    # 이 값이 다음 field 함수에서 탐색할 총 칸 수
    next_gap = int((end - start + 1) / 4)
    # 이 값이 다음 field 함수에서 탐색할 총 행 수
    next_line = int((data[2] - data[0] + 1) / 2)

    # 사분면 분리 4 5 6 7중에 45에 들어갈지 67에 들어갈지
    if goal[0] >= data[0] + next_line:
        # 사분면 중 아래쪽-오른쪽 범위일 경우
        if goal[1] >= data[1] + next_line:
            return field(start + 3*next_gap, start + 4*next_gap - 1, [data[0] + next_line, data[1] + next_line, data[0] + 2*next_line - 1, data[1] + 2*next_line - 1], goal)

        # 사분면 중 아래쪽-왼쪽 범위일 경우
        else:
            return field(start + 2*next_gap, start + 3*next_gap - 1, [data[0] + next_line, data[1], data[0] + 2*next_line - 1, data[1] + next_line - 1], goal)

    # 사분면 중 위쪽-오른쪽 범위일 경우
    elif goal[1] >= data[1] + next_line:
        return field(start + next_gap, start + 2*next_gap - 1, [data[0], data[1] + next_line, data[0] + next_line - 1, data[1] + 2*next_line - 1], goal)

    # 사분면 중 위쪽-왼족 범위일 경우
    else:
        return field(start, start + next_gap - 1, [data[0], data[1], data[0] + next_line - 1, data[1] + next_line - 1], goal)


def solve(N: int, y: int, x: int) -> int:
    start = 0
    end = 2 ** (2*N) - 1

    return field(start, end, [0, 0, 2**N-1, 2**N-1], [y, x])


def main():
    N, r, c = map(int, input().split())
    print(solve(N, r, c))

main()