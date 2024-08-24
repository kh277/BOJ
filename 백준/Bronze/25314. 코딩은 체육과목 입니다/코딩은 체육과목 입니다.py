# 백준 25314


def solve(N: int) -> int:
    repeat = (N-1) // 4 + 1
    return 'long ' * repeat + 'int' 

def main():
    N = int(input())
    print(solve(N))


main()