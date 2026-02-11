// 백준 1927

#pragma GCC optimize("O3")
#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")
#pragma GCC target("avx,avx2")
#include <bits/stdc++.h>
using namespace std;


int main()
{
    cin.tie(0);
	ios_base::sync_with_stdio(0);

    int N;
    cin >> N;

    priority_queue<int, vector<int>, greater<int>> pq;
    for (int i=0; i<N; i++)
    {
        int x;
        cin >> x;
        if (x == 0)
        {
            if (pq.empty())
                cout << 0 << "\n";
            else
            {
                cout << pq.top() << "\n";
                pq.pop();
            }
        }
        else
            pq.emplace(x);
    }
}
