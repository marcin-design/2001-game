import random


def dice_roll(dice_code):
    POSSIBLE_DICES = {
        "D3", "D4", "D6", "D8", "D10", "D12", "D20", "D100",
    }

    for dice in POSSIBLE_DICES:
        if dice in dice_code:
            try:
                x, y = dice_code.split(dice)
            except ValueError:
                return "Wrong Input"
            dice_value = int(dice[1:])
            break
    else:
        return "Wrong Input"

    try:
        x = int(x) if x else 1
    except ValueError:
        return "Wrong Input"

    try:
        y = int(y) if y else 0
    except ValueError:
        return "Wrong Input"

    return sum([random.randint(1, dice_value) for _ in range(x)]) + y


def game():
    print("""            
                        !!!Here is a 2001 game!!! 
    Let's fight against the computer to collect 2001 points faster by using dice. 
       Choose two dice per roll or use 'Enter' button to make the odds even. 
            The computer will choose random two dice every time
        Dice types in the game: D3, D4, D6, D8, D10, D12, D20, D100
                             Let's begin!
    """)
    user_points = 0
    comp_points = 0
    user_roll = 0
    user_roll_2 = 0
    comp_roll = 0
    comp_roll_2 = 0
    POSSIBLE_DICES = {
        "D3",
        "D4",
        "D6",
        "D8",
        "D10",
        "D12",
        "D20",
        "D100",
    }

    while user_points <= 1001 and comp_points <= 1001:
        user_dice_code = input("Choose type of the first dice (or press Enter for random): ")
        if user_dice_code == "":
            user_dice_code = random.choice(list(POSSIBLE_DICES))

        if user_dice_code not in POSSIBLE_DICES:
            print("Dice code cannot be found")
            continue

        user_roll = dice_roll(user_dice_code)

        user_dice_code_2 = input("Choose type of the second dice (or press Enter for random): ")
        if user_dice_code_2 == "":
            user_dice_code_2 = random.choice(list(POSSIBLE_DICES))

        if user_dice_code_2 not in POSSIBLE_DICES:
            print("Dice code cannot be found")
            continue
        print("")

        user_roll_2 = dice_roll(user_dice_code_2)

        comp_dice_code = random.choice(list(POSSIBLE_DICES))
        comp_roll = dice_roll(comp_dice_code)

        comp_dice_code_2 = random.choice(list(POSSIBLE_DICES))
        comp_roll_2 = dice_roll(comp_dice_code_2)

        user_points += user_roll + user_roll_2
        comp_points += comp_roll + comp_roll_2

        if 7 in (user_roll, user_roll_2):
            user_points //= 7
        if 11 in (user_roll, user_roll_2):
            user_points *= 11

        if 7 in (comp_roll, comp_roll_2):
            comp_points //= 7
        if 11 in (comp_roll, comp_roll_2):
            comp_points *= 11

        print(f"User rolled: {user_roll} and {user_roll_2}")
        print(f"User current points: {user_points}")
        print(f"User used dice: {user_dice_code} and {user_dice_code_2}")
        print("")
        print(f"Computer rolled: {comp_roll} and {comp_roll_2}")
        print(f"Computer current points: {comp_points}")
        print(f"Computer used dice: {comp_dice_code} and {comp_dice_code_2}")
        print("")

        if user_points >= 2001 and comp_points >= 2001:
            print("It's a draw")
            break
        if user_points >= 2001:
            print("The user won!")
            break
        if comp_points >= 2001:
            print("The computer won!")
            break

game()
