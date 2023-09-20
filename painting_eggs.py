eggs_size = input()
eggs_color = input()
number_eggs = int(input())
price_for_sale = 0
price = 0
down = 0
if eggs_size == "Large":
    if eggs_color == "Red":
        price_for_sale = 16

    elif eggs_color == "Green":
        price_for_sale = 12

    else:
        price_for_sale = 9

elif eggs_size == "Medium":
    if eggs_color == "Red":
        price_for_sale = 13

    elif eggs_color == "Green":
        price_for_sale = 9

    else:
        price_for_sale = 7
else:
    if eggs_color == "Red":
        price_for_sale = 9

    elif eggs_color == "Green":
        price_for_sale = 8

    else:
        price_for_sale = 5

price = price_for_sale * number_eggs

down = price*35/100

after_sum = price - down

print(f"{after_sum:.2f} leva.")

