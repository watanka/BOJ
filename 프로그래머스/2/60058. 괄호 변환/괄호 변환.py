def is_correct(p):
    num_open, num_close = 0, 0
    idx = 0
    while idx < len(p):
        if p[idx] == '(':
            num_open += 1
        else:
            num_close += 1
                
        if num_close > num_open:
            return False
        
        idx += 1
        
    return num_open == num_close
        
    
    
def divide(p):
    open_count, close_count = 0, 0
    
    for i in range(len(p)):
        if p[i] == '(':
            open_count += 1
        else:
            close_count += 1
        if open_count == close_count:
            return p[:i+1], p[i+1:]
    return p, ''
            
def reverse(p):
    return ''.join(['(' if c == ')' else ')' for c in p])
        

def solution(p):
    if p == '':
        return ''
    
    # 균형잡힌 문자열: (, ) 갯수가 같을 때
    # 올바른 괄호 문자열: (, ) 순서도 맞을 때
    
    # p가 이미 올바른 괄호 문자열일 경우, 바로 리턴한다.
    if is_correct(p):
        return p
    else:
        # u와 v를 나눈다.
        u, v = divide(p)
        # print(f'u: {u}, v: {v}')
        # u가 올바른 괄호 문자열일 경우, v를 다시 u와 v로 나눔
        if is_correct(u):
            return u + solution(v)
        else:
            return '(' + solution(v) + ')' + reverse(u[1:-1])
        
    
    