## 쇠막대기
pipelines = input()


num_pipe = 0
total_num = 0
for i in range(len(pipelines)) :
    if pipelines[i] == '(' :
        if pipelines[i+1] == ')' :
            total_num += num_pipe
        else :
            num_pipe += 1
    elif pipelines[i] ==')' and pipelines[i-1] != '(': # ')'
        total_num += 1
        num_pipe -= 1
print(total_num)
        
