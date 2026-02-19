// 백준 35263

#pragma GCC target ("avx2,fma")
#pragma GCC optimize ("Ofast,unroll-loops")
#include <bits/stdc++.h>
using namespace std;
#define MAX 500001


int A[MAX];
int diff[MAX];
int sieve[MAX];
vector<int> prime;


// [2, N] 까지의 선형 체 처리
void LinearSieve(int N)
{
    for (int i=2; i<N+1; i++)
    {
        if (sieve[i] == 0)
        {
            prime.push_back(i);
            sieve[i] = i;
        }

        for (int j=0; j<prime.size(); j++)
        {
            if (i*prime[j] > N)
                break;
            sieve[i*prime[j]] = prime[j];
            if (i % prime[j] == 0)
                break;
        }
    }
}


// N의 소인수 반환
unordered_set<int> factorize(int N)
{
    unordered_set<int> result;
    while (N > 1)
    {
        result.insert(sieve[N]);
        N = N/sieve[N];
    }
    return result;
}


double solve(int N)
{
    // MAX까지 선형 체 처리
    LinearSieve(MAX);

    long long diffSum = 0;
    double result = 0.0;
    int size = 0;
    
    // 차분 배열의 값이 1 이상인 값에 대해 기대값 계산
    for (int i=0; i<N; i++)
    {
        diffSum += diff[i];
        if (diffSum > 0)
        {
            unordered_set<int> fact = factorize(A[i]);
            result += (double)accumulate(fact.begin(), fact.end(), 0) / fact.size();
        }
        else
            result += A[i];
    }
    return result;
}


int main()
{
    cin.tie(0);
	ios_base::sync_with_stdio(0);

    int N, M;
    cin >> N >> M;

    for (int i=0; i<N; i++)
        cin >> A[i];

    // 각 폭발을 차분 배열에 저장
    while (M--)
    {
        int a, b;
        cin >> a >> b;
        diff[a-1] += 1;
        diff[b] -= 1;
    }

    cout << fixed << setprecision(12) << solve(N) << "\n";
}
