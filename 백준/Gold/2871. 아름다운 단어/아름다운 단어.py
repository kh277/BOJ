# 백준 2871

'''
주어진 문자열에 같은 문자가 여러 번 등장하는 경우,
희원이는 뒤쪽 문자열을 우선해서 가져가는 경우가 더 유리하다.
'''


import sys
import heapq

input = sys.stdin.readline

def solve():
    pq = []
    visited = [False for _ in range(N)]
    
    # 단어를 우선순위 큐에 저장
    for i in range(N):
        # [알파벳 순서, 영어 글자, 원본 인덱스]
        # 뒤쪽 인덱스를 우선해서 가져가기 위해 * -1을 해줌
        heapq.heappush(pq, [ord(string[i])-ord('a'), -i])
            
    hye = ""
    sang = ""
    index = N-1
    count = 0
    
    # 상근이와 희원이가 번갈아가며 글자 제거
    while count < N//2:
        # 상근이 차례
        while True:
            if visited[index] == True:
                index -= 1
                continue
            visited[index] = True
            sang += string[index]
            index -= 1
            break
        
        # 희원이 차례
        while True:
            cur = heapq.heappop(pq)
            if visited[-cur[1]] == True:
                continue
            visited[-cur[1]] = True
            hye += string[-cur[1]]
            break
        
        count += 1
    
    # 누가 이겼는지 판단
    if sang > hye:
        return ['DA', hye]
    else:
        return ['NE', hye]
    

# main 함수 ----------
N = int(input())
string = list(input().rstrip())

for i in solve():
    print(i)