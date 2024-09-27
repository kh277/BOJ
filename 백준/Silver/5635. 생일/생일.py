# 백준 5635


import sys

input = sys.stdin.readline

# 최대값이 갱신 가능한지 확인
def check_max(cur_data: list, max_data: list) -> bool:
    # 연, 월, 일 순서대로 비교
    for i in range(1, 4):
        if cur_data[i] < max_data[i]:
            return True
        elif cur_data[i] == max_data[i]:
            continue
        else:
            return False
    
    return False


# 최소값이 갱신 가능한지 확인
def check_min(cur_data: list, min_data: list) -> bool:
    # 현재 값과 최소값 비교
    for i in range(1, 4):
        if cur_data[i] > min_data[i]:
            return True
        elif cur_data[i] == min_data[i]:
            continue
        else:
            return False
    
    return False


def solve(N: int, data: list) -> list:
    # 초기값 설정
    min_age = data[0]
    max_age = data[0]
    
    # 최소값 및 최대값이 갱신 가능한지 확인
    for i in range(1, N):
        if check_min(data[i], min_age) == True:
            min_age = data[i]
        if check_max(data[i], max_age) == True:
            max_age = data[i]
            
    return [min_age[0], max_age[0]]


def main():
    N = int(input())
    
    data = []
    for i in range(N):
        temp = list(map(str, input().split()))
        # [이름, 연, 월, 일] 순서로 재배치
        data.append([temp[0], int(temp[3]), int(temp[2]), int(temp[1])])
    
    for i in solve(N, data):
        print(i)


main()