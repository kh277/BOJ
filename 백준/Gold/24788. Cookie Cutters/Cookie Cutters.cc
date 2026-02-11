// 백준 20501

#pragma GCC optimize("O3")
#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")
#pragma GCC target("avx,avx2")
#include <bits/stdc++.h>
using namespace std;

#define INF 100000000

struct Point
{
    double x, y;
};

typedef vector<Point> vp;
vp points;


// 신발끈 공식으로 넓이 도출
double getArea(int N)
{
    double area = 0;
    for (int i = 0; i < N; i++)
    {
        int j = (i+1) % N;
        area += points[i].x * points[j].y;
        area -= points[i].y * points[j].x;
    }

    return abs(area) / 2.0;
}


// x축, y축과 접하는 점이 하나씩 존재하도록 평행이동 처리
void moveMain(int N)
{
    // 좌표 경계값 찾기
    double minX = INF;
    double minY = INF;
    double maxX = -INF;
    double maxY = -INF;
    for (int i = 0; i < N; i++)
    {
        auto &[curX, curY] = points[i];
        minX = min(minX, curX);
        minY = min(minY, curY);
        maxX = max(maxX, curX);
        maxY = max(maxY, curY);
    }

    // 원점으로 평행이동
    for (int i = 0; i < N; i++)
    {
        points[i].x -= minX;
        points[i].y -= minY;
    }
}


void solve(int N, int A)
{
    // 원점으로 평행이동
    moveMain(N);

    // 넓이에 맞게 크기 조절
    double curArea = getArea(N);
    double move = sqrt(A / curArea);
    for (int i = 0; i < N; i++)
    {
        points[i].x *= move;
        points[i].y *= move;
    }

    // 원점으로 평행이동
    moveMain(N);
}


int main()
{
    cin.tie(0);
	ios_base::sync_with_stdio(0);

    int N;
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        double a, b;
        cin >> a >> b;
        points.emplace_back(Point{a+500, b+500});
    }
    int A;
    cin >> A;

    solve(N, A);
    for (int i = 0; i < N; i++)
    {
        cout << points[i].x << " " << points[i].y << "\n";
    }
}
