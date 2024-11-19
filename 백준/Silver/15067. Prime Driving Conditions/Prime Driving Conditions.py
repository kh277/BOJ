# 백준 15067

import sys

input = sys.stdin.readline


def Eratos(N):
    num = [i for i in range(N+1)]

    for i in range(2, int(N**0.5)+1):
        # i가 소수인 경우, i를 제외한 i의 배수 지우기
        if num[i] != 0:
            for j in range(i+i, N+1, i):
                num[j] = 0
    
    # 에라토스테네스의 체에서 1인 값만 추출
    return [i for i in num if not i == 0][1:]


def solve():
    number = int(num)

    # num보다 큰 소수를 result에 저장 
    result = -1
    for i in range(len(prime)):
        if prime[i] >= number:
            result = prime[i]
            return [string, '0'*(4-len(str(result)))+str(result)]
    
    # num보다 큰 소수가 없는 경우
    if string[1:] == "ZZ":
        return [chr(ord(string[0])+1) + "AA", "0002"]
    elif string[2:] == "Z":
        return [string[0] + chr(ord(string[1])+1) + "A", "0002"]
    else:
        return [string[:2] + chr(ord(string[2])+1), "0002"]


# main 함수 ----------
prime = Eratos(10000)
while True:
    string, num = map(str, input().split())
    if string == "END" and num == "0000":
        break
    print(*solve())