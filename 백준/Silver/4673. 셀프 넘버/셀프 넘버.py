## 셀프 넘버

def generate(n) :
    return n + sum(list(map(int, str(n))))

candidates = list(range(1, 10001))
for i in range(1,10001) :
    generator = i
    
    while generator <= 10000 :        
        generator = generate(generator)
        if generator in candidates :
            candidates.remove(generator)
        else : break

for cand in candidates :
    print(cand)