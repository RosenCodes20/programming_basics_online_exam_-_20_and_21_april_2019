price_for_flour_for_kg=float(input())
kg_flour=float(input())
kg_sugar=float(input())
number_eggs=int(input())
packets_of_maya=int(input())
price_of_the_sugar=price_for_flour_for_kg*0.75
price_of_the_eggs=price_for_flour_for_kg*1.1
price_for_maya=price_of_the_sugar*0.2
sum_of_the_flour=price_for_flour_for_kg*kg_flour
sum_of_the_sugar=price_of_the_sugar*kg_sugar
sum_of_the_eggs=price_of_the_eggs*number_eggs
sum_of_the_maya=price_for_maya*packets_of_maya
total=sum_of_the_flour+sum_of_the_sugar+sum_of_the_eggs+sum_of_the_maya
print(f"{total:.2f}")