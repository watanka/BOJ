## 상수
a,b = input().split()

sangsoo_a, sangsoo_b = int(a[::-1]), int(b[::-1])

print(max([sangsoo_a, sangsoo_b]))