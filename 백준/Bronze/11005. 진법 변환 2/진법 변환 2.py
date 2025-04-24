# 백준 11005

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, B):
    # 0~Z에 10진수 값 할당
    dic = dict()
    for i in range(26):
        dic[i+10] = chr(ord('A')+i)
    for i in range(10):
        dic[i] = str(i)
    
    # B진법 수 계산
    exp = [1]
    num = 1
    while True:
        if num*B <= N:
            num *= B
            exp.append(num)
            continue
        break

    # N을 B진법으로 변환
    result = ""
    for i in range(len(exp)-1, -1, -1):
        result = result + dic[N // exp[i]]
        N = N % exp[i]
    
    return result 


def main():
    N, B = map(int, input().split())
    print(solve(N, B))


main()
