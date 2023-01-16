## 대표값2

num_list = []
for _ in range(5) :
    num_list.append(int(input()))


for i in range(len(num_list)):
    for j in range(i, 0, -1) :
        if num_list[j-1] > num_list[j] :
            num_list[j-1], num_list[j] = num_list[j], num_list[j-1]
        else :
            break


mean = int(sum(num_list) / len(num_list))
median = num_list[2]

print(mean)
print(median)