## 암호 만들기
L, C = map(int, input().split())
letters = sorted(list(input().split()))

def count_vowels(letters) :
    ## 해당 idx 포함하여 최소 2개 자음, 최소 1개 모음이 포함되어 있는지 확인
    vowels = 'aeiou'
    cnt = 0
    for v in vowels :
        cnt += letters.count(v)
    return cnt

stack = []
def dfs(start) :
    if len(stack) == L :
        comb_letter = ''.join(stack)
        num_vowels = count_vowels(comb_letter)
        if num_vowels >= 1 and L - num_vowels >= 2 :
            print(comb_letter)
        return
    
    for i in range(start, C) :
        if letters[i] not in stack :
            stack.append(letters[i])
            dfs(i)
            stack.pop()

dfs(0)
