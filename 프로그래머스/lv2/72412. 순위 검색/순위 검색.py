from bisect import bisect_left
def bisect(ls, value) :
    l = 0
    r = len(ls) - 1
    idx = 0
    
    while l <= r :
        mid = (l + r) // 2
        
        if ls[mid] >= value :
            idx = mid
            r = mid - 1
        else :
            l = mid + 1
            
    return idx

def solution(info, query):
    answer = []
    
    db = dict()
    
    # language 
    lang_list = ['cpp', 'java', 'python', '-']
    # job
    job_list = ['backend', 'frontend', '-']
    # level
    level_list = ['junior', 'senior', '-']
    # food
    food_list = ['chicken', 'pizza', '-']
    
    
    # 이들의 조합으로 key 생성
    for lang in lang_list :
        for job in job_list :
            for level in level_list :
                for food in food_list :
                    db[f'{lang}_{job}_{level}_{food}'] = []
                    
    for personal_info in info :
        lang, job, level, food, score = personal_info.split()
        score = int(score)
        
        for l in [lang, '-'] :
            for j in [job, '-'] :
                for lev in [level, '-'] :
                    for f in [food, '-'] :
                        db[f'{l}_{j}_{lev}_{f}'].append(score)
    
    for key, value in db.items() : 
        db[key] = sorted(value)
    
    
    
    for q in query :
        # query formatting
        q_lang, q_job, q_level, q_food, q_score = [cond for cond in q.split() if cond != 'and']
        q_score = int(q_score)
        
        candidates = db[f'{q_lang}_{q_job}_{q_level}_{q_food}']
        # print(candidates)    
        # print(bisect_left(candidates, q_score))
        
        answer.append(len(candidates) - bisect_left(candidates, q_score))
    
    
    
    
    return answer