# 백준 2473

'''
세 용액의 특성값을 합쳐 0에 가장 가까운 경우를 출력하기

용액을 하나 잡고 나머지 두 용액을 조절하여 0에 가장 가까워지는 경우까지 탐색을 하면 된다.
'''

import sys

input = sys.stdin.readline


def solve(N: int, liquid: list) -> list:
    # 탐색을 위해 우선 오름차순으로 정렬한다.
    liquid.sort()
    
    # [세 용액의 합, 용액1, 용액2, 용액3] 순서로 저장
    result = [10e10, None, None, None]

    # 용액1을 0 ~ N-3번까지 잡으며 탐색 
    for i in range(N-2):
        # i, i+1, N-1(마지막) 이렇게 세 용액을 잡고 탐색
        left = i+1
        right = N-1

        while True:
            # left와 right가 만나면 반복 종료
            if left >= right:
                break
            
            # 세 용액의 특성값 계산 후 현재 저장된 특성값보다 작을 경우 갱신
            cur_sum = liquid[i] + liquid[left] + liquid[right]
            if abs(cur_sum) < abs(result[0]):
                result = [cur_sum, liquid[i], liquid[left], liquid[right]]
            
            # 합이 음수일 경우
            if cur_sum < 0:
                left += 1
            # 합이 양수일 경우
            else:
                right -= 1
    
    return result[1:]


def main():
    N = int(input())
    liquid = list(map(int, input().split()))

    print(*solve(N, liquid))


main()