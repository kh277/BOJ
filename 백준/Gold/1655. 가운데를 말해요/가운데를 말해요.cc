// 백준 1655

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

    priority_queue<int> pqLow;    // 하위 절반을 저장하는 최대 힙
    priority_queue<int, vector<int>, greater<int>> pqHigh;     // 상위 절반을 저장하는 최소 힙

    int cur;
    if (N >= 1)
    {
        cin >> cur;
        pqLow.emplace(cur);
        cout << cur << "\n";
    }

    if (N >= 2)
    {
        cin >> cur;
        if (pqLow.top() > cur)
        {
            pqLow.emplace(cur);
            pqHigh.emplace(pqLow.top());
            pqLow.pop();
        }
        else
        {
            pqHigh.emplace(cur);
        }
        cout << pqLow.top() << "\n";
    }

    for (int i = 3; i <= N; i++)
    {
        int cur;
        cin >> cur;
        pqLow.emplace(cur);

        // 상위 절반 중 최하위 값이 하위 절반 중 최상위 값보다 큰 경우, 이동 / 서로 교환
        if (i & 1 == 1)
        {
            pqHigh.emplace(pqLow.top());
            pqLow.pop();
            pqLow.emplace(pqHigh.top());
            pqHigh.pop();
        }
        else
        {
            pqHigh.emplace(pqLow.top());
            pqLow.pop();
        }

        // 중앙값 반환
        cout << pqLow.top() << "\n";
    }
}
