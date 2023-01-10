## 알파벳 찾기
S = input()

alphabet = 'abcdefghijklmnopqrstuvwxyz'

ls = []
for char in alphabet :
    if char in S :
        ls.append(S.index(char))
    else :
        ls.append(-1)

print(' '.join(map(str, ls)))