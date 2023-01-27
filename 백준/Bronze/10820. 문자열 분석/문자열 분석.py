## 문자열 분석

while True :
    try :
        sentence = input()
        if sentence == '' :
            break
    except :
        break

    lowercase, uppercase, numbercase, spacecase = 0,0,0,0

    for s in sentence :
        if s.isalpha() : # 알파벳
            if s.islower() : #소문자
                lowercase += 1
            else : # 대문자
                uppercase += 1
        else :
            if s.isnumeric() :
                numbercase += 1
            elif s == ' ' :
                spacecase += 1

    print(lowercase, uppercase, numbercase, spacecase)
