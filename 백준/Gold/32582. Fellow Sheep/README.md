# [Gold III] Fellow Sheep - 32582 

[문제 링크](https://www.acmicpc.net/problem/32582) 

### 성능 요약

메모리: 111144 KB, 시간: 132 ms

### 분류

수학, 다이나믹 프로그래밍

### 제출 일자

2025년 12월 19일 14:01:24

### 문제 설명

<p>The sheep are fleeing from the wolf that has entered their pasture. To save themselves, they must escape through fenced paths designated for sheep shearing. The paths are connected to each other and eventually lead to a single exit into the farmyard, where the sheep that escape the wolf will be safe. The paths are arranged in a special formation, consisting of several segments of the same shape, with each segment containing $5$ paths. The entry point of each segment, except for the first, is also the exit point of the previous segment.</p>

<p>The entry point of the first segment is in the pasture, and the exit point of the last segment leads into the farmyard. The sheep always run in the same direction along one path, and it never happens that two sheep run along the same path in opposite directions. The sheep cannot jump over the fence of the path. The sheep’s escape is further complicated by the fact that halfway along each path there is an automatic gate that allows a certain number of sheep to pass through before closing itself, making the path impassable for other sheep. However, the wolf can jump over the gates on the paths, making him extremely dangerous. We assume (and the sheep assume as well) that the wolf can catch only those sheep which are no longer able to reach the farmyard due to the closed gates.</p>

<p>Determine how many sheep can escape from the wolf at most, given that for each gate it is known how many sheep it will let through.</p>

<p>The diagram shows the paths arranged in a formation of $4$ segments.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/8e6386f4-afc8-4932-bece-4681e911589d/-/preview/" style="width: 472px; height: 100px;"></p>

### 입력 

 <p>The first input line contains a single integer $N$ ($1 ≤ N ≤ 10^5$), the number of segments in the path formation. Each of the next $N$ lines contains $5$ space separated integers $A_i$, $B_i$, $C_i$, $D_i$, $E_i$ ($1 ≤ A_i , B_i , C_i , D_i , E_i ≤ 10^8$), the numbers of sheep which can pass through the corresponding gate in the $i$-th segment before the gate closes. The letters $A$, $B$, $C$, $D$, $E$ correspond to the notation in the image above. Segments are linked in the same order as they appear in the input. The entry of the first segment is in the pasture, the last segment leads into the farmyard.</p>

### 출력 

 <p>Output a single integer, the maximum number of sheep which can escape the wolf.</p>

