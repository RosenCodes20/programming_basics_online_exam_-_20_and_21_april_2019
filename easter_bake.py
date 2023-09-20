import math
number_easter_breads=int(input())
sum_needed_sugar=0
sum_needed_flour=0
number_packets_of_sugar=0
number_packets_of_flour=0
max_used_sugar=0
max_used_flour=0
for breads in range(number_easter_breads):
    quantity_gived_sugar=int(input())
    quantity_gived_flour=int(input())
    sum_needed_sugar+=quantity_gived_sugar
    sum_needed_flour+=quantity_gived_flour

    if quantity_gived_sugar>max_used_sugar:
        max_used_sugar=quantity_gived_sugar
    if quantity_gived_flour>max_used_flour:
        max_used_flour=quantity_gived_flour

number_packets_of_sugar=math.ceil(sum_needed_sugar/950)
number_packets_of_flour=math.ceil(sum_needed_flour/750)
print(f"Sugar: {number_packets_of_sugar}")
print(f"Flour: {number_packets_of_flour}")
print(f"Max used flour is {max_used_flour} grams, max used sugar is {max_used_sugar} grams.")