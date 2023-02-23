## 퇴사
N = int(input())
days = []
pays = []
for _ in range(N) :
    T, P = map(int, input().split())
    days.append(T)
    pays.append(P)

stack = []
max_pay = 0
def dfs(day_pass, payment) :
    global max_pay
    if day_pass == N :
            max_pay = max(max_pay, payment)
            return
    t = days[day_pass]
    p = pays[day_pass]

    if t + day_pass <= N :
        dfs(t + day_pass, payment + p)
    dfs(day_pass + 1, payment)

for day in range(N) :
    dfs(day, 0)

print(max_pay)


