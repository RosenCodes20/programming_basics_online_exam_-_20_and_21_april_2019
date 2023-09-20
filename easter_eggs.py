number_colored_eggs=int(input())
red_eggs=0
orange_eggs=0
blue_eggs=0
green_eggs=0
max_eggs=0
color=""
for eggs in range(number_colored_eggs):
    eggs_color=input()
    if eggs_color=="red":
        red_eggs+=1
    elif eggs_color == "orange":
        orange_eggs += 1
    elif eggs_color=="blue":
        blue_eggs+=1
    elif eggs_color=="green":
        green_eggs+=1

    if red_eggs>orange_eggs and red_eggs>blue_eggs and red_eggs>green_eggs:
        max_eggs=red_eggs
        color="red"

    if orange_eggs>red_eggs and orange_eggs>blue_eggs and orange_eggs>green_eggs:
        max_eggs=orange_eggs
        color="orange"

    if blue_eggs>red_eggs and blue_eggs>orange_eggs and blue_eggs>green_eggs:
        max_eggs=blue_eggs
        color="blue"

    if green_eggs>blue_eggs and green_eggs>red_eggs and green_eggs>orange_eggs:
        max_eggs=green_eggs
        color="green"

print(f"Red eggs: {red_eggs}")
print(f"Orange eggs: {orange_eggs}")
print(f"Blue eggs: {blue_eggs}")
print(f"Green eggs: {green_eggs}")
print(f"Max eggs: {max_eggs} -> {color}")
