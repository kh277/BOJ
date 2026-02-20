// 백준 11610

#pragma GCC target ("avx2,fma")
#pragma GCC optimize ("Ofast,unroll-loops")
#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define MAX 300000


struct Task
{
    int time, value, index;
    bool isStart;

    bool operator<(const Task& other) const { return time != other.time ? time < other.time : isStart < other.isStart; }
};

vector<Task> tasks;
ll DP[MAX];


int solve(int N)
{
    ll curMax = 0;
    sort(tasks.begin(), tasks.end());
    for (auto &ev: tasks)
    {
        // 시작 지점인 경우
        if (ev.isStart)
            DP[ev.index] = curMax;
        // 끝 지점인 경우
        else
            curMax = max(curMax, DP[ev.index] + ev.value);
    }

    return curMax;
}


int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    for (int i=0; i<N; i++)
    {
        int a, b, c;
        cin >> a >> b >> c;
        tasks.push_back({a<<1 | 1, b, i, true});
        tasks.push_back({(a+c)<<1, b, i, false});
    }

    cout << solve(N) << "\n";
}
