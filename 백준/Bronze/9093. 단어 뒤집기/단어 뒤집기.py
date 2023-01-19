## 단어 뒤집기

N = int(input())

for _ in range(N) :
    sentence = input().split()
    
    print(' '.join([word[::-1] for word in sentence]))