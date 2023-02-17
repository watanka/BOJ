## 리모컨

channel = int(input())
N = int(input())
if N :
    brokens = list(map(int, input().split()))
else :
    brokens = []

# channel 값과 100 간의 차이 계산
answer = abs(channel - 100)

for nums in range(1000001) :
    target = str(nums)

    for i in range(len(target)) :
        if int(target[i]) in brokens :
            break
    else :
        answer = min(answer, abs(nums - channel) + len(target))

print(answer)