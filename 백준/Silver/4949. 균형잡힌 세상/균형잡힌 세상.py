# 균형잡힌 세상
import sys
input = sys.stdin.readline

while True :
    txt = input().rstrip()
    if txt == '.' :
        break

    stack = []
    wrong = False
    for char in txt :
        if char in ['(', ')', '[', ']'] :
            if char == ')' :
                if not stack or stack[-1] != '(' :
                    print('no')
                    wrong = True
                    break
                stack.pop()
            elif char == ']' :
                if not stack or stack[-1] != '[' :
                    print('no')
                    wrong = True
                    break
                stack.pop()
                
            elif char in ['(', '['] :
                stack.append(char)
                

    if not wrong :
        if stack :
            print('no')
        else :
            print('yes')
    