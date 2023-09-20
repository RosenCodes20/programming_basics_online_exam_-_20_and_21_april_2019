start_quantity_of_eggs = int(input())
sold_eggs = 0
while True:
    command_for_adding_or_filling_eggs = input()
    if command_for_adding_or_filling_eggs == "Close":
        print("Store is closed!")
        print(f"{sold_eggs} eggs sold.")
        break
    else:
        added_eggs = int(input())
    if command_for_adding_or_filling_eggs == "Buy":
        start_quantity_of_eggs = start_quantity_of_eggs - added_eggs
        sold_eggs += added_eggs
    else:
        start_quantity_of_eggs = start_quantity_of_eggs + added_eggs
    if start_quantity_of_eggs < 0:
        print("Not enough eggs in store!")
        print(f"You can buy only {start_quantity_of_eggs + added_eggs}.")
        break
