## 평균은 넘겠지
N = int(input())

for _ in range(N) :
    inputs = list(map(int, input().split())) # sys.stdin.readline().rstrip().split()
    num_students, scores = inputs[0], inputs[1:]
    mean_score = sum(scores) / num_students
    cnt = 0
    for score in scores :
        if mean_score < score :
            cnt += 1
    print(f'{(cnt / num_students * 100):.3f}%')
