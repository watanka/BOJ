## 접미사 배열

S = input()

arr = []
for i in range(len(S)) :
    arr.append(S[i:])

sorted_arr = sorted(arr)

for word in sorted_arr :
    print(word)