# 백준 14640

'''
https://epubs.siam.org/doi/abs/10.1137/0210018 논문을 참고하여 코드를 작성했다.
이하는 해당 논문에 있는 O(N^2) 알고리즘을 정리한 것이다.

알고리즘 A:
작업에 임의로 인덱스를 부여하여 r₁ ≤ r₂ ≤ … ≤ rₙ이 되도록 정렬한다.
Part I. (금지 구간 선언)
    초기에는 금지 구간이 하나도 선언되어 있지 않다. 인덱스가 큰 순서(즉, Tₙ, Tₙ₋₁, …, T₁)로 각 작업 Tᵢ에 대해 다음 두 단계를 수행한다:
    - 1. dⱼ ≥ dᵢ인 각 작업 Tⱼ에 대해, 임계 시간 cⱼ를 다음과 같이 갱신한다.
        - 1a. 만약 cⱼ가 정의되지 않았다면 cⱼ를 dⱼ - 1로, 이미 정의되어 있다면 cⱼ를 cⱼ - 1로 갱신한다.
        - 1b. 만약 cⱼ가 이미 선언된 금지 구간 F에 속한다면, cⱼ를 F의 하한(inf(F))으로 설정한다.
    - 2. 만약 i = 1 또는 rᵢ₋₁ < rᵢ인 경우, 정의된 cⱼ들 중 최소값 c을 구한 후 다음을 수행한다:
        - 2a. 만약 c < rᵢ이면, 스케줄이 불가능함을 선언하고 알고리즘을 중단한다.
        - 2b. 만약 rᵢ ≤ c < rᵢ + 1이면, (c-1, rᵢ)를 금지 구간으로 선언한다.

Part II. (스케줄 생성) -> 성공적으로 금지 구간이 선언된 경우 항상 스케줄링이 가능하므로 코드에서는 생략.
    초기에는 모든 작업이 스케줄되어 있지 않으며, t = 0으로 설정한다. 다음 세 단계를 모든 작업이 스케줄될 때까지 반복한다:
    - 1. 현재 시간 t에 스케줄되지 않은 작업이 없다면, 아직 스케줄되지 않은 작업들 중 최소의 rᵢ를 t로 설정한다.
    - 2. t가 어떤 금지 구간 F에 속한다면, t를 F의 상한(sup(F))으로 설정한다.
    - 3. 스케줄되지 않은 작업들 중 가장 빠른 마감일을 가진 작업 Tⱼ를 선택하여 Tⱼ의 시작 시간 sⱼ을 t로 설정한 후 t를 t+1로 갱신한다.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 10**10


def solve(N, T, tasks):
    tasks.sort(key= lambda x: (x[0], x[1]))
    forbidden = []

    # I. 금지 구간 선언
    critical = [tasks[i][1] for i in range(N)]      # 임계 시간
    visited = [0 for _ in range(N)]     # 이미 적용한 금지 구간의 수
    minC = INF
    for i in range(N-1, -1, -1):
        curR, curD = tasks[i]

        # I-1. 임계 시간 갱신
        for j in range(N):
            _, otherD = tasks[j]
            if otherD < curD:
                continue
            critical[j] -= T

            while True:
                if visited[j] < len(forbidden) and critical[j] < forbidden[visited[j]][1]:
                    critical[j] = min(critical[j], forbidden[visited[j]][0])
                    visited[j] += 1
                    continue
                break

            minC = min(minC, critical[j])

        # I-2. 금지 구간 추가
        if i == 0 or tasks[i-1][0] < curR:
            if minC < curR:
                return 'no'
            if minC < curR + T:
                forbidden.append((minC-T, curR))

    # II. 스케줄 생성
    return 'yes'


def main():
    N, T = map(int, input().split())
    tasks = []
    for _ in range(N):
        r, d = map(int, input().split())
        tasks.append((r, d))
    
    print(solve(N, T, tasks))


main()