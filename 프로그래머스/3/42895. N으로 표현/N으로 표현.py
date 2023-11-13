def solution(N, number):
    
    
    # 숫자 N 사용횟수 num_use
    #              +   -  x    /  . 
    # num_use = 1, N   N  N    N  N    => 1 = 1
    # num_use = 2, N*2 0  N**2 1  N*11 => 2 = 1 + 1
    # num_use = 3,                     => 3 = 1 + 2 = 2 + 1
    answer = 0
    if N == number :
        return 1
    
    s = [set() for _ in range(8)]
    
    for i, x in enumerate(s, start = 1) :
        x.add(int(str(N) * i))
        
    for i in range(1, 8) :
        for j in range(i) :
            for op1 in s[j] :
                for op2 in s[i-j-1] :
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op2 != 0 :
                        s[i].add(op1 // op2)
        if number in s[i] :
            answer = i + 1
            break
    
    else :
        answer = -1
        
    return answer
    
    
    return answer