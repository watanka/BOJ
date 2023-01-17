## 단어 정렬
N = int(input())
word_list = [input() for _ in range(N)]

word_cnt = {}
for word in word_list :
    if word not in word_cnt.keys() :
        word_cnt[word] = len(word)
sorted_wordlist = [f[0] for f in sorted(word_cnt.items(), key = lambda x : (x[1], x))]

for word in sorted_wordlist :
    print(word)