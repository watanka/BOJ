## 후위 표기식 2

N = int(input())
equation = input()

dic = {}
for i in range(N) :
    dic[chr(i + 65)] = input()

stack = []
for char in equation :
    if char.isalpha() :
        stack.append(int(dic[char]))
    else :
        num2 = stack.pop()
        num1 = stack.pop()

        if char == '+' :
            stack.append(num1 + num2) 
        elif char == '-' :
            stack.append(num1 - num2) 
        elif char == '*' :
            stack.append(num1 * num2) 
        elif char == '/' :
            stack.append(num1 / num2) 

print('%.2f' %stack[0])