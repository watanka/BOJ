## 다이얼
alphabets = ['ABC' , 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

phone_dict = {}
for i,char_list in enumerate(alphabets) :
    for char in char_list :
        phone_dict[char] = i+3

word = input()

time = 0
for w in word :
    time+= phone_dict[w]
print(time)