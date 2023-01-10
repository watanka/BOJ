## 단어 공부
word = input().upper()

cnt_dict = {}
for w in word :
    if w not in cnt_dict.keys() :
        cnt_dict[w] = 1
    else :
        cnt_dict[w] += 1
max_cnt = 0
freq_char = '?'
for char, cnt in cnt_dict.items() :
    if cnt > max_cnt :
        max_cnt = cnt
        freq_char = char

if list(cnt_dict.values()).count(max_cnt) > 1 :
    freq_char = '?'


print(freq_char)