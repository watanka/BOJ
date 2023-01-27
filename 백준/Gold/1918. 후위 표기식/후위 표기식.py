## 후위 표기식
expression = input()
result = ''
stack = []
for exp in expression :
    if exp.isalpha() :
        result += exp 
    else :
        if exp == '(' :
            stack.append(exp)
        elif exp == '*' or exp == '/' :
            while stack and (stack[-1] == '*' or stack[-1] == '/') :
                result += stack.pop()
            stack.append(exp)
        elif exp == '+' or exp == '-' :
            while stack and stack[-1] != '(' :
                result += stack.pop()
            stack.append(exp)

        elif exp == ')' :
            while stack and stack[-1] != '(' :
                result += stack.pop()
            stack.pop()
while stack :
    result += stack.pop()

print(result)