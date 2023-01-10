## 최댓값

max_value = 0
max_idx = 0
for i in range(9) :
    inp = int(input())
    if max_value < inp :
        max_value = inp
        max_idx = i + 1

print(max_value, max_idx)