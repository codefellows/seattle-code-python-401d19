def play():
    choice = invite_to_play()

    if choice == "y":
        start_game()
    else:
        decline_game()


def invite_to_play():
    print("Welcome to Ten Thousand")
    print("(y)es to play or (n)o to decline")
    choice = input("> ")
    return choice


def start_game():
    round_num = 1
    max_round = 20
    total_points = 0

    while round_num <= max_round:
        round_result = do_round(round_num)
        if round_result == "q":
            break

        total_points += round_result
        round_num += 1

    print(f"Thanks for playing. You earned {total_points} points")


def do_round(round_num):
    """
    Play a round of the game
    Args:
        round_num:

    Returns:
        "q" if user quits or
        points earned in the round
    """
    print(f"Starting round {round_num}")

    # TODO: all the logic for playing a round
    # temp code below
    if round_num > 5:
        return "q"

    return 150


def decline_game():
    print("OK. Maybe another time")


if __name__ == "__main__":
    play()
