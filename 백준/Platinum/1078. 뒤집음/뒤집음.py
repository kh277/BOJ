# 백준 1078


import sys

input = sys.stdin.readline


# x-y = a에서 a에 해당하는 값들이 div에 저장되어 있을 때, 가장 작은 수 반환
# ex) ABCD에서 A-D=a, B-C=b인 경우 div = [a, b]가 됨. 이 때 가장 작은 ABCD 반환
def check_pair(result_length: int, div: list) -> str:
    length = len(div)
    result = [0 for _ in range(result_length)]

    # A는 0의 값이 불가능하므로
    for A in range(1, 10):
        B = A - div[0]
        if 0 <= B <= 9:
            result[0] = A
            result[-1] = B
            break
    
    # 이후 쌍들에 대해 반복
    for i in range(1, length):
        for C in range(10):
            D = C - div[i]
            if 0 <= D <= 9:
                result[i] = C
                result[-i-1] = D
                break

    # 홀수일 경우 중앙값 최소로 처리
    if result_length % 2 == 1:
        result[(result_length-1)//2] = 0

    return ''.join(map(str, result))


# 나누기 생성 함수
# ex) 5인 경우 [9999, 99], 8의 경우 [9999999, 99999, 999, 9]가 리턴됨
def generate_divider(N: int) -> list:
    result = []
    for i in range(N, 1, -2):
        result.append(int('9' * (i - 1)))
    return result


def check(N: int, type: int) -> str:
    coef = [0 for _ in range(type//2)]
    divider = generate_divider(type)
    
    temp = N
    
    # 계수 생성
    for i in range(type//2):
        if str(temp)[-1] == '0':
            coef[i] = 0
        elif temp > 0:
            coef[i] = 10 - int(str(temp)[-1])
        elif temp < 0:
            coef[i] = int(str(temp)[-1]) - 10
        
        # 마지막은 temp를 10으로 나누지 않음
        if i == type//2 - 1:
            temp = (temp - coef[i]*divider[i])
        else:
            temp = (temp - coef[i]*divider[i]) // 10
    
    # 모든 계수가 10 미만인지 확인
    for i in coef:
        if abs(i) >= 10:
            return ""
    
    # 가능한 경우 리턴
    if temp == 0:
        return check_pair(type, coef)
    else:
        return ""
    
    
def solve(N: int) -> int:
    N_length = len(str(N))
    
    if N % 9 != 0:
        return -1
    
    if N == 9:
        return 10
    
    for i in range(N_length, 13):
        result = check(N, i)
        
        # 현재 자리수에서 처리가 된다면 해당 값 리턴
        if len(result) != 0:
            return result
    
    return -1


def main():
    N = int(input())

    print(solve(N))


main()
