## 골드바흐의 추측
import sys
input = sys.stdin.readline



num_arr = [1 for _ in range(1000001)]

for i in range(2, 1001) : 
    j = 2
    if num_arr[i] :
        for k in range(i + i, 1000001, i) :
            num_arr[k] = 0

while True :
    
    inp= int(input())
    if inp == 0 : break
    
    for i in range(3, inp):
        if num_arr[i] and num_arr[inp - i] :
            print(f'{inp} = {i} + {inp-i}')
            break
    else :
        print("Goldbach's conjecture is wrong.")
        
