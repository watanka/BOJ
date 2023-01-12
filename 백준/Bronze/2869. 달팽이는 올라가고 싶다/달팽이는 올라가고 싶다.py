## 달팽이는 올라가고 싶다
A, B, V = map(int,input().split())

day_move = (A-B)

day_dist = V - A

day = day_dist // day_move

remain_dist = day_dist % day_move + A
day += -(-remain_dist // A)

print(day)