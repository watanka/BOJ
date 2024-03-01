## 1439 뒤집기
'''
0001100
0000000
문자열 S가 모두 같은 숫자로 이루어질 수 있도록 뒤집기
뒤집기는 한번에 연속된 숫자들을 0에서 1, 또는 1에서 0으로 바꿀 수 있다.
'''

S = input()

# 연속된 1과 0을 구함
prev = S[0]

cnt_zero, cnt_one = int(prev == '0'), int(prev == '1')

for idx in range(1, len(S)):
        if S[idx-1] != S[idx]:
            if S[idx] == '0':
                cnt_zero += 1
            else:
                cnt_one += 1
    

print(min(cnt_zero, cnt_one))