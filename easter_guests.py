import math
number_guests = int(input())
lubo_s_budget = int(input())
sweat_brea = 4
egg = 0.45
number_easter_breads = 0
nuber_eggs = 0
price_for_easter_bread=0
number_easter_breads = number_guests / 3
nuber_eggs=number_guests*2
price_for_easter_bread=sweat_brea*math.ceil(number_easter_breads)
price_for_eggs=nuber_eggs*egg
sum=price_for_easter_bread+price_for_eggs
difference=abs(sum-lubo_s_budget)
if sum<=lubo_s_budget:
    print(f"Lyubo bought {math.ceil(number_easter_breads)} Easter bread and {nuber_eggs} eggs.")
    print(f"He has {difference:.2f} lv. left.")
else:
    print("Lyubo doesn't have enough money.")
    print(f"He needs {difference:.2f} lv. more.")

