# def solution(cap, n, deliveries, pickups):
#     answer = 0
    
#     trg_idx = n - 1
    
#     while trg_idx >= 0:
#         while trg_idx >= 0 and deliveries[trg_idx] == 0 and pickups[trg_idx] == 0 :
#             trg_idx -= 1

#         num_deliver = cap
#         num_collect = cap
        
#         deliver_idx = trg_idx
#         collect_idx = trg_idx
        
#         while num_deliver > 0 and deliver_idx >= 0 :
#             to_deliver = min(num_deliver, deliveries[deliver_idx])
#             deliveries[deliver_idx] -= to_deliver
#             num_deliver -= to_deliver
#             deliver_idx -= 1
        
#         while num_collect > 0 and collect_idx >= 0 :
#             to_pickup = min(num_collect, pickups[collect_idx])
#             pickups[collect_idx] -= to_pickup
#             num_collect -= to_pickup
#             collect_idx -= 1
            
#         answer += (trg_idx + 1) * 2

#     return answer

def solution(cap, n, deliveries, pickups):
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    answer = 0

    have_to_deli = 0
    have_to_pick = 0

    for i in range(n):
        have_to_deli += deliveries[i]
        have_to_pick += pickups[i]

        while have_to_deli > 0 or have_to_pick > 0:
            have_to_deli -= cap
            have_to_pick -= cap
            answer += (n - i) * 2

    return answer