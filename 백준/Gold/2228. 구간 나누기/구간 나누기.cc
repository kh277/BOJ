// 백준 2228

/*
DP[i][j][k] = i번째 수까지 고려하고, 현재 누적된 구간이 j개이며 현재 원소의 사용 여부가 k일 때, 합의 최대값
*/

#pragma GCC target ("avx2,fma")
#pragma GCC optimize ("Ofast,unroll-loops")
#include <bits/stdc++.h>
#define INF 100000000
using namespace std;

int A[101];
int DP[101][52][2];


void init(int N, int M)
{
    fill(&DP[0][0][0], &DP[0][0][0] + sizeof(DP) / sizeof(int), -INF);
}


int solve(int N, int M)
{
    init(N, M);
    for (int i=0; i<=N; i++)
        DP[i][0][0] = 0;

    for (int cur=1; cur<=N; cur++)
    {
        for (int j=1; j<=M; j++)
        {
            // 현재 값을 포함하지 않는 경우
            DP[cur][j][0] = max(DP[cur-1][j][0], DP[cur-1][j][1]);

            // 현재 값을 포함하는 경우 - max(현재 값에서 새로운 구간 시작, 이전 구간에서 연장)
            DP[cur][j][1] = max(DP[cur-1][j-1][0] + A[cur-1], DP[cur-1][j][1] + A[cur-1]);
        }
    }
    return max(DP[N][M][0], DP[N][M][1]);
}


int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;
    for (int i=0; i<N; i++)
        cin >> A[i];

    cout << solve(N, M) << "\n";
}
