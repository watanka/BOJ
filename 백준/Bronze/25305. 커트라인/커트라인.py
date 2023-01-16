## 커트라인

N, k = map(int, input().split())

scores = list(map(int, input().split()))

for i in range(len(scores)) :
    for j in range(i, 0, -1) :
        if scores[j-1] > scores[j] :
            scores[j-1], scores[j] = scores[j], scores[j-1]
        else :
            break
print(scores[-k])
