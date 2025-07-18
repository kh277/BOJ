# [Gold III] 스트레이트 스위치 게임 - 20209 

[문제 링크](https://www.acmicpc.net/problem/20209) 

### 성능 요약

메모리: 152076 KB, 시간: 528 ms

### 분류

너비 우선 탐색, 브루트포스 알고리즘, 자료 구조, 그래프 이론, 그래프 탐색, 해시를 사용한 집합과 맵, 집합과 맵

### 제출 일자

2025년 7월 11일 11:09:16

### 문제 설명

<p>어느 나라에는, 여러 큐브와 연결된 스위치를 적절한 횟수만큼 눌러 모든 큐브 위에 적힌 숫자를 동일하게 만드는 게임이 있다.</p>

<p>그중 스트레이트 스위치라는 게임이 있다.</p>

<p>스트레이트 스위치 게임은 다음의 규칙을 따른다.</p>

<ul>
	<li>선분 위에 여러 개의 큐브가 일렬로 놓여 있고, 이 큐브 중 특정 큐브들과 연결된 스위치들이 여러 개 존재한다.</li>
	<li><u><strong><em>i</em> 번 스위치</strong></u>를 한 번 누르면 해당 스위치와 연결된 모든 큐브 위의 숫자가 각각<u><strong> <em>i </em>만큼 증가</strong></u>한다.</li>
	<li>큐브 위의 숫자는 0, 1, 2, 3, 4만 존재할 수 있으며 스위치를 눌러 큐브 위의 숫자 K가 4를 초과하면 K를 <strong>5로 나눈 나머지</strong>로 즉시 초기화된다.</li>
	<li>스위치를 한 번 누를 때, 반드시 단 한 개의 스위치만 누를 수 있다.</li>
	<li>같은 번호의 큐브가 한 스위치에 여러 번 연결되어있는 경우는 없다.</li>
	<li>각 스위치를 누를 수 있는 횟수의 제한은 없다.</li>
	<li>큐브 위에 쓰여 있는 모든 숫자가 동일해지는 순간, 게임은 종료된다.</li>
</ul>

<p>이 스트레이트 스위치 게임의 국가 대표 선수인 당신은 세계 대회에서 우수한 성적을 거두기 위해 전략을 세워야 한다.</p>

<p>큐브의 개수와 현재 큐브 위에 쓰여 있는 숫자들, 그리고 스위치-큐브 간의 연결 정보가 주어질 때</p>

<p>이 큐브들 위에 쓰여 있는 숫자를 모두 동일하게 만들기 위해 눌러야 하는 스위치의 최소 횟수를 구해보자.</p>

### 입력 

 <p>첫 번째 줄에는 큐브의 개수 N과 스위치의 개수 K가 주어진다. (1 ≤ N, K ≤ 8)</p>

<p>두 번째 줄에는 현재 N개의 큐브 위에 쓰여 있는 숫자 a<sub>1 </sub>a<sub>2 </sub>a<sub>3</sub> ... a<sub>N</sub> 가 한 줄에 주어진다. (0 ≤ a<sub>i</sub> ≤ 4)</p>

<p>세 번째 줄 부터 K+3번째 줄에는, 1번 스위치부터 K번 스위치까지 각 스위치에 연결된 큐브의 개수(B<sub><span style="font-size: 10.8333px;">m</span></sub>)와, 연결된 큐브의 번호들(b<sub>j</sub>)이 각 줄 마다 주어진다. (1 ≤ B<sub>m</sub> ≤ 8, 1 ≤ b<sub>j</sub> ≤ N)</p>

### 출력 

 <p>첫 번째 줄에 큐브들 위에 쓰여 있는 숫자를 모두 동일하게 만들기 위해 눌러야 하는 스위치의 최소 횟수를 출력한다.</p>

<p>(단, 주어진 스위치들을 아무리 누르더라도 모든 큐브의 숫자를 동일하게 만들 수 없는 경우에는 -1을 출력한다.)</p>

