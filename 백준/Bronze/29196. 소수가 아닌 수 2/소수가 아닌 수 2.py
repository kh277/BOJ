k = float(input())

# k를 10^6으로 곱한 후 가장 가까운 정수로 반올림
p = round(k * 10**9)
q = 10**9

# 절대오차 또는 상대오차가 10^-6 이하인지 확인
if abs(p/q - k) <= 10**-6:
    print("YES")
    print(p, q)
else:
    print("NO")
