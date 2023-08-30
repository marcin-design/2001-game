import random
#Typical dice tempalte: xDy+z
def dice_roll(dice_code):
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
    for dice in POSSIBLE_DICES:
        if dice in dice_code:
            try:
                x, y, = dice_code.split(dice)
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
                            Here is a 2001 game.
    Let's fight each other to collect 2001 points faster by using dice.
                               Let's begin!
    
    Dice types in the game: D3, D4, D6, D8, D10, D12, D20, D100.
    Otherwise choose them from the box and type the dice code like: D100
    """)
    user_points = 0
    comp_points = 0
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
    while user_points <= 100 and comp_points <= 100:
        user_dice_code = input("Chose type of the first dice:")
        user_roll = dice_roll(user_dice_code)
        if user_dice_code not in POSSIBLE_DICES:
            print("Dice code cannot be found")
            continue

        user_dice_code_2 = ""
        while user_dice_code_2 not in POSSIBLE_DICES:
            user_dice_code_2 = input("Choose type of the second dice: ")
            user_roll_2 = dice_roll(user_dice_code_2)
            print("Dice code cannot be found")
            continue

        comp_dice_code = random.choice(list(POSSIBLE_DICES))
        comp_roll = dice_roll(comp_dice_code)

        comp_dice_code_2 = random.choice(list(POSSIBLE_DICES))
        comp_roll_2 = dice_roll(comp_dice_code_2)

        user_points += user_roll + user_roll_2
        comp_points += comp_roll + comp_roll_2
        print(f"You rolled: {user_roll} and {user_roll_2}")
        print(f"Your current points: {user_points}")
        print("")
        print(f"I rolled: {comp_roll} and {comp_roll_2}")
        print(f"My current points: {comp_points}")
        print(f"Used dices: {comp_dice_code} and {comp_dice_code_2}")
        print("")

        if user_roll == 7 or user_roll_2 == 7:
            int(user_points) // 7
        if user_roll == 11 or user_roll_2:
            int(user_points) * 11

        if comp_roll == 7 or comp_roll_2:
            comp_points //= 7
        if comp_roll == 11 or comp_roll_2:
            comp_points *= 11

        if user_points >= 100 and comp_points >= 100:
            print("It's a draw")
            break
        if user_points >= 100:
            print("You won! (user)")
        if comp_points >= 100:
            print("I won! (comp)")

game()