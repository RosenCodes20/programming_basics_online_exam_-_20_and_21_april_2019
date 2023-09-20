number_of_eggs_for_the_first_player = int(input())
number_of_eggs_for_the_second_player = int(input())
while True:
    winner = input()
    if winner == "one":
        number_of_eggs_for_the_second_player -= 1
    elif winner == "two":
        number_of_eggs_for_the_first_player -= 1

    if number_of_eggs_for_the_first_player == 0:
        print(f"Player one is out of eggs. Player two has {number_of_eggs_for_the_second_player} eggs left.")
        break
    if number_of_eggs_for_the_second_player == 0:
        print(f"Player two is out of eggs. Player one has {number_of_eggs_for_the_first_player} eggs left.")
        break
    if winner == "End":
        print(f"Player one has {number_of_eggs_for_the_first_player} eggs left.")
        print(f"Player two has {number_of_eggs_for_the_second_player} eggs left.")
        break
