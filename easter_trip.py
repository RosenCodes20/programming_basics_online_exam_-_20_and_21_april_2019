destination=input()
dates=input()
number_nights=int(input())
price_for_night=0
if destination=="France":
    if dates=="21-23":
        price_for_night=30
    elif dates=="24-27":
        price_for_night=35
    else:
        price_for_night=40
elif destination=="Italy":
    if dates=="21-23":
        price_for_night=28
    elif dates=="24-27":
        price_for_night=32
    else:
        price_for_night=39
else:
    if dates=="21-23":
        price_for_night=32
    elif dates=="24-27":
        price_for_night=37
    else:
        price_for_night=43
sum=price_for_night*number_nights
print(f"Easter trip to {destination} : {sum:.2f} leva.")
