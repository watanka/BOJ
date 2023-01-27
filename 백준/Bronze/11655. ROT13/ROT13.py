## ROT13

sentence = input()

dic = {}
for i in range(13) :
    dic[chr(65 + i)] = chr(65 + i + 13)
for i in range(13,26) :
    dic[chr(65 + i)] = chr(65 + i - 13)



result = ''
for s in sentence :
    if s.isalpha() :
        if s.isupper() :
            new_s = dic[s]
        else :
            new_s = dic[s.upper()].lower()
    else :
        new_s = s


    result += new_s

print(result)