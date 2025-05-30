# [Platinum IV] 쥐 잡기 - 1087 

[문제 링크](https://www.acmicpc.net/problem/1087) 

### 성능 요약

메모리: 111216 KB, 시간: 108 ms

### 분류

삼분 탐색

### 제출 일자

2025년 1월 17일 16:25:55

### 문제 설명

<p>이번에 김지민은 쥐를 잡는 게임을 만들어냈다. 이 게임은 큰 보드 위를 움직이는 로봇 쥐를 가지고 한다. 이 게임의 참가자는 정사각형 모양의 우리를 움직일 수 있다.</p>

<p>참가자는 이 우리를 보드 위라면 어느 곳이든지 이동할 수 있고, 떨어뜨려서 쥐를 잡을 수 있다.</p>

<p>하지만 김지민은 모든 쥐를 한 번에 잡는 것이 불가능하도록 우리의 크기를 작게 하고 싶다.</p>

<p>로봇 쥐는 2차원 평면에서 움직인다. 쥐는 항상 일정한 속도로 움직이고, 처음 위치가 알려져 있다고 가정한다. 우리는 길이가 L이고 축에 평행한 정사각형 모양이고 회전시키지 못한다. 우리는 게임이 시작된 직후부터 움직이거나 떨어뜨릴 수 있다.</p>

<p>게임은 쥐가 우리 내부에 완벽하게 포함되어야 잡혔다고 간주한다. 만약 쥐가 우리의 경계에 있다면 그 쥐는 잡힌 쥐가 아니다. 한 번에 모든 쥐를 절대로 잡을 수 없는 가장 큰 L을 구하는 프로그램을 작성하시오..</p>

### 입력 

 <p>첫째 줄에 쥐의 수 N이 주어진다. N은 2보다 크거나 같고, 50보다 작거나 같은 자연수이다. 둘째 줄부터 각 쥐의 시작 위치와 속도가 주어진다. 이 값은 모두 절댓값이 1,000보다 작거나 같은 정수이다. 시작 위치를 (px, py)라고 하고, 속도가 (vx, vy)라면, t초 때 쥐의 위치는 (px+vx*t, py+vy*t)이다.</p>

### 출력 

 <p>첫째 줄에 문제의 정답을 출력한다. 절대/상대 오차는 10<sup>-9</sup>까지 허용한다.</p>

