## 나이순 정렬

N = int(input())

addressbook = {}
for _ in range(N) :
    age, name = input().split()
    age = int(age)
    if age not in addressbook.keys() :
        addressbook[age] = [name]
    else :
        addressbook[age].append(name)

addressbook = sorted(addressbook.items(), key = lambda x: x[0])

for age, names in addressbook :
    for name in names :
        print(age, name) 