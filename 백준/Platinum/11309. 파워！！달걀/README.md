# [Platinum V] 파워!!달걀 - 11309 

[문제 링크](https://www.acmicpc.net/problem/11309) 

### 성능 요약

메모리: 111108 KB, 시간: 116 ms

### 분류

다이나믹 프로그래밍

### 제출 일자

2025년 7월 22일 13:48:45

### 문제 설명

<p>잘생긴 오이 베네딕트는 쿠팡에서 K개의 동일한 파워!!달걀을 구매했다. 그리고 그는 악독한 건물주라서, 갑자기 서로 다른 층에서 재미삼아 달걀을 떨궈보고 싶어졌다. 그의 건물은 1에서 N까지 층수가 매겨진, 총 N층 높이의 건물이다. </p>

<p>베네딕트가 구매한 달걀은 파워!!달걀이라서, 특정 조건을 만족해야만 깨진다. 각 달걀은 F+1 이상의 층에서 떨궈지면 깨지지만, F 이하의 층에서 떨궈지면 깨지지 않는다고 한다. (F는 0에서 N 사이 숫자 중 하나이다.)</p>

<p>베네딕트는 달걀이 깨질 때까지, 그가 원하는 횟수만큼 원하는 층에서 떨굴 수 있다. 그는 F를 확정하기 위해 최소한 몇 번 달걀을 떨어뜨려야 하는지 알고 싶다.</p>

<p>예를 들어서, 만약 베네딕트의 건물이 3층 짜리이고, 베네딕트가 달걀을 하나만 가지고 있다고 가정해보자. 처음에 그는 첫 번째 층에서 달걀을 떨어뜨려보아야 하고, 그런 다음에 두 번째 층에서(만약 달걀이 무사하다면 말이다), 그런 다음 다시 세 번째 층에서(역시나 만약 달걀이 무사하다면) 떨어뜨려보아야 할 것이다. 그러므로, 최악의 경우를 고려해볼 때 최소한 세 번은 떨어뜨려 보아야 한다.</p>

### 입력 

 <p>첫 번째 줄에는 테스트 실행횟수인 T가 주어지고 (1 ≤ T ≤ 10000), 뒤이어 T개의 줄이 이어진다.</p>

<p>각 줄에는 두 개의 숫자 : 건물의 높이 N과 달걀의 개수 K가 주어진다. (1 ≤ N ≤ 2000000007, 1 ≤ K ≤ 32)</p>

### 출력 

 <p>T개의 각 줄에는, F를 확정하기 위해 달걀을 떨궈야 하는 최소횟수를 출력한다. </p>

<p>만약 그 횟수가 32보다 크다면, Impossible이라고 출력한다. 불쌍하고도 가엾은 우리 베네딕트는, 그렇게 많이 달걀을 떨어뜨리고는 너무도 힘들어서 더는 작업을 지속할 수가 없다. 이하 작업은 생략한다.</p>

