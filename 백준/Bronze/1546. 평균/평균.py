## 평균

N = int(input())

scores = list(map(int, input().split()))

max_score = 0
for score in scores :
    if score > max_score :
        max_score = score


print((sum(scores) / max_score * 100) / N)
