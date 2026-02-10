// 백준 15658

#pragma GCC optimize("O3")
#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")
#pragma GCC target("avx,avx2")
#include <bits/stdc++.h>
using namespace std;

#define INF 2000000000
int maxV = -INF;
int minV = INF;


void DFS(int N, int A[], int op[], int depth, int accSum)
{
    if (depth == N)
    {
        maxV = max(maxV, accSum);
        minV = min(minV, accSum);
        return;
    }

    // + 처리
    if (op[0] > 0)
    {
        op[0] -= 1;
        DFS(N, A, op, depth+1, accSum+A[depth]);
        op[0] += 1;
    }

    // - 처리
    if (op[1] > 0)
    {
        op[1] -= 1;
        DFS(N, A, op, depth+1, accSum-A[depth]);
        op[1] += 1;
    }

    // * 처리
    if (op[2] > 0)
    {
        op[2] -= 1;
        DFS(N, A, op, depth+1, accSum*A[depth]);
        op[2] += 1;
    }

    // / 처리
    if (op[3] > 0)
    {
        op[3] -= 1;
        DFS(N, A, op, depth+1, accSum/A[depth]);
        op[3] += 1;
    }
}


int main()
{
    cin.tie(0);
	ios_base::sync_with_stdio(0);

    int N;
    cin >> N;
    int A[N];
    for (int i = 0; i < N; i++)
        cin >> A[i];
    int op[4];
    for (int i = 0; i < 4; i++)
        cin >> op[i];
    DFS(N, A, op, 1, A[0]);
    cout << maxV << "\n" << minV << "\n";
}
