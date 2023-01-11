## 손익분기점
import math

fixed_cost, per_cost, per_price = map(int, input().split())

if per_price > per_cost :
    breakeven_point = fixed_cost // (per_price - per_cost) + 1
else :
    breakeven_point = -1





print( breakeven_point)