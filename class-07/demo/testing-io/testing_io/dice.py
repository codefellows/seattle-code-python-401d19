from random import randint


def play_dice(roll_dice):
    while True:
        print("Enter r to roll or q to quit")
        choice = input("> ")
        if choice == "q":
            print("OK, bye")
            break
        elif choice == "r":
            # roll the dice
            roll = roll_dice()
            values_in_roll = []
            for value in roll:
                values_in_roll.append(str(value))

            formatted_roll = " ".join(values_in_roll)

            print(f"*** {formatted_roll} ***")  # TODO turn (1, 3) into "1 3"


def default_dice_roller():
    return randint(1, 6), randint(1, 6)


def dice_roller_4_3():
    return (4, 3)

# def dice_roller_dynamic():
#     nums = input("")
#     return the numbers as tuples, maybe


if __name__ == '__main__':
    play_dice(dice_roller_4_3) # normally default_dice_roller
