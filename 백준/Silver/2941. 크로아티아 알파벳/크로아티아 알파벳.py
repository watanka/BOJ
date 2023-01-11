## 크로아티아 알파벳

alphabets = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

cnt = 0
i = 0
word = input()

while i < len(word) : 
    for look_length in range(1,4) : 
        char = word[i: i+look_length]
        if char in alphabets :
            cnt += 1
            i += look_length
            break
        if char not in alphabets and look_length == 3 :
            i += 1
            cnt += 1
print(cnt)