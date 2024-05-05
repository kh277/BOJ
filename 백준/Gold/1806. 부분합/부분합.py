# 백준 1806

"""
start와 end 두 포인터를 0번 인덱스에 잡는다.
end를 한 칸씩 뒤로 보내며 탐색을 한다.
start~end까지의 합이 S 이상인지 확인한다.
S 미만이라면 end를 한 칸 증가, S 이상이라면 갱신 확인 후 start를 한 칸 증가시킨다. 
"""

import sys

input = sys.stdin.readline


def solve(N: int, S: int, num: list) -> int:
    # acm[i] = 0 ~ i번 인덱스까지의 합
    acm = [0 for i in range(N)]
    acm[0] = num[0]
    for i in range(1, N):
        acm[i] = acm[i-1] + num[i]

    start = 0
    end = 0
    result = 10e6

    # start = 0일 때 (num[0]이 결과에 포함될 경우)
    for i in range(N):
        if acm[i] >= S and result > i+1:
            result = i+1

    start += 1

    # start > 0일 때 (num[0]이 결과에 포함될 경우)
    # start ~ end까지의 누적합이 S보다 큰 경우 길이 result와 비교 
    while True:
        # 탈출 조건 : end가 끝까지 도달했고, start의 인덱스를 이동시켜도 S를 만들 수 없는 경우
        if end == N-1 and acm[end] - acm[start - 1] < S:
            break
        
        # start ~ end 까지의 합이 S보다 크다면
        if acm[end] - acm[start - 1] >= S:
            # 갱신이 가능하다면
            if result > (end - start):
                result = end - start + 1
            start += 1
        
        # start ~ end 까지의 합이 S보다 작다면
        elif acm[end] - acm[start - 1] < S:
            end += 1
    
    # 합을 만드는 것이 불가능하다면
    if result == 10e6:
        return 0
    
    return result


def main():
    N, S = map(int, input().split())
    num = list(map(int, input().split()))

    print(solve(N, S, num))


main()