# [Gold I] Takistusrada - 7187 

[문제 링크](https://www.acmicpc.net/problem/7187) 

### 성능 요약

메모리: 192368 KB, 시간: 728 ms

### 분류

너비 우선 탐색, 기하학, 그래프 이론, 그래프 탐색, 선분 교차 판정

### 제출 일자

2025년 11월 26일 13:30:13

### 문제 설명

<p>Sul on litter, mis võib libiseda mööda jääd. Kord sekundis saad Sa litrit toksata, kas põhjast, lõunast, idast või läänest. Toksamine muudab litri vastavasuunalist kiirust 1 meetri võrra sekundis. Alguses on litter punktis koordinaatidega $(0;0)$ ja seisab paigal.</p>

<p>Liikumise näide: toksame litrit 5 korda: läänest, lõunast, veel kord läänest ja siis kaks korda põhjast. Esimese sekundi jooksul liigub litter 1 meetri itta ja jõuab punkti $(1;0)$. Teise sekundi jooksul liigub litter 1 meetri itta ning 1 meetri põhja, jõudes punkti $(2;1)$. Kolmandal sekundil liigub litter 2 meetrit itta ja 1 meetri põhja, jõudes punkti $(4;2)$. Neljandal sekundil liigub litter 2 meetrit itta, jõudes punkti $(6;2)$. Viiendal sekundil liigub litter 2 meetrit itta ning ühe meetri lõunasse, jõudes punkti $(8;1)$.</p>

<p>Litri liikumine igal sekundil on sirgjooneline, otse algpunktist lõpp-punkti. Litrit ei pea tingimata toksama, sel juhul jäävad tema suund ja kiirus samaks. Litri maksimumkiirus nii ida-lääne kui põhja-lõuna suunas on 7 m/s. Kui litter liigub parajasti näiteks 7 m/s lääne suunas ja 4 m/s põhja suunas, siis idast seda enam toksata ei saa, aga teistest suundadest saab.</p>

<p>Jääle on paigutatud ka takistused. Takistusteks on maas pikali asetsevad pulgad, mis ühendavad täisarvuliste koordinaatidega punkte.</p>

<p>Eesmärgiks on liigutada litter võimalikult kiiresti etteantud punkti ilma ühtki takistust puudutamata. Lihtsuse mõttes eeldame, et nii pulgad kui ka litter on ühedimensioonilised ning puudutavad üksteist siis ja ainult siis, kui nad asuvad täpselt samas punktis. Puudutamiseks loetakse seda, kui litter lõpetab oma teekonna punktis, kus asub takistus või läbib oma teel mõnda sellist punkti.</p>

<p>Lõpp-punktis ei pea litter seisma jääma, kuid ta peab vastava sekundi teekonna lõpetama selles punktis.</p>

### 입력 

 <p>Tekstifaili esimesel real on 3 arvu: sihtpunkti täisarvulised koordinaadid ning takistuste arv $N$ (maksimaalselt 100). Järgmisel $N$ real on igaühel neli arvu, mis tähistavad takistuseks olevate pulkade algus- ja lõpp-punktide koordinaate. Kõigi lähteandmete koordinaadid on täisarvud $-10 \ldots 10$.</p>

### 출력 

 <p>Tekstifaili väljastada täpselt üks arv: mitme sekundiga on võimalik eesmärgini jõuda. Kui lõppu jõuda ei saa, väljastada $-1$.</p>

