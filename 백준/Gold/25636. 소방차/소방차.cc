// 백준 25636

#pragma GCC target ("avx2,fma")
#pragma GCC optimize ("Ofast,unroll-loops")
#include <bits/stdc++.h>
#define INF 10000000000000
using namespace std;
typedef long long ll;
typedef pair<int, ll> pil;

ll water[100001];
ll distDP[100001];
ll waterDP[100001];
vector<vector<pil>> graph;


struct Node
{
    ll dist, water;
    int v;

    bool operator>(const Node& other) const
    {
        if (dist!=other.dist)
            return dist > other.dist;
        return water < other.water;
    }
};


vector<ll> solve(int V, int S, int T)
{
    priority_queue<Node, vector<Node>, greater<Node>> pq;
    fill(distDP, distDP+V, INF);
    fill(waterDP, waterDP+V, -1);
    distDP[S] = 0;
    waterDP[S] = water[S];
    pq.push({0, water[S], S});

    while (!pq.empty())
    {
        auto [curD, curW, curV] = pq.top();
        pq.pop();

        if (curD > distDP[curV])
            continue;
        if (curD == distDP[curV] && curW < waterDP[curV])
            continue;
        if (curV == T)
            return {distDP[curV], waterDP[curV]};

        for (auto &[nextV, d]: graph[curV])
        {
            ll nextD = curD + d;
            ll nextW = curW + water[nextV];
            if (nextD < distDP[nextV])
            {
                distDP[nextV] = nextD;
                waterDP[nextV] = nextW;
                pq.push({nextD, nextW, nextV});
            }
            else if (nextD == distDP[nextV] && nextW > waterDP[nextV])
            {
                waterDP[nextV] = nextW;
                pq.push({nextD, nextW, nextV});
            }
        }
    }
    return {-1};
}


int main()
{
    cin.tie(0);
	ios_base::sync_with_stdio(0);

    int V, E, S, T;
    cin >> V;
    graph.resize(V);
    for (int i=0; i<V; i++)
        cin >> water[i];
    cin >> E;
    for (int i=0; i<E; i++)
    {
        int s, e, v;
        cin >> s >> e >> v;
        graph[s-1].push_back({e-1, v});
        graph[e-1].push_back({s-1, v});
    }
    cin >> S >> T;
    for (auto &i: solve(V, S-1, T-1))
    {
        cout << i << " ";
    }
    cout << "\n";
}
