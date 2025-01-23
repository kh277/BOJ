# [Gold IV] Presidential Elections - 13350 

[문제 링크](https://www.acmicpc.net/problem/13350) 

### 성능 요약

메모리: 149576 KB, 시간: 192 ms

### 분류

다이나믹 프로그래밍, 배낭 문제

### 제출 일자

2025년 1월 23일 17:44:02

### 문제 설명

<p>In a few weeks time, a new president will be elected in the country of Marecia. There are two political parties: the Constituents and the Federals. Each party has one presidential candidate; one of these will become the new president. </p>

<p>This year you are more involved than ever before: you are the candidate for the Constituents! With only a few weeks to go, you decide to take stock of the situation. Instead of touring blindly through the country, you feel that it is better to focus your attention on certain particular states.</p>

<p>The Marecian electoral system is quite complicated. Every registered voter will vote for exactly one of the two candidates, but the totals are not calculated nationwide. Instead, every state has a fixed number of delegates. After the popular vote is in, the delegates from all states travel by foot to the capital of Marecia, the city of Ashwington. One final round of voting is done in Ashwington: every delegate gets to vote for one of the two candidates. A delegate is required by law to vote for the candidate who received the majority of the votes in his own home state.</p>

<p>Your campaign team has painstakingly compiled a very accurate list of voting preferences per state. Therefore you now have the following information about every state:</p>

<ul>
	<li>The number of voters who will definitely vote for the Constituents;</li>
	<li>The number of voters who will certainly vote for the Federals;</li>
	<li>The number of voters who have not made up their minds yet.</li>
</ul>

<p>Voters from the first two categories are not susceptible to any further campaigning, so your focus for the remaining weeks is on people of the third category. Specifically, you would like to know the minimum number of people you still have to convince in order to secure a victory.</p>

<p>If there is a tie on either state or national level, the law states that it is resolved in favour of the oldest of the two political parties, which unfortunately is the Federal party.</p>

### 입력 

 <p>The first line contains a single integer S, the number of states.</p>

<p>The following S lines each contain four integers D<sub>i</sub>, C<sub>i</sub>, F<sub>i</sub>, U<sub>i</sub>, where</p>

<ul>
	<li>D<sub>i</sub> denotes the number of delegates for the i-th state,</li>
	<li>C<sub>i</sub> denotes the number of registered voters in the i-th state who will definitely vote for the Constituents,</li>
	<li>F<sub>i </sub>denotes the number of registered voters in the i-th state who will certainly vote for the Federals,</li>
	<li>U<sub>i</sub> denotes the number of undecided voters in the i-th state.</li>
</ul>

<p>There are at most 2016 delegates in total, and the total number of registered voters is at most 10<sup>9</sup>. Every state has at least one delegate and at least one registered voter. There is at least one state.</p>

### 출력 

 <p>Output one line with a single integer: the minimum number of voters you have to convince to secure a victory. If it is not possible for you to win the election, output “impossible” instead.</p>

