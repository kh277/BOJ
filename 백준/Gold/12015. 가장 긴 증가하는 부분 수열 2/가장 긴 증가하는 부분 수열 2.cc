// 백준 12015

#pragma GCC target ("avx2,fma")
#pragma GCC optimize ("Ofast,unroll-loops")
#include <bits/stdc++.h>
#define MAX 1048576
using namespace std;

typedef pair<int, int> pii;
vector<pii> A;
int tree[2*MAX];


bool cmp(const pii& x, const pii& y)
{
    if (x.first != y.first) return x.first < y.first;
    return x.second > y.second;
}


// index번째 값을 value로 변경
void update(int N, int index, int value)
{
    for (tree[index += N] = value; index > 1; index >>= 1)
        tree[index>>1] = max(tree[index], tree[index ^ 1]);
}


// [left, right] 구간의 최대값 구하기
int query(int N, int left, int right)
{
    int result = 0;
    for (left += N, right += N; left <= right; left >>= 1, right >>= 1)
    {
        if (left & 1)
            result = max(result, tree[left++]);
        if (~right & 1)
            result = max(result, tree[right--]);
    }
    return result;
}


int solve(int N)
{
    sort(A.begin(), A.end(), cmp);

    for (int i=0; i<N; i++)
    {
        auto &[value, index] = A[i];
        int prev = query(N, 0, index-1);
        update(N, index, prev+1);
    }

    return tree[1];
}


int main()
{
    cin.tie(0);
	ios_base::sync_with_stdio(0);

    int N;
    cin >> N;

    for (int i=0; i<N; i++)
    {
        int a;
        cin >> a;
        A.push_back({a, i});
    }

    cout << solve(N) << "\n";
}
