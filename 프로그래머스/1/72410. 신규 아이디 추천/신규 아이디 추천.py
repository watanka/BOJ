import re

def solution(new_id):
    answer = ''
    
    # 빈 문자열이라면 'a' 대입
    def fill_if_empty(id):
        if id == '':
            return 'a'
        else:
            return id

    def lower_case_only(id):
        """
        대문자 -> 소문자
        """
        return id.lower()
    
    def clean_string(id):
        """
        소문자, 숫자, -, _, . 제외한 모든 문자 제거
        """
        return re.sub(r'[^a-z0-9\-\_\.]', '', id)
    
    def reduce_dots(id):
        """
        마침표가 2번 이상 반복될 경우 하나의 마침표로 치환
        """
        return re.sub(r'\.{2,}', '.', id)
     
    def remove_first_and_last_period(id):
        """
        마침표가 처음이나 끝에 위치하면 제거
        """
        if id.startswith('.'):
            id = id[1:]
        if id.endswith('.'):
            id = id[:-1]
        return id
    
    def remove_if_longer_than_16(id): 
        """
        길이가 16자 이상이면, 15개 제외 모두 제거. 제거 후 마침표가 new_id 끝에 위치한다면 마침표 문자 제거
        """
        if len(id) >= 16:
            id = id[:15]
            if id.endswith('.'):
                id = id[:-1]
        return id
    
    def extend_id_if_shorter_than_2(id):
        if len(id) <= 2:
            last_letter = id[-1]
        while len(id) < 3:
            id += last_letter
        return id
    
    
    answer = lower_case_only(new_id)
    
    answer = clean_string(answer)
    
    answer = reduce_dots(answer)
    
    answer = remove_first_and_last_period(answer)
    
    answer = fill_if_empty(answer)
    
    answer = remove_if_longer_than_16(answer)
    

    
    answer = extend_id_if_shorter_than_2(answer)
    
    
    return answer