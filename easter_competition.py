import sys
number_easter_breads=int(input())
most_points=-sys.maxsize
best_baker=""
for _ in range(number_easter_breads):
    cooker_name=input()
    got_points=0
    sum_points=0
    while True:
        command=input()
        if command=="Stop":
            print(f"{cooker_name} has {got_points} points.")
            break
        grade_for_a_bread_for_a_person=int(command)
        got_points+=grade_for_a_bread_for_a_person
        if got_points>most_points:
            highest_points=got_points
            best_baker=cooker_name
            print(f"{cooker_name} is the new number 1!")
print(f"{best_baker} won competition with {highest_points} points!")