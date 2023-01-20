##괄호
T = int(input())

for _ in range(T) :
    string = input()

    cnt = 0
    valid = True
    for s in string :
        if s =='(' :
            cnt += 1
        else :
            if cnt > 0 :
                cnt -= 1
            else :
                valid = False
                break
    
    if valid and cnt == 0:
        print('YES')
    else :
        print('NO')
