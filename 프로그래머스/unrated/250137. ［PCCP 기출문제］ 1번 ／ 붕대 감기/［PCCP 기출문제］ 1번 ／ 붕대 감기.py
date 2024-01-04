def solution(bandage, health, attacks):
    answer = 0
    max_health = health
    
    required_heal_time, heal_per_sec, extra_heal = bandage
    
    time_range = range(0, attacks[-1][0] + 1)
    
    attack_dict = {attack_time : damage for attack_time, damage in attacks}
    
    total_heal_time = 0
    
    for time in time_range : 
        
        if time in attack_dict.keys() :
            total_heal_time = 0
            health -= attack_dict[time]
            
            if health <= 0 :
                return -1

        else :
            total_heal_time += 1
            
            if total_heal_time == required_heal_time :
                health = min(max_health, health + extra_heal)
                total_heal_time = 0 
            
            health = min(max_health, health + heal_per_sec)
            

            
        
    
    return health