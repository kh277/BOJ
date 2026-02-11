// 백준 20501

#pragma GCC optimize("O3")
#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")
#pragma GCC target("avx,avx2")
#include <bits/stdc++.h>
using namespace std;

#define MAX 2000

bitset<MAX> bs[MAX+1];


int main()
{
    cin.tie(0);
	ios_base::sync_with_stdio(0);

    int N;
    cin >> N;

    // bitset에 원소 저장
    for (int i = 1; i <= N; i++)
    {
        cin >> bs[i];
    }

    // AND 쿼리 처리
    int Q;
    cin >> Q;
    for (int i = 0; i < Q; i++)
    {
        int a, b;
        cin >> a >> b;
        cout << (bs[a] & bs[b]).count() << "\n";
    }
}
