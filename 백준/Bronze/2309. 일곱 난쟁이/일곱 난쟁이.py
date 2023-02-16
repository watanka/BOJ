## 일곱 난쟁이

heights = []
for _ in range(9) :
    heights.append(int(input()))

heights.sort()
total_heights = sum(heights)

class Found(Exception) : pass

try : 
    for i in range(8) :
        for j in range(i+1, 9) :

            if total_heights - heights[i] - heights[j] == 100 :
                raise Found

except Found :

    for idx in range(9) :
        if idx == i or idx == j :
            pass
        else :
            print(heights[idx])