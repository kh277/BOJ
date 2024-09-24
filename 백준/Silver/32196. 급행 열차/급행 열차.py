# 백준 32196


def solve(N: int, M: int, K: int, X: int, Y: int, time: list) -> int:
    time.sort(key= lambda x: (x[0]*X - x[1]*Y))
    
    normal = K
    rapid = K
    
    for i in range(M):
        normal = normal + time[i][0]
        rapid = rapid - time[i][1]
        
    return normal*X + rapid*Y


def main():
    N, M, K, X, Y = map(int, input().split())
    
    time = []
    for _ in range(N):
        time.append(list(map(int, input().split())))
        
    
    print(solve(N, M, K, X, Y, time))


main()
