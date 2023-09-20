number_guests = int(input())
price_for_a_person = float(input())
desi_s_budget = float(input())
down = 0
price_for_cake = 0
sum_for_party = 0
if 10 <= number_guests <= 15:
    down = price_for_a_person - (price_for_a_person * 1.5) / 10
elif 15 < number_guests <= 20:
    down = price_for_a_person - (price_for_a_person * 2.0) / 10
elif number_guests > 20:
    down = price_for_a_person - (price_for_a_person * 2.5) / 10
elif number_guests<10:
    down=price_for_a_person
price_for_cake = 0.1 * desi_s_budget
sum_for_party = number_guests * down + price_for_cake
difference = abs(desi_s_budget - sum_for_party)
if sum_for_party >= desi_s_budget:
    print(f"No party! {difference:.2f} leva needed.")
else:
    print(f"It is party time! {difference:.2f} leva left.")

