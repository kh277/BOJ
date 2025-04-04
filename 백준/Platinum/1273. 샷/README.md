# [Platinum III] 샷 - 1273 

[문제 링크](https://www.acmicpc.net/problem/1273) 

### 성능 요약

메모리: 285660 KB, 시간: 628 ms

### 분류

자료 구조, 누적 합, 세그먼트 트리

### 제출 일자

2025년 1월 13일 16:46:43

### 문제 설명

<p>준수는 생일선물을 맞아 새로운 공기총을 샀다. 그리고 공기총의 성능을 시험해보기 위해 맥주캔을 쌓았다.</p>

<p>맥주캔은 총 검은색, 회색, 흰색으로 총 3가지 종류가 있다. 그리고 이를 N개의 열에 따라 쌓아올렸다. 쌓아올릴 때 순서는 아래에서부터 검은색, 회색, 흰색 순서이다. 한 열에 어느 색이 모두 없을 수는 있지만 색깔 순서를 위배하는 경우는 없다.</p>

<p>이렇게 맥주캔을 쌓아올린 뒤 준수는 높이를 정하고 공기총을 발사했다. 이 공기총은 성능이 뛰어나기에 한 높이를 쏘면 그 높이의 모든 캔은 모두 바깥으로 떨어지고 위쪽의 캔이 쓰러지지 않은 그대로 내려온다.</p>

<p>준수는 성능 시험을 위해 각 높이를 쏘았을 때 점수를 구하려고 한다. 점수 구하는 법은 검은색은 1점, 회색은 2점, 흰색은 5점이고, 바깥으로 떨어진 캔 점수의 총 합이다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/f408f395-e2fe-4c22-be73-0e4636c8a31b/-/preview/" style="width: 132px; height: 100px;"></p>

<p>위 그림은 초기에 맥주캔을 쌓은 상태이다. 여기서 2번 높이를 총으로 쏜다면 아래와 같이 된다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/3b3c6928-a273-434a-9e91-b828c5415087/-/preview/" style="width: 133px; height: 80px;"></p>

<p>검은색이 3개, 회색이 2개, 흰색이 1개 쓰러졌기 때문에 12점을 얻게 된다. 이 상태에서 4번 높이에 총을 쏘면 아래와 같이 되고, 7점을 얻는다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/521c64b8-99d0-4f02-bd6c-3ef6e1b172a0/-/preview/" style="width: 133px; height: 60px;"></p>

<p>캔을 쌓은 정보와 쏘는 높이를 순서대로 알고있을 때, 각 높이를 쏠 때 얻어지는 점수를 구해보자.</p>

### 입력 

 <p>첫째 줄에 열의 개수 N(1 ≤ N ≤ 300,000)이 주어진다. 두 번째 줄에는 각 열에 쌓인 검은색의 개수를 나타내는 N개의 정수가 주어진다. 세 번째 줄에는 각 열에 쌓인 회색의 개수를 나타내는 N개의 정수가 주어진다. 네 번째 줄에는 각 열에 쌓인 흰색의 개수를 나타내는 N개의 정수가 주어진다. 모든 수는 10<sup>6</sup>이하인 음이 아닌 정수이다. 다음 줄에는 준수가 쏘는 횟수 M(1 ≤ M ≤ 300,000)이 주어진다. 다음 줄에는 차례대로 준수가 쏘는 높이를 나타내는 M개의 정수가 입력된다.</p>

### 출력 

 <p>첫째 줄부터 M번째 줄까지 해당 높이를 쐈을 때 얻게되는 점수를 한 줄에 하나씩 출력한다.</p>

