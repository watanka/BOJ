## 단어 수학
N = int(input())
words = []
alpha_dict = {}
num_list = []

for i in range(N) :
    word = input()
    words.append(word)

for i in range(N) :
    for j in range(len(words[i]))  :
        if words[i][j] not in alpha_dict.keys() :
            alpha_dict[words[i][j]] = 10 ** (len(words[i]) - j - 1)
        else : 
            alpha_dict[words[i][j]] += 10 ** (len(words[i]) - j - 1)
    
for num in alpha_dict.values() :
    num_list.append(num)

num_list.sort(reverse = True)

total = 0
assign = 9
for i in num_list :
    total += assign * i
    assign -= 1

print(total)