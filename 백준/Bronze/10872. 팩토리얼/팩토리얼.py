## 팩토리얼

N = int(input())

def factorial(num) :
    if num == 1 or num == 0:
        return 1
    else :
        return factorial(num-1) * num

print(factorial(N))