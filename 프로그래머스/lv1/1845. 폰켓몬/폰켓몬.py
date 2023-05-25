def solution(nums):
    ponket_dict = {}
    for species in nums :
        if species not in ponket_dict.keys() :
            ponket_dict[species] = 1
        else :
            ponket_dict[species] += 1
    answer = min(len(ponket_dict), len(nums) // 2)
        
    return answer