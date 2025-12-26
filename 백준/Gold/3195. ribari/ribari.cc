// 백준 3195

#pragma GCC optimize("O3")
#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")
#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pii pair<int, int>

vector<pii> town;


bool cmp(const pii& v1, const pii& v2) {
    if (v1.first == v2.first)
        return v1.second < v2.second;
    return v1.first < v2.first;
} 


bool check(int N, ll v) {
    ll accSum = town[0].second - v;
    for (int i=1; i<N; i++) {
        ll dist = town[i].first - town[i-1].first;

        // 현재 마을로 이동하다 사라져 버리는 경우
        if (accSum >= 0)
            accSum = max(0LL, accSum - dist);
        else
            accSum -= dist;
        // 현재 마을의 사람 수만큼 차감
        accSum += town[i].second - v;
    }

    return accSum >= 0;
}


ll solve(int N) {
    // 오름차순 정렬
    sort(town.begin(), town.end());

    // 매개변수 탐색 진행
    ll yes = 0;
    ll no = 100000000000000;

    while (abs(yes-no) > 1) {
        ll mid = (yes+no)/2;
        if (check(N, mid) == true)
            yes = mid;
        else
            no = mid;
    }
    return yes;
}


int main() {
    int N;
    cin >> N;

    for (int i=0; i<N; i++) {
        int a, b;
        cin >> a >> b;
        town.push_back({a, b});
    }

    cout << solve(N) << "\n";
}
