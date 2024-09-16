# 백준 3003


def solve(count: list) -> list:
    right = [1, 1, 2, 2, 2, 8]
    
    for i in range(6):
        count[i] = right[i] - count[i]
        
    return count


def main():
    count = list(map(int, input().split()))
    print(*solve(count))


main()