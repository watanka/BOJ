## 부녀회장이 될테야

T = int(input())

for _ in range(T) :
    floor = int(input())
    door = int(input())

    f0 = list(range(1, door+1))

    for k in range(floor) :
        for n in range(1, door) :
            f0[n] += f0[n-1]

    print(f0[-1])