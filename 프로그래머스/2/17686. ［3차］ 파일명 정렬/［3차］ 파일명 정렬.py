def solution(files):
    answer = []
    
    # 파일명은 HEAD, NUMBER, TAIL로 이루어짐. TAIL은 없을 수도 있다
    # 정렬 규칙
    # 1. HEAD 사전 순(대소문자 구분 X)
    # 2. NUMBER 숫자순 9 < 10 < 0011 < 012 < 013 < 014. 숫자 앞 0 무시
    # 3. HEAD와 NUMBER도 같은 경우, 입력 들어온 순서를 유지
    
    dic = {}
    for file in files:
        head = ''
        number = ''
        pointer = 0
        on_number = False
        
        while pointer < len(file):
            if not file[pointer].isnumeric() and not on_number:
                head += file[pointer]
            
            elif file[pointer].isnumeric():
                on_number = True
                number += file[pointer]
            else:
                break
            pointer += 1
            
        print('head: ', head)
        print('number: ', number)
        dic[file] = (head.lower(), int(number))
    print(dic)
    return [x[0] for x in sorted(dic.items(), key=lambda x: (x[1][0], x[1][1]))]
    
            