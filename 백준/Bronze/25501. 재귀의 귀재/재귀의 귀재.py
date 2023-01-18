## 재귀의 귀재
N = int(input())

def recursion(s, l, r, cnt) :
    cnt += 1
    if l >= r : 
        return 1, cnt
    elif s[l] != s[r] : 
        return 0, cnt
    else : 
        return recursion(s, l+1, r-1, cnt)

def isPalindrome(word) :
    return recursion(word, 0, len(word) -1, 0)

for _ in range(N) :
    S =  input()

    print(*isPalindrome(S))
    