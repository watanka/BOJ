## 별 찍기
N = int(input())

def draw_star(n) :
    
    if n == 1 :
        return ['*']
    
    stars = draw_star(n // 3)
    L = []
    
    for star in stars :
        L.append(star * 3)
    for star in stars :
        L.append(star + ' '*(n // 3) + star)
    for star in stars :
        L.append(star * 3)
        
    return L

print('\n'.join(draw_star(N)))
    