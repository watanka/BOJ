

def solution(users, emoticons):
    
    def yield_discount_combination(emoticons, prefix) :
        if not emoticons :
            yield prefix
            return
        for i in range(10, 50, 10) :
            price = emoticons[0] * (1 - 0.01 * i)
            yield from yield_discount_combination(emoticons[1:], prefix + [(i, price)])
    
    answer_price = answer_user = 0
    # discount의 조합은 [10, 20, 30, 40]
    # 전체 조합에 대해서 금액 계산 후, 최대 구독자 수, 최대 금액 반환
    for comb in yield_discount_combination(emoticons, []) :
        comb_price = comb_user = 0
        for criteria_rate, criteria_price in users : 
            price = sum(map(lambda x : x[1], filter(lambda x : x[0] >= criteria_rate, comb)))
            if price >= criteria_price :
                comb_user += 1
            else :
                comb_price += price
        if comb_user > answer_user or (comb_user == answer_user and comb_price > answer_price) :
            answer_user, answer_price = comb_user, comb_price
        
        
    return [answer_user, answer_price]

    
    
    