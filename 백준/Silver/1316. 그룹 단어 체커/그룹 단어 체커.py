## 그룹 단어 체커
N = int(input())
cnt = 0
for _ in range(N) :
    word = input()

    group = []
    group_num = True
    for i in range(len(word)) :
        if word[i] not in group :
            group.append(word[i])
        else :
            if word[i] != group[-1] :
                group_num = False

    if group_num :
        cnt += 1



print(cnt)