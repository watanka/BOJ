

def calculate_time(str_today, str_date) -> int :
    today_year, today_month, today_date = str_today.split('.')
    Y, M, D = str_date.split('.')
    
    pass_date = int(today_date) - int(D)
    month_remainder = 0
    if pass_date < 0 :
        pass_date += 28
        month_remainder = -1
    
    year_remainder = 0
    pass_month = int(today_month) - int(M) + month_remainder
    if pass_month < 0 :
        pass_month += 12
        year_remainder = -1
        
    pass_year = int(today_year) - int(Y) + year_remainder
    
    month_passed = pass_year * 12 + pass_month
    
    return month_passed + (0.5 if pass_date else 0)
    

def solution(today, terms, privacies):
    answer = []
    
    # today = {"YYYY.MM.DD"}
    # terms = "약관종류 유효기간"
    # privacies = ['계약날짜 약관종류']
    
    term_dict = {t.split()[0] : int(t.split()[1]) for t in terms}
    
    for idx, private_info in enumerate(privacies) :
        str_date, term_type = private_info.split()
        time_passed = calculate_time(today, str_date)
        
        val_time = term_dict[term_type]
        
        if time_passed >= val_time :
            answer.append(idx + 1)
    
    
    return answer