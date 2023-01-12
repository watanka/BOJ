## 설탕 배달

N = int(input())

cnt3, cnt5 = N//3, N//5

find = False
for c5 in range(cnt5, -1, -1) :
    for c3 in range(cnt3, -1, -1) :
        # print('c5 : ', c5, ', c3 : ', c3)
        made = c3 * 3 + c5 * 5
        # print('made : ', made)
        if made == N :
            print(c3 + c5)
            find = True
            break
    if find :
        break
if not find :
    print(-1)