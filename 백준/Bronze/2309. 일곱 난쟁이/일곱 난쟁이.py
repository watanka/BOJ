## 일곱 난쟁이

heights = []
for _ in range(9) :
    heights.append(int(input()))

heights.sort()
total_heights = sum(heights)

exclude = []
for i in range(8) :
    for j in range(i+1, 9) :

        if total_heights - heights[i] - heights[j] == 100 :
            exclude.append(heights[i])
            exclude.append(heights[j])
            break

    if len(exclude) == 2 :
        break






for h in heights :
    if h not in exclude :
        print(h)