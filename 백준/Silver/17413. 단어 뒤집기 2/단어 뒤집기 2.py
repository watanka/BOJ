## 단어 뒤집기 2


words = input()
    
stack = []
result = ''
idx = 0
while idx < len(words) :

    if words[idx] == '<' :
        result += ''.join(reversed(stack))
        stack = []
        while words[idx] != '>' :
            stack.append(words[idx])
            idx += 1
        stack.append('>')
        result += ''.join(stack)
        stack = []
        
    else :
        if words[idx] == ' ' :
            result += ''.join(reversed(stack))
            result += ' '
            stack = []
        else :
            stack.append(words[idx])
    idx += 1

result += ''.join(reversed(stack))

print(result)
    
